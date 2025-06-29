import os
import re
from pathlib import Path

ANALYSIS_ROOT = Path(__file__).parent.parent

# 检查章节编号和标题层级
section_pattern = re.compile(r'^(#+)\s*(\d+(?:\.\d+)*)([\u4e00-\u9fa5\w\-\s]*)')

# 检查 LaTeX 公式
latex_inline = re.compile(r'\$(?!\$)(.+?)(?<!\$)\$')
latex_block = re.compile(r'\\\[(.*?)\\\]', re.DOTALL)
latex_fence = re.compile(r'```latex[\s\S]*?```', re.MULTILINE)

# 检查代码块
code_fence = re.compile(r'```(\w+)?[\s\S]*?```', re.MULTILINE)

# 检查交叉引用
anchor_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

# 检查中英文文件同步

def find_md_files(root):
    return [p for p in root.rglob('*.md') if not p.name.startswith('README')]

def check_sections(content):
    return section_pattern.findall(content)

def check_latex(content):
    return latex_inline.findall(content), latex_block.findall(content), latex_fence.findall(content)

def check_code_blocks(content):
    return code_fence.findall(content)

def check_anchors(content):
    return anchor_pattern.findall(content)

def check_bilingual(md_files):
    pairs = {}
    for p in md_files:
        rel = p.relative_to(ANALYSIS_ROOT)
        if any('form' in s or 'theory' in s for s in rel.parts):
            # 英文
            mirror = ANALYSIS_ROOT / str(rel).replace('form', '形式').replace('theory', '理论').replace('-', '')
        elif any('形式' in s or '理论' in s for s in rel.parts):
            # 中文
            mirror = ANALYSIS_ROOT / str(rel).replace('形式', 'form').replace('理论', 'theory')
        else:
            continue
        pairs[p] = mirror if mirror.exists() else None
    return pairs

def main():
    md_files = find_md_files(ANALYSIS_ROOT)
    print(f"Found {len(md_files)} markdown files.")
    for md in md_files:
        print(f"\n---\nAnalyzing: {md.relative_to(ANALYSIS_ROOT)}")
        content = md.read_text(encoding='utf-8')
        sections = check_sections(content)
        print(f"Section headings: {sections}")
        latex_inline, latex_block, latex_fence = check_latex(content)
        print(f"Inline LaTeX: {len(latex_inline)}, Block LaTeX: {len(latex_block)}, Fenced LaTeX: {len(latex_fence)}")
        code_blocks = check_code_blocks(content)
        print(f"Code blocks: {len(code_blocks)}")
        anchors = check_anchors(content)
        print(f"Anchors/Links: {len(anchors)}")
    # 检查中英文同步
    bilingual = check_bilingual(md_files)
    for k, v in bilingual.items():
        if v is None:
            print(f"No bilingual mirror for: {k.relative_to(ANALYSIS_ROOT)}")

if __name__ == '__main__':
    main() 