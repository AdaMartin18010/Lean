#!/usr/bin/env python3
"""
Link validation tool for Lean Formal Knowledge System
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple
from urllib.parse import urlparse

class LinkValidator:
    def __init__(self, base_dir: str = "analysis"):
        self.base_dir = Path(base_dir)
        self.broken_links = []
        self.valid_links = []
        
    def extract_links_from_markdown(self, file_path: Path) -> List[Tuple[str, str]]:
        """Extract all links from markdown file"""
        links = []
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # Match markdown links: [text](url)
            link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
            matches = re.findall(link_pattern, content)
            
            for text, url in matches:
                links.append((text, url))
                
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            
        return links
    
    def validate_link(self, link_url: str, source_file: Path) -> bool:
        """Validate if a link is valid"""
        # Skip external URLs
        if link_url.startswith(('http://', 'https://', 'mailto:')):
            return True
            
        # Handle anchor links
        if link_url.startswith('#'):
            return True
            
        # Handle relative paths
        if link_url.startswith('./') or link_url.startswith('../'):
            target_path = source_file.parent / link_url
        else:
            target_path = source_file.parent / link_url
            
        # Check if file exists
        if target_path.exists():
            return True
            
        # Check if it's an anchor in the same file
        if '#' in link_url:
            file_part, anchor = link_url.split('#', 1)
            if not file_part:  # Same file anchor
                return True
            else:
                target_file = source_file.parent / file_part
                if target_file.exists():
                    return True
                    
        return False
    
    def validate_file(self, file_path: Path) -> Dict[str, List]:
        """Validate all links in a single file"""
        results = {
            'valid': [],
            'broken': [],
            'external': []
        }
        
        links = self.extract_links_from_markdown(file_path)
        
        for text, url in links:
            if url.startswith(('http://', 'https://')):
                results['external'].append((text, url))
            elif self.validate_link(url, file_path):
                results['valid'].append((text, url))
            else:
                results['broken'].append((text, url))
                
        return results
    
    def validate_all_files(self) -> Dict[str, List]:
        """Validate all markdown files in the directory"""
        all_results = {
            'valid': [],
            'broken': [],
            'external': [],
            'files_checked': 0
        }
        
        for md_file in self.base_dir.rglob('*.md'):
            all_results['files_checked'] += 1
            file_results = self.validate_file(md_file)
            
            for category in ['valid', 'broken', 'external']:
                all_results[category].extend([
                    (str(md_file.relative_to(self.base_dir)), text, url)
                    for text, url in file_results[category]
                ])
                
        return all_results
    
    def generate_report(self, results: Dict[str, List]) -> str:
        """Generate validation report"""
        report = []
        report.append("# Link Validation Report\n")
        
        report.append(f"## Summary")
        report.append(f"- Files checked: {results['files_checked']}")
        report.append(f"- Valid links: {len(results['valid'])}")
        report.append(f"- Broken links: {len(results['broken'])}")
        report.append(f"- External links: {len(results['external'])}\n")
        
        if results['broken']:
            report.append("## Broken Links\n")
            for file_path, text, url in results['broken']:
                report.append(f"- **{file_path}**: `{text}` -> `{url}`")
            report.append("")
            
        if results['external']:
            report.append("## External Links\n")
            for file_path, text, url in results['external']:
                report.append(f"- **{file_path}**: `{text}` -> `{url}`")
            report.append("")
            
        return "\n".join(report)

def main():
    """Main function"""
    validator = LinkValidator()
    
    print("Validating links...")
    results = validator.validate_all_files()
    
    report = validator.generate_report(results)
    
    # Save report
    report_path = validator.base_dir / "tools" / "link_validation_report.md"
    report_path.write_text(report, encoding='utf-8')
    
    print(report)
    print(f"\nReport saved to: {report_path}")
    
    if results['broken']:
        print(f"\n⚠️  Found {len(results['broken'])} broken links!")
        return 1
    else:
        print("\n✅ All links are valid!")
        return 0

if __name__ == "__main__":
    exit(main()) 