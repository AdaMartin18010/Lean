#!/usr/bin/env python3
"""
Simple Content Validator for lean/analysis
"""

import os
import re
from pathlib import Path

def check_numbering():
    """检查编号一致性"""
    print("检查编号体系...")
    errors = []
    
    for md_file in Path(".").rglob("*.md"):
        if md_file.name in ["README.md", "cross-reference-index.md"]:
            continue
            
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if line.startswith('#'):
                if not re.match(r'^#+\s+\d+\.\d+', line):
                    errors.append(f"{md_file}:{i+1} - {line.strip()}")
    
    return errors

def check_cross_references():
    """检查交叉引用"""
    print("检查交叉引用...")
    errors = []
    
    for md_file in Path(".").rglob("*.md"):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        refs = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
        for ref_text, ref_path in refs:
            if ref_path.startswith('http'):
                continue
                
            ref_file = md_file.parent / ref_path
            if not ref_file.exists():
                errors.append(f"{md_file}: {ref_text} -> {ref_path}")
    
    return errors

def main():
    """主函数"""
    print("开始内容验证...")
    
    numbering_errors = check_numbering()
    cross_ref_errors = check_cross_references()
    
    print(f"\n编号错误: {len(numbering_errors)}")
    print(f"交叉引用错误: {len(cross_ref_errors)}")
    
    if numbering_errors or cross_ref_errors:
        print("发现错误，请检查并修复。")
        return False
    else:
        print("✅ 验证通过！")
        return True

if __name__ == "__main__":
    main() 