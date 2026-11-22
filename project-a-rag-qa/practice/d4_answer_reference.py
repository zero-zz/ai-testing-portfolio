"""D4 参考答案：卡住 3 分钟以上再看，看完立刻合上，凭理解自己写。

验证方式（在 project-a-rag-qa 目录下）：
  ../.venv/Scripts/python.exe -m pytest practice/d4_answer_reference.py -q -o python_files=d4_answer_reference.py
注意：本文件在 practice/ 下，import 不到隔壁 tests/ 的模块，
     需要手动把 tests/ 加进 sys.path（tests/test_d4_param.py 里不需要这步，
     pytest 收集测试时会把 tests/ 自动加进 sys.path）。
"""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "tests"))

from test_d2_practice import load_cases

ALL_CASES = load_cases()


@pytest.mark.parametrize(
    "case",
    ALL_CASES,
    ids=[c.get("id", "?") for c in ALL_CASES],
)
def test_case_fields_not_empty(case):
    for field in ("input", "expected", "risk"):
        value = case.get(field, "")
        assert value and value.strip(), (
            f"用例 {case.get('id', '?')} 的 {field} 字段为空"
        )
