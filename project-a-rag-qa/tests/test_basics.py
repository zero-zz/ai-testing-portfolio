"""D1 最小脚手架：验证测试数据完整性 + 一个参数化pytest测试。

今天是第一天，这个文件只需要做到：pytest -q 能跑通、看懂参数化。
明天再逐步加 load_cases()、断言、接口调用。
"""
import csv
from pathlib import Path

import pytest

CASES_CSV = Path(__file__).parent.parent / "test_data" / "cases.csv"


def load_cases():
    """读取 CSV，返回用例字典列表。"""
    with CASES_CSV.open(encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def test_cases_file_exists():
    assert CASES_CSV.exists(), f"找不到测试数据文件: {CASES_CSV}"


def test_case_has_required_fields():
    """验证每条用例都有必备字段。"""
    cases = load_cases()
    assert len(cases) >= 5, "至少需要 5 条用例"
    for case in cases:
        for field in ("id", "input", "tag", "expected"):
            assert case.get(field), f"用例 {case.get('id', '?')} 缺少字段: {field}"


@pytest.mark.parametrize("case", load_cases(), ids=lambda c: c["id"])
def test_input_is_nonempty(case):
    """参数化：对每一条用例跑一次，验证 input 非空。"""
    assert case["input"].strip(), f"{case['id']} 的 input 为空"
