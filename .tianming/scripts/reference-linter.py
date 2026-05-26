#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
天命 Skill 引用完整性 Lint 工具 (Python 版)

扫描 .tianming 规则目录下所有 .md 文件，检查：
- 所有 [REF:xxx] 是否能在 [ID:xxx] 中找到
- 所有 [KERNEL_REF:xxx] 是否能在 [ID:xxx] 中找到
- 所有 [VAR:xxx] 是否能在 constants/global-constants.md 中找到
- 是否存在不规范的带空格引用 [REF: xxx] / [VAR: xxx] / [KERNEL_REF: xxx]
- 原始提示词中的所有 [ID] 是否已迁移（可选）

用法:
    python reference-linter.py
    python reference-linter.py -SkillPath /path/to/.tianming
    python reference-linter.py --json > report.json
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

def get_all_text(path):
    per_file = {}
    for root, _, files in os.walk(path):
        for f in files:
            if f.endswith('.md'):
                full_path = Path(root) / f
                rel_path = str(full_path.relative_to(path))
                with open(full_path, 'r', encoding='utf-8') as file:
                    per_file[rel_path] = file.read()
    return per_file

def strip_code_regions(text):
    # Remove fenced code blocks
    text = re.sub(r'(?ms)^```.*?^```', '<<<CODEBLOCK>>>', text)
    # Remove inline code spans
    text = re.sub(r'`[^`\r\n]*`', '<<<INLINE>>>', text)
    return text

def extract_tokens(per_file, pattern, strip_code=False):
    items = []
    for file, text in per_file.items():
        if strip_code:
            text = strip_code_regions(text)
        lines = text.splitlines()
        for i, line in enumerate(lines):
            for m in re.finditer(pattern, line):
                raw = m.group(1).strip()
                # Support multiple targets like [KERNEL_REF:a, b]
                for x in raw.split(','):
                    v = x.strip()
                    if v:
                        items.append({'Token': v, 'File': file, 'Line': i + 1})
    return items

def write_section(title, color_code='\033[96m'):
    RESET = '\033[0m'
    print()
    print(f"{color_code}{'=' * 70}{RESET}")
    print(f"{color_code}  {title}{RESET}")
    print(f"{color_code}{'=' * 70}{RESET}")

