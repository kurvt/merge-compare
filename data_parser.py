"""
数据解析模块
"""
import re
from datetime import datetime
from difflib import SequenceMatcher


def parse_time(t: str) -> datetime:
    months = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,
               'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
    t = (t or '').strip()
    m = re.match(r'(\d+):(\d+)\s*(AM|PM)?', t, re.IGNORECASE)
    if m:
        h, mn = int(m.group(1)), int(m.group(2))
        ampm = (m.group(3) or '').upper()
        if ampm == 'PM' and h != 12: h += 12
        elif ampm == 'AM' and h == 12: h = 0
        return datetime(2026, 4, 9, h, mn)
    m2 = re.match(r'([A-Za-z]+)\s+(\d+)', t)
    if m2:
        mo = months.get(m2.group(1), 4)
        day = int(m2.group(2))
        return datetime(2025 if mo > 4 else 2026, mo, day)
    return datetime(2026, 1, 1)


def load_from_json(raw_list: list) -> list:
    """
    直接加载 HTML 提取的 JSON 格式数据。
    每条已包含 in_str 字段（True = 已在 STR 分支合入）。
    """
    result = []
    for item in raw_list:
        entry = {
            'idx':          f"bsp-{item.get('id', 0)}",
            'jira_no':      item.get('jira', ''),
            'subject':      item.get('subject', ''),
            'commit_type':  item.get('type', ''),
            'function':     item.get('function', ''),
            'repo':         item.get('repo', ''),
            'author':       item.get('owner', ''),
            'in_str':       bool(item.get('in_str', False)),
            'updated':      item.get('updated', ''),
            'size':         item.get('size', '--'),
            'branch':       'bsp_REL1_CSP1_20260219',
        }
        result.append(entry)
    return result


# ── 以下为管道格式解析（用于用户粘贴自定义数据） ──

def parse_entry(full_text: str) -> dict:
    jira_m = re.search(r'\[JiraNo\]\s*:\s*([^\s\[\]]+)', full_text, re.IGNORECASE)
    subj_m = re.search(r'\[Subject\]\s*:\s*(.*?)(?=\[Affects|\[Impact|\[Type\]|\[JiraNo\]|$)',
                       full_text, re.IGNORECASE)
    type_m = re.search(r'\[Type\]\s*:\s*(\w+)', full_text, re.IGNORECASE)
    return {
        'jira_no':     jira_m.group(1).strip() if jira_m else '',
        'subject':     subj_m.group(1).strip() if subj_m else full_text.strip(),
        'commit_type': type_m.group(1).strip() if type_m else '',
        'full_text':   full_text.strip(),
    }


def parse_pipe_text(raw: str) -> list:
    """解析管道分隔的文本（Subject 内可能含 |）"""
    entries = []
    for line in raw.strip().splitlines():
        line = line.strip()
        if not line or len(line) < 10 or '|' not in line:
            continue
        all_parts = [p.strip() for p in line.split('|')]
        branch_idx = next((i for i, p in enumerate(all_parts) if p.startswith('bsp_')), None)
        if branch_idx is None or branch_idx < 3:
            continue
        full_text  = '|'.join(all_parts[:branch_idx - 3])
        parsed     = parse_entry(full_text)
        author     = all_parts[branch_idx - 3]
        parsed.update({
            'author':    author,
            'reviewers': all_parts[branch_idx - 2],
            'repo':      all_parts[branch_idx - 1],
            'branch':    all_parts[branch_idx],
            'time_str':  all_parts[branch_idx + 1] if branch_idx + 1 < len(all_parts) else '',
            'size':      all_parts[branch_idx + 2] if branch_idx + 2 < len(all_parts) else '--',
            'status':    all_parts[branch_idx + 3] if branch_idx + 3 < len(all_parts) else 'Merged',
            'in_str':    False,
        })
        parsed['time_dt'] = parse_time(parsed['time_str'])
        # 仍需相似度匹配
        entries.append(parsed)
    return entries
