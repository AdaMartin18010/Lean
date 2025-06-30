#!/usr/bin/env python3
"""
Project Completeness Checker for Lean Formal Knowledge System

This tool analyzes the completeness and quality of the analysis framework,
checking for missing English mirrors, content quality, and cross-references.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple, Set
from dataclasses import dataclass
import argparse

@dataclass
class ContentMetrics:
    """Metrics for content analysis"""
    file_path: str
    line_count: int
    word_count: int
    code_blocks: int
    formulas: int
    diagrams: int
    references: int
    has_english_mirror: bool
    quality_score: float

@dataclass
class ProjectStatus:
    """Overall project status"""
    total_files: int
    completed_files: int
    english_mirrors: int
    missing_mirrors: List[str]
    low_quality_files: List[str]
    broken_links: List[str]
    overall_completion: float

class CompletenessChecker:
    def __init__(self, base_dir: str = "analysis"):
        self.base_dir = Path(base_dir)
        self.chinese_dirs = [
            "0-总览与导航",
            "1-形式化理论", 
            "2-数学基础与应用",
            "3-哲学与科学原理",
            "4-行业领域分析",
            "5-架构与设计模式", 
            "6-编程语言与实现",
            "7-验证与工程实践"
        ]
        self.english_dirs = [
            "0-Overview-and-Navigation",
            "1-formal-theory",
            "2-mathematics-and-applications", 
            "3-philosophy-and-scientific-principles",
            "4-industry-domains-analysis",
            "5-architecture-and-design-patterns",
            "6-programming-languages-and-implementation",
            "7-verification-and-engineering-practice"
        ]
    
    def analyze_file_content(self, file_path: Path) -> ContentMetrics:
        """Analyze individual file content quality"""
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # Basic metrics
            lines = content.split('\n')
            line_count = len(lines)
            word_count = len(content.split())
            
            # Content quality indicators
            code_blocks = len(re.findall(r'```[\s\S]*?```', content))
            formulas = len(re.findall(r'\$[\s\S]*?\$|\\\[[\s\S]*?\\\]', content))
            diagrams = len(re.findall(r'```mermaid[\s\S]*?```', content))
            references = len(re.findall(r'##.*[Rr]eferences|##.*参考文献', content))
            
            # Check for English mirror
            has_english_mirror = self.check_english_mirror(file_path)
            
            # Calculate quality score
            quality_score = self.calculate_quality_score(
                line_count, word_count, code_blocks, formulas, diagrams, references
            )
            
            return ContentMetrics(
                file_path=str(file_path),
                line_count=line_count,
                word_count=word_count,
                code_blocks=code_blocks,
                formulas=formulas,
                diagrams=diagrams,
                references=references,
                has_english_mirror=has_english_mirror,
                quality_score=quality_score
            )
            
        except Exception as e:
            print(f"Error analyzing {file_path}: {e}")
            return ContentMetrics(
                file_path=str(file_path),
                line_count=0, word_count=0, code_blocks=0,
                formulas=0, diagrams=0, references=0,
                has_english_mirror=False, quality_score=0.0
            )
    
    def calculate_quality_score(self, lines: int, words: int, code: int, 
                              formulas: int, diagrams: int, refs: int) -> float:
        """Calculate content quality score (0-100)"""
        score = 0.0
        
        # Length score (0-30 points)
        if lines > 1000:
            score += 30
        elif lines > 500:
            score += 20
        elif lines > 100:
            score += 10
        elif lines > 50:
            score += 5
        
        # Code examples (0-25 points)
        if code >= 10:
            score += 25
        elif code >= 5:
            score += 15
        elif code >= 2:
            score += 10
        elif code >= 1:
            score += 5
        
        # Mathematical content (0-20 points)
        if formulas >= 10:
            score += 20
        elif formulas >= 5:
            score += 15
        elif formulas >= 2:
            score += 10
        elif formulas >= 1:
            score += 5
        
        # Visual content (0-15 points)
        if diagrams >= 5:
            score += 15
        elif diagrams >= 3:
            score += 10
        elif diagrams >= 1:
            score += 5
        
        # References (0-10 points)
        if refs >= 1:
            score += 10
        
        return min(score, 100.0)
    
    def check_english_mirror(self, chinese_file: Path) -> bool:
        """Check if English mirror exists for Chinese file"""
        relative_path = chinese_file.relative_to(self.base_dir)
        path_parts = list(relative_path.parts)
        
        # Map Chinese directory to English
        if len(path_parts) > 0:
            chinese_dir = path_parts[0]
            if chinese_dir in self.chinese_dirs:
                idx = self.chinese_dirs.index(chinese_dir)
                english_dir = self.english_dirs[idx]
                path_parts[0] = english_dir
                
                # Map Chinese filename to English equivalent
                filename = path_parts[-1]
                english_filename = self.map_filename_to_english(filename)
                if english_filename:
                    path_parts[-1] = english_filename
                    english_path = self.base_dir / Path(*path_parts)
                    return english_path.exists()
        
        return False
    
    def map_filename_to_english(self, chinese_filename: str) -> str:
        """Map Chinese filename to English equivalent"""
        mapping = {
            # Navigation files
            "0.1-全局主题树形目录.md": "0.1-Global-Topic-Tree.md",
            "0.2-交叉引用与本地跳转说明.md": "0.2-Cross-References-and-Local-Navigation.md",
            "0.3-持续上下文进度文档.md": "0.3-Continuous-Context-Progress.md",
            
            # Formal theory
            "1.1-统一形式化理论综述.md": "1.1-unified-formal-theory-overview.md",
            "1.x-其他形式化主题.md": "1.x-other-formal-topics.md",
            
            # Mathematics  
            "2.1-数学内容全景分析.md": "2.1-mathematical-content-panoramic-analysis.md",
            "2.2-数学与形式化语言关系.md": "2.2-mathematics-and-formal-language.md",
            "2.x-其他数学主题.md": "2.x-other-mathematics-topics.md",
            
            # Philosophy
            "3.1-哲学内容全景分析.md": "3.1-philosophy-content-panoramic-analysis.md", 
            "3.2-哲学与形式化推理.md": "3.2-philosophy-and-formal-reasoning.md",
            "3.x-其他哲学主题.md": "3.x-other-philosophy-topics.md",
            
            # Industry domains
            "4.1-人工智能与机器学习.md": "4.1-artificial-intelligence-and-machine-learning.md",
            "4.2-物联网与边缘计算.md": "4.2-internet-of-things-and-edge-computing.md",
            "4.x-其他行业主题.md": "4.x-other-industry-topics.md",
            
            # Architecture
            "5.1-架构设计与形式化分析.md": "5.1-architecture-design-and-formal-analysis.md",
            "5.2-设计模式与代码实践.md": "5.2-design-patterns-and-code-practice.md", 
            "5.x-其他架构主题.md": "5.x-other-architecture-topics.md",
            
            # Programming languages
            "6.1-lean语言与形式化证明.md": "6.1-lean-language-and-formal-proof.md",
            "6.2-rust_haskell代码实践.md": "6.2-rust-haskell-code-practice.md",
            "6.x-其他实现主题.md": "6.x-other-implementation-topics.md",
            
            # Verification
            "7.1-形式化验证架构.md": "7.1-formal-verification-architecture.md",
            "7.2-工程实践案例.md": "7.2-engineering-practice-cases.md", 
            "7.x-其他实践主题.md": "7.x-other-practice-topics.md",
        }
        
        return mapping.get(chinese_filename, "")
    
    def scan_all_files(self) -> List[ContentMetrics]:
        """Scan all markdown files in the project"""
        all_metrics = []
        
        for chinese_dir in self.chinese_dirs:
            dir_path = self.base_dir / chinese_dir
            if dir_path.exists():
                for md_file in dir_path.rglob("*.md"):
                    metrics = self.analyze_file_content(md_file)
                    all_metrics.append(metrics)
        
        return all_metrics
    
    def generate_project_status(self) -> ProjectStatus:
        """Generate overall project status report"""
        all_metrics = self.scan_all_files()
        
        total_files = len(all_metrics)
        english_mirrors = sum(1 for m in all_metrics if m.has_english_mirror)
        missing_mirrors = [m.file_path for m in all_metrics if not m.has_english_mirror]
        
        # Quality thresholds
        completed_files = sum(1 for m in all_metrics if m.quality_score >= 50)
        low_quality_files = [m.file_path for m in all_metrics if m.quality_score < 30]
        
        overall_completion = (completed_files / total_files * 100) if total_files > 0 else 0
        
        return ProjectStatus(
            total_files=total_files,
            completed_files=completed_files,
            english_mirrors=english_mirrors,
            missing_mirrors=missing_mirrors,
            low_quality_files=low_quality_files,
            broken_links=[],  # TODO: Implement link checking
            overall_completion=overall_completion
        )
    
    def print_detailed_report(self):
        """Print detailed project analysis report"""
        print("=" * 80)
        print("LEAN FORMAL KNOWLEDGE SYSTEM - PROJECT COMPLETENESS REPORT")
        print("=" * 80)
        
        status = self.generate_project_status()
        all_metrics = self.scan_all_files()
        
        # Overall statistics
        print(f"\n📊 OVERALL STATISTICS")
        print(f"Total files analyzed: {status.total_files}")
        print(f"High-quality files (≥50 points): {status.completed_files}")
        print(f"English mirrors: {status.english_mirrors}")
        print(f"Overall completion: {status.overall_completion:.1f}%")
        
        # Quality distribution
        quality_ranges = {"Excellent (≥80)": 0, "Good (60-79)": 0, "Fair (30-59)": 0, "Poor (<30)": 0}
        for metrics in all_metrics:
            score = metrics.quality_score
            if score >= 80:
                quality_ranges["Excellent (≥80)"] += 1
            elif score >= 60:
                quality_ranges["Good (60-79)"] += 1
            elif score >= 30:
                quality_ranges["Fair (30-59)"] += 1
            else:
                quality_ranges["Poor (<30)"] += 1
        
        print(f"\n📈 QUALITY DISTRIBUTION")
        for range_name, count in quality_ranges.items():
            percentage = (count / status.total_files * 100) if status.total_files > 0 else 0
            print(f"{range_name}: {count} files ({percentage:.1f}%)")
        
        # Top quality files
        top_files = sorted(all_metrics, key=lambda x: x.quality_score, reverse=True)[:10]
        print(f"\n🏆 TOP QUALITY FILES")
        for i, metrics in enumerate(top_files, 1):
            filename = Path(metrics.file_path).name
            print(f"{i:2d}. {filename} (Score: {metrics.quality_score:.1f})")
        
        # Missing English mirrors
        if status.missing_mirrors:
            print(f"\n🔍 MISSING ENGLISH MIRRORS ({len(status.missing_mirrors)} files)")
            for missing in status.missing_mirrors[:10]:  # Show first 10
                filename = Path(missing).name
                print(f"   • {filename}")
            if len(status.missing_mirrors) > 10:
                print(f"   ... and {len(status.missing_mirrors) - 10} more")
        
        # Low quality files needing attention
        if status.low_quality_files:
            print(f"\n⚠️  LOW QUALITY FILES NEEDING ATTENTION ({len(status.low_quality_files)} files)")
            for low_quality in status.low_quality_files[:5]:  # Show first 5
                filename = Path(low_quality).name
                quality = next(m.quality_score for m in all_metrics if m.file_path == low_quality)
                print(f"   • {filename} (Score: {quality:.1f})")
        
        # Content statistics
        total_lines = sum(m.line_count for m in all_metrics)
        total_words = sum(m.word_count for m in all_metrics)
        total_code = sum(m.code_blocks for m in all_metrics)
        total_formulas = sum(m.formulas for m in all_metrics)
        total_diagrams = sum(m.diagrams for m in all_metrics)
        
        print(f"\n📝 CONTENT STATISTICS")
        print(f"Total lines of content: {total_lines:,}")
        print(f"Total words: {total_words:,}")
        print(f"Code blocks: {total_code}")
        print(f"Mathematical formulas: {total_formulas}")
        print(f"Diagrams: {total_diagrams}")
        
        # Recommendations
        print(f"\n💡 RECOMMENDATIONS")
        if status.english_mirrors < status.total_files:
            missing_count = status.total_files - status.english_mirrors
            print(f"   • Create {missing_count} missing English mirrors")
        
        if status.low_quality_files:
            print(f"   • Enhance {len(status.low_quality_files)} low-quality files")
        
        if status.overall_completion < 80:
            print(f"   • Focus on improving content depth and examples")
        
        print(f"\n✅ PROJECT STATUS: {'EXCELLENT' if status.overall_completion >= 90 else 'GOOD' if status.overall_completion >= 70 else 'NEEDS IMPROVEMENT'}")
        print("=" * 80)

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Check Lean Formal Knowledge System completeness")
    parser.add_argument("--base-dir", default="analysis", help="Base directory to analyze")
    parser.add_argument("--summary", action="store_true", help="Show summary only")
    
    args = parser.parse_args()
    
    checker = CompletenessChecker(args.base_dir)
    
    if args.summary:
        status = checker.generate_project_status()
        print(f"Project Completion: {status.overall_completion:.1f}%")
        print(f"Files: {status.completed_files}/{status.total_files}")
        print(f"English Mirrors: {status.english_mirrors}/{status.total_files}")
    else:
        checker.print_detailed_report()

if __name__ == "__main__":
    main() 