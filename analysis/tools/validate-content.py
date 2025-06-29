#!/usr/bin/env python3
"""
Content Validation Tool for lean/analysis
Checks cross-references, numbering, and format consistency
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Dict, Set, Tuple

class ContentValidator:
    def __init__(self, root_dir: str = "."):
        self.root_dir = Path(root_dir)
        self.cross_refs: Dict[str, Set[str]] = {}
        self.numbering_errors: List[str] = []
        self.format_errors: List[str] = []
        
    def validate_all(self) -> bool:
        """执行所有验证检查"""
        print("🔍 开始内容验证...")
        
        success = True
        success &= self.check_numbering()
        success &= self.check_cross_references()
        success &= self.check_format()
        success &= self.check_latex_syntax()
        
        self.print_report()
        return success
    
    def check_numbering(self) -> bool:
        """检查编号一致性"""
        print("📋 检查编号体系...")
        
        for md_file in self.root_dir.rglob("*.md"):
            if md_file.name in ["README.md", "cross-reference-index.md", "content-update-guide.md"]:
                continue
                
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # 检查标题编号
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if line.startswith('#'):
                    # 检查编号格式
                    if not re.match(r'^#+\s+\d+\.\d+', line):
                        self.numbering_errors.append(f"{md_file}:{i+1} - 缺少编号: {line.strip()}")
        
        return len(self.numbering_errors) == 0
    
    def check_cross_references(self) -> bool:
        """检查交叉引用完整性"""
        print("🔗 检查交叉引用...")
        
        # 收集所有文件路径
        all_files = set()
        for md_file in self.root_dir.rglob("*.md"):
            all_files.add(md_file.relative_to(self.root_dir))
        
        # 检查交叉引用
        broken_refs = []
        for md_file in self.root_dir.rglob("*.md"):
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # 查找交叉引用
            refs = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
            for ref_text, ref_path in refs:
                if ref_path.startswith('http'):
                    continue
                    
                # 解析相对路径
                ref_file = md_file.parent / ref_path
                if not ref_file.exists():
                    broken_refs.append(f"{md_file}: {ref_text} -> {ref_path}")
        
        self.format_errors.extend(broken_refs)
        return len(broken_refs) == 0
    
    def check_format(self) -> bool:
        """检查格式一致性"""
        print("📝 检查格式规范...")
        
        for md_file in self.root_dir.rglob("*.md"):
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # 检查LaTeX块
            latex_blocks = re.findall(r'```latex\s*\n(.*?)\n```', content, re.DOTALL)
            for block in latex_blocks:
                if not re.search(r'\\\[.*\\\]', block):
                    self.format_errors.append(f"{md_file}: LaTeX块缺少块级公式")
            
            # 检查代码块
            code_blocks = re.findall(r'```(\w+)\s*\n(.*?)\n```', content, re.DOTALL)
            for lang, code in code_blocks:
                if lang not in ['lean', 'rust', 'haskell', 'mermaid']:
                    self.format_errors.append(f"{md_file}: 不支持的代码语言: {lang}")
        
        return len(self.format_errors) == 0
    
    def check_latex_syntax(self) -> bool:
        """检查LaTeX语法"""
        print("🧮 检查LaTeX语法...")
        
        for md_file in self.root_dir.rglob("*.md"):
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # 检查LaTeX表达式
            latex_exprs = re.findall(r'\\\[(.*?)\\\]', content, re.DOTALL)
            for expr in latex_exprs:
                # 基本语法检查
                if '\\' in expr and not re.search(r'\\[a-zA-Z]+', expr):
                    self.format_errors.append(f"{md_file}: 可疑的LaTeX语法: {expr[:50]}...")
        
        return True
    
    def print_report(self):
        """打印验证报告"""
        print("\n" + "="*50)
        print("📊 验证报告")
        print("="*50)
        
        if self.numbering_errors:
            print(f"\n❌ 编号错误 ({len(self.numbering_errors)}):")
            for error in self.numbering_errors[:5]:  # 只显示前5个
                print(f"  - {error}")
            if len(self.numbering_errors) > 5:
                print(f"  ... 还有 {len(self.numbering_errors) - 5} 个错误")
        
        if self.format_errors:
            print(f"\n❌ 格式错误 ({len(self.format_errors)}):")
            for error in self.format_errors[:5]:  # 只显示前5个
                print(f"  - {error}")
            if len(self.format_errors) > 5:
                print(f"  ... 还有 {len(self.format_errors) - 5} 个错误")
        
        if not self.numbering_errors and not self.format_errors:
            print("\n✅ 所有检查通过！")
        
        print("\n" + "="*50)

def main():
    """主函数"""
    validator = ContentValidator()
    success = validator.validate_all()
    
    if not success:
        print("\n⚠️  发现一些问题，请检查并修复。")
        sys.exit(1)
    else:
        print("\n🎉 内容验证完成！")

if __name__ == "__main__":
    main() 