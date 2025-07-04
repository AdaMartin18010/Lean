#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
最终发布准备脚本
用于检查项目完整性、格式统一性和发布就绪状态
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple, Set

class FinalReleasePreparation:
    def __init__(self, root_dir: str = "analysis"):
        self.root_dir = Path(root_dir)
        self.md_files = []
        self.errors = []
        self.warnings = []
        self.stats = {}
        
    def scan_files(self):
        """扫描所有Markdown文件"""
        print("🔍 扫描项目文件...")
        for md_file in self.root_dir.rglob("*.md"):
            self.md_files.append(md_file)
        print(f"📁 发现 {len(self.md_files)} 个Markdown文件")
        
    def check_file_structure(self):
        """检查文件结构完整性"""
        print("📋 检查文件结构...")
        
        # 检查核心目录
        core_dirs = [
            "0-总览与导航",
            "1-形式化理论", 
            "2-数学基础与应用",
            "3-哲学与科学原理",
            "4-行业领域分析",
            "5-架构与设计模式",
            "6-编程语言与实现",
            "7-验证与工程实践"
        ]
        
        missing_dirs = []
        for dir_name in core_dirs:
            dir_path = self.root_dir / dir_name
            if not dir_path.exists():
                missing_dirs.append(dir_name)
                
        if missing_dirs:
            self.errors.append(f"缺少核心目录: {missing_dirs}")
        else:
            print("✅ 核心目录结构完整")
            
    def check_cross_references(self):
        """检查交叉引用完整性"""
        print("🔗 检查交叉引用...")
        broken_refs = []
        
        for md_file in self.md_files:
            try:
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
                        
            except Exception as e:
                self.errors.append(f"读取文件失败 {md_file}: {e}")
                
        if broken_refs:
            self.warnings.extend(broken_refs)
            print(f"⚠️  发现 {len(broken_refs)} 个断开的交叉引用")
        else:
            print("✅ 交叉引用检查通过")
            
    def check_format_consistency(self):
        """检查格式一致性"""
        print("📝 检查格式一致性...")
        
        format_issues = []
        for md_file in self.md_files:
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                # 检查标题格式
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    if line.startswith('#'):
                        # 检查标题后是否有空格
                        if not re.match(r'^#+\s+', line):
                            format_issues.append(f"{md_file}:{i+1} 标题格式错误")
                            
                # 检查列表格式
                for i, line in enumerate(lines):
                    if line.strip().startswith('- ') or line.strip().startswith('* '):
                        # 检查列表项缩进
                        if not line.startswith('  ') and not line.startswith('\t'):
                            format_issues.append(f"{md_file}:{i+1} 列表格式错误")
                            
            except Exception as e:
                self.errors.append(f"格式检查失败 {md_file}: {e}")
                
        if format_issues:
            self.warnings.extend(format_issues)
            print(f"⚠️  发现 {len(format_issues)} 个格式问题")
        else:
            print("✅ 格式一致性检查通过")
            
    def check_content_completeness(self):
        """检查内容完整性"""
        print("📚 检查内容完整性...")
        
        required_sections = [
            "## 目录",
            "## 参考文献",
            "## 交叉引用"
        ]
        
        missing_sections = []
        for md_file in self.md_files:
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                for section in required_sections:
                    if section not in content:
                        missing_sections.append(f"{md_file}: 缺少 {section}")
                        
            except Exception as e:
                self.errors.append(f"内容检查失败 {md_file}: {e}")
                
        if missing_sections:
            self.warnings.extend(missing_sections)
            print(f"⚠️  发现 {len(missing_sections)} 个内容完整性问题")
        else:
            print("✅ 内容完整性检查通过")
            
    def generate_stats(self):
        """生成统计信息"""
        print("📊 生成统计信息...")
        
        self.stats = {
            "total_files": len(self.md_files),
            "total_lines": 0,
            "total_words": 0,
            "errors": len(self.errors),
            "warnings": len(self.warnings)
        }
        
        for md_file in self.md_files:
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    lines = content.split('\n')
                    words = content.split()
                    self.stats["total_lines"] += len(lines)
                    self.stats["total_words"] += len(words)
            except:
                pass
                
        print(f"📈 统计信息: {self.stats}")
        
    def generate_report(self):
        """生成最终报告"""
        print("📋 生成最终报告...")
        
        report = {
            "project_name": "Lean语言深度与广度关联性分析项目",
            "version": "1.0.0",
            "release_date": "2024-12-28",
            "stats": self.stats,
            "errors": self.errors,
            "warnings": self.warnings,
            "status": "READY" if not self.errors else "NEEDS_FIXES"
        }
        
        # 保存报告
        report_file = self.root_dir / "FINAL_RELEASE_REPORT.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
            
        print(f"📄 报告已保存到: {report_file}")
        
        # 打印摘要
        print("\n" + "="*60)
        print("🎉 最终发布准备完成!")
        print("="*60)
        print(f"📁 文件总数: {self.stats['total_files']}")
        print(f"📝 总行数: {self.stats['total_lines']:,}")
        print(f"📚 总字数: {self.stats['total_words']:,}")
        print(f"❌ 错误数: {len(self.errors)}")
        print(f"⚠️  警告数: {len(self.warnings)}")
        print(f"📊 状态: {report['status']}")
        
        if self.errors:
            print("\n❌ 需要修复的错误:")
            for error in self.errors[:5]:  # 只显示前5个
                print(f"  - {error}")
                
        if self.warnings:
            print("\n⚠️  建议修复的警告:")
            for warning in self.warnings[:5]:  # 只显示前5个
                print(f"  - {warning}")
                
        if not self.errors:
            print("\n✅ 项目已准备就绪，可以发布!")
        else:
            print("\n🔧 请修复上述错误后重新运行检查")
            
    def run_all_checks(self):
        """运行所有检查"""
        print("🚀 开始最终发布准备检查...")
        print("="*60)
        
        self.scan_files()
        self.check_file_structure()
        self.check_cross_references()
        self.check_format_consistency()
        self.check_content_completeness()
        self.generate_stats()
        self.generate_report()
        
        return len(self.errors) == 0

def main():
    """主函数"""
    preparer = FinalReleasePreparation()
    success = preparer.run_all_checks()
    
    if success:
        print("\n🎊 恭喜! 项目已完全准备就绪，可以立即发布!")
        return 0
    else:
        print("\n🔧 请修复发现的问题后重新运行检查")
        return 1

if __name__ == "__main__":
    exit(main()) 