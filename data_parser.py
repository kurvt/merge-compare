"""
数据解析模块 - 解析 BSP/STR 合入记录
"""

import re
from datetime import datetime
from difflib import SequenceMatcher
from typing import Optional


def parse_entry(full_text: str) -> dict:
    """从原始文本行中提取结构化字段"""
    # JiraNo
    jira_match = re.search(r'\[JiraNo\]\s*:\s*([^\s\[\]]+)', full_text, re.IGNORECASE)
    jira_no = jira_match.group(1).strip() if jira_match else ''

    # Subject：取到下一个[...] 标签或行尾
    subject_match = re.search(
        r'\[Subject\]\s*:\s*(.*?)(?=\[Affects|\[Impact|\[Type\]|\[JiraNo\]|$)',
        full_text, re.IGNORECASE
    )
    subject = subject_match.group(1).strip() if subject_match else full_text.strip()

    # Type
    type_match = re.search(r'\[Type\]\s*:\s*(\w+)', full_text, re.IGNORECASE)
    commit_type = type_match.group(1).strip() if type_match else ''

    return {
        'jira_no': jira_no,
        'subject': subject,
        'commit_type': commit_type,
        'full_text': full_text.strip(),
    }


def parse_time(t: str) -> datetime:
    """将时间字符串转换为 datetime，用于排序"""
    months = {
        'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
        'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
    }
    t = (t or '').strip()

    # "11:39 AM" or "2:16 PM" → today (Apr 9 2026)
    m = re.match(r'(\d+):(\d+)\s*(AM|PM)?', t, re.IGNORECASE)
    if m:
        h, mn = int(m.group(1)), int(m.group(2))
        ampm = (m.group(3) or '').upper()
        if ampm == 'PM' and h != 12:
            h += 12
        elif ampm == 'AM' and h == 12:
            h = 0
        return datetime(2026, 4, 9, h, mn)

    # "Apr 08" / "Mar 30"
    m2 = re.match(r'([A-Za-z]+)\s+(\d+)', t)
    if m2:
        mo = months.get(m2.group(1), 4)
        day = int(m2.group(2))
        year = 2025 if mo > 4 else 2026
        return datetime(year, mo, day)

    return datetime(2026, 1, 1)


def parse_raw_text(raw: str) -> list:
    """
    解析粘贴的原始文本（从网页复制的格式）。
    支持两种格式：
      1. 管道分隔格式（pipe-separated，内置数据用）
      2. 原始多行粘贴格式（从Gerrit/Review页面复制）
    """
    entries = []

    for line in raw.strip().splitlines():
        line = line.strip()
        if not line or len(line) < 10:
            continue

        # 管道分隔格式
        if '|' in line:
            parts = [p.strip() for p in line.split('|')]
            if len(parts) < 6:
                continue
            full_text = parts[0]
            parsed = parse_entry(full_text)
            parsed.update({
                'author': parts[1] if len(parts) > 1 else '',
                'reviewers': parts[2] if len(parts) > 2 else '',
                'repo': parts[3] if len(parts) > 3 else '',
                'branch': parts[4] if len(parts) > 4 else '',
                'time_str': parts[5] if len(parts) > 5 else '',
                'size': parts[6] if len(parts) > 6 else '--',
                'status': parts[7] if len(parts) > 7 else 'Merged',
            })
            parsed['time_dt'] = parse_time(parsed['time_str'])
            entries.append(parsed)

    return entries


# ==================== 相似度匹配 ====================

def normalize(s: str) -> str:
    s = s.lower()
    s = re.sub(r'[|,.\!\?。，！？：:；;]', ' ', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()


def similarity_score(a: str, b: str) -> float:
    na, nb = normalize(a), normalize(b)
    if na == nb:
        return 1.0
    if na in nb or nb in na:
        return 0.88

    # Jaccard on words (len > 2)
    words_a = set(w for w in na.split() if len(w) > 2)
    words_b = set(w for w in nb.split() if len(w) > 2)
    if not words_a or not words_b:
        return 0.0
    shared = len(words_a & words_b)
    union = len(words_a | words_b)
    jaccard = shared / union

    # SequenceMatcher bonus
    seq = SequenceMatcher(None, na, nb).ratio()
    return jaccard * 0.6 + seq * 0.4


def find_best_match(item: dict, candidates: list) -> tuple:
    """返回 (最佳匹配项, 匹配级别, 得分)"""
    best_item, best_score = None, 0.0
    for c in candidates:
        score = similarity_score(item['subject'], c['subject'])
        # 同仓库加分
        if item.get('repo') and c.get('repo') and item['repo'] == c['repo']:
            score = min(1.0, score + 0.08)
        if score > best_score:
            best_score = score
            best_item = c

    if best_score >= 0.82:
        return best_item, 'exact', best_score
    elif best_score >= 0.42:
        return best_item, 'similar', best_score
    return None, 'none', 0.0


def enrich_with_matches(source: list, target: list, prefix: str) -> list:
    """为 source 中每条记录附加与 target 的匹配信息，并生成唯一 idx"""
    result = []
    for i, item in enumerate(source):
        matched, level, score = find_best_match(item, target)
        entry = dict(item)
        entry['idx'] = f'{prefix}-{i}'
        entry['match_level'] = level
        entry['match_score'] = round(score, 3)
        entry['matched_subject'] = matched['subject'] if matched else ''
        result.append(entry)
    return result
