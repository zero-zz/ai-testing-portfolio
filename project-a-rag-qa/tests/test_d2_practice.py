"""D2 练习：AAA 用例数据校验（订正版）

独立于 test_basics.py 重写 load_cases()，并新增 risk 字段合法性校验，
用于检验"不看参考也能写出数据加载 + 断言"的能力。

订正点对照（与首次填写版本相比）：
1. 删除遗留的 ______ 占位符（未定义变量会导致模块导入即 NameError）
2. 目录名 test_data 用下划线，不是空格
3. VALID_RISKS 的值必须与 cases.csv 中的中文取值一致
4. open() 的参数是 encoding，不是 encodeing
5. 遍历出来的单条是 case（字典），cases 是整个列表；取值用 case.get("risk")
"""

import csv
from pathlib import Path

CASES_CSV = Path(__file__).parent.parent / "test_data" / "cases.csv"
VALID_RISKS = {"低", "中", "高"}  # 值域来自 cases.csv 中 risk 列的真实取值


def load_cases():
    """读取 CSV，返回用例字典列表。"""
    with CASES_CSV.open(encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def test_case_risk_is_valid():
    """每条用例的 risk 字段只能是 低/中/高。"""
    cases = load_cases()
    for case in cases:
        risk = case.get("risk")
        assert risk in VALID_RISKS, f"用例 {case.get('id', '?')} 的 risk 非法: {risk}"