def main():
    parser = argparse.ArgumentParser(description="天命 Skill · 引用完整性 Lint 报告")
    parser.add_argument('-SkillPath', type=str, default=str(Path(__file__).parent.parent),
                        help='Skill 根目录路径，默认为脚本所在目录的父目录')
    parser.add_argument('-OriginalPrompt', type=str, default='',
                        help='可选：原始提示词文件路径，用于"迁移完整性"反推校验')
    parser.add_argument('--json', '-Json', action='store_true',
                        help='输出 JSON 报告而非彩色控制台报告')
    
    args = parser.parse_args()
    
    skill_path = Path(args.SkillPath)
    if not skill_path.exists():
        print(f"Skill 路径不存在：{skill_path}", file=sys.stderr)
        sys.exit(2)
        
    per_file = get_all_text(skill_path)
    
    ids = extract_tokens(per_file, r'\[ID:\s*([^\]]+)\]', strip_code=True)
    refs = extract_tokens(per_file, r'\[REF:\s*([^\]]+)\]')
    krefs = extract_tokens(per_file, r'\[KERNEL_REF:\s*([^\]]+)\]')
    vars_refs = extract_tokens(per_file, r'\[VAR:\s*([^\]]+)\]')
    
    # VAR 定义来自 constants/global-constants.md
    var_def_set = set()
    constants_files = [f for f in per_file.keys() if 'global-constants.md' in f]
    if constants_files:
        constants_text = per_file[constants_files[0]]
        for m in re.finditer(r'`\[VAR:([^\]]+)\]`', constants_text):
            var_def_set.add(m.group(1).strip())
            
    id_set = {item['Token'] for item in ids}
    
    # 示例文档占位符
    placeholders = {'xxx', 'yyy', 'zzz', '...', '元标签:...', 'a, b', 'a', 'b'}
    
    def is_real_reference(item):
        return item['Token'] not in placeholders
        
    bad_refs = [i for i in refs if is_real_reference(i) and i['Token'] not in id_set]
    bad_krefs = [i for i in krefs if is_real_reference(i) and i['Token'] not in id_set]
    bad_vars = [i for i in vars_refs if is_real_reference(i) and i['Token'] not in var_def_set]
    
    bad_space_refs = extract_tokens(per_file, r'\[REF:\s+([^\]]+)\]')
    bad_space_krefs = extract_tokens(per_file, r'\[KERNEL_REF:\s+([^\]]+)\]')
    bad_space_vars = extract_tokens(per_file, r'\[VAR:\s+([^\]]+)\]')
    
    # 检查重复ID
    id_counts = {}
    id_locs = {}
    for item in ids:
        tok = item['Token']
        id_counts[tok] = id_counts.get(tok, 0) + 1
        loc = f"{item['File']}:{item['Line']}"
        if tok not in id_locs:
            id_locs[tok] = []
        id_locs[tok].append(loc)
        
    dup_ids = [{'Token': tok, 'Count': count, 'Files': '; '.join(id_locs[tok])} 
               for tok, count in id_counts.items() if count > 1]
               
    orig_missing = []
    if args.OriginalPrompt and Path(args.OriginalPrompt).exists():
        with open(args.OriginalPrompt, 'r', encoding='utf-8') as f:
            orig_text = f.read()
        orig_ids = {m.group(1).strip() for m in re.finditer(r'\[ID:\s*([^\]]+)\]', orig_text)}
        for oi in sorted(orig_ids):
            if oi not in placeholders and oi not in id_set:
                orig_missing.append(oi)
                
    total_issues = (len(bad_refs) + len(bad_krefs) + len(bad_vars) +
                    len(bad_space_refs) + len(bad_space_krefs) + len(bad_space_vars) +
                    len(dup_ids) + len(orig_missing))
                    
    if args.json:
        report = {
            "timestamp": datetime.now().isoformat(),
            "skill_path": str(skill_path),
            "stats": {
                "files": len(per_file),
                "ids": len(ids),
                "unique_ids": len(id_set),
                "refs": len(refs),
                "krefs": len(krefs),
                "vars": len(vars_refs),
                "var_defs": len(var_def_set)
            },
            "issues": {
                "unresolved_refs": bad_refs,
                "unresolved_krefs": bad_krefs,
                "unresolved_vars": bad_vars,
                "malformed_space_refs": bad_space_refs,
                "malformed_space_krefs": bad_space_krefs,
                "malformed_space_vars": bad_space_vars,
                "duplicate_ids": dup_ids,
                "missing_from_original": orig_missing
            },
            "total_issues": total_issues,
            "pass": total_issues == 0
        }
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        RED = '\033[91m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        GRAY = '\033[90m'
        RESET = '\033[0m'
        
        write_section("天命 Skill · 引用完整性 Lint 报告")
        print(f"{GRAY}Skill 路径 : {skill_path}{RESET}")
        print(f"{GRAY}扫描时间   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{RESET}")
        if args.OriginalPrompt:
            print(f"{GRAY}原始提示词 : {args.OriginalPrompt}{RESET}")
            
        write_section("统计", YELLOW)
        print(f"  文件总数      : {len(per_file)}")
        print(f"  [ID] 总数     : {len(ids)} (唯一 {len(id_set)})")
        print(f"  [REF] 引用    : {len(refs)}")
        print(f"  [KERNEL_REF]  : {len(krefs)}")
        print(f"  [VAR] 引用    : {len(vars_refs)}")
        print(f"  [VAR] 定义    : {len(var_def_set)}")
        
        write_section("问题检查", YELLOW)
        
        if bad_refs:
            print(f"{RED}  [✗] 悬空 [REF] : {len(bad_refs)} 处{RESET}")
            for b in bad_refs: print(f"{RED}      {b['File']}:{b['Line']}  →  [REF:{b['Token']}]{RESET}")
        else:
            print(f"{GREEN}  [✓] [REF]      : 全部能解析{RESET}")
            
        if bad_krefs:
            print(f"{RED}  [✗] 悬空 [KERNEL_REF] : {len(bad_krefs)} 处{RESET}")
            for b in bad_krefs: print(f"{RED}      {b['File']}:{b['Line']}  →  [KERNEL_REF:{b['Token']}]{RESET}")
        else:
            print(f"{GREEN}  [✓] [KERNEL_REF]: 全部能解析{RESET}")
            
        if bad_vars:
            print(f"{RED}  [✗] 悬空 [VAR] : {len(bad_vars)} 处{RESET}")
            for b in bad_vars: print(f"{RED}      {b['File']}:{b['Line']}  →  [VAR:{b['Token']}]{RESET}")
        else:
            print(f"{GREEN}  [✓] [VAR]      : 全部能解析{RESET}")
            
        space_count = len(bad_space_refs) + len(bad_space_krefs) + len(bad_space_vars)
        if space_count > 0:
            print(f"{RED}  [✗] 带空格不规范引用 : {space_count} 处{RESET}")
            for b in bad_space_refs: print(f"{RED}      {b['File']}:{b['Line']}  →  [REF: {b['Token']}]{RESET}")
            for b in bad_space_krefs: print(f"{RED}      {b['File']}:{b['Line']}  →  [KERNEL_REF: {b['Token']}]{RESET}")
            for b in bad_space_vars: print(f"{RED}      {b['File']}:{b['Line']}  →  [VAR: {b['Token']}]{RESET}")
        else:
            print(f"{GREEN}  [✓] 引用格式    : 全部符合规范（冒号后无空格）{RESET}")
            
        if dup_ids:
            print(f"{YELLOW}  [!] 重复 [ID] 定义 : {len(dup_ids)} 个{RESET}")
            print(f"{GRAY}      （注意：天命系统允许同一文件中放总入口+子协议双 ID，可能为合理重复）{RESET}")
            for d in dup_ids:
                print(f"{YELLOW}      [ID:{d['Token']}] 出现 {d['Count']} 次{RESET}")
                print(f"{GRAY}         位置: {d['Files']}{RESET}")
        else:
            print(f"{GREEN}  [✓] [ID] 唯一性 : 无重复定义{RESET}")
            
        if args.OriginalPrompt:
            if orig_missing:
                print(f"{RED}  [✗] 原始提示词迁移缺失 : {len(orig_missing)} 个 ID{RESET}")
                for m in orig_missing: print(f"{RED}      [ID:{m}] 未在 Skill 中定义{RESET}")
            else:
                print(f"{GREEN}  [✓] 原始迁移   : 原始所有 [ID] 已全部迁移{RESET}")
                
        color = GREEN if total_issues == 0 and len(dup_ids) == 0 else RED
        write_section("总结", color)
        if total_issues == 0 and len(dup_ids) == 0:
            print(f"{GREEN}  ✓ 所有引用完整性检查通过{RESET}")
        elif total_issues == 0:
            print(f"{GREEN}  ✓ 引用完整性通过（仅 {len(dup_ids)} 个重复 ID 为合理设计）{RESET}")
        else:
            print(f"{RED}  ✗ 发现 {total_issues} 个问题，请检查上方明细{RESET}")
        print()
        
    hard_issues = (len(bad_refs) + len(bad_krefs) + len(bad_vars) +
                   len(bad_space_refs) + len(bad_space_krefs) + len(bad_space_vars) +
                   len(orig_missing))
                   
    sys.exit(1 if hard_issues > 0 else 0)

if __name__ == "__main__":
    main()
