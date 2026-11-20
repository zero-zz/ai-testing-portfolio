"""D2 重写练习：凭记忆独立完成

目标：让 `python -m pytest -q` 全绿。
规则：不要打开 reference/d2_answer_reference.txt；
      卡住超过 3 分钟再瞄一眼，看完立刻合上，凭理解自己写。

需要完成 5 件事：
1. 导入 csv 模块、从 pathlib 导入 Path
2. 定义 CASES_CSV，指向 test_data/cases.csv（从当前文件出发向上两级）
3. 定义 VALID_RISKS，合法风险值的集合（想清楚 CSV 里是中文还是英文）
4. load_cases()：读取 CSV，返回用例字典列表
5. test_case_risk_is_valid()：校验每条用例的 risk 在合法集合内，
   失败消息要带用例 id 和非法值

写完运行：python -m pytest -q
"""
import csv
from pathlib import Path
import pytest
CASE_CSV=Path(__file__).parent.parent/ "test_data" /"cases.csv"
VALID_RISKS={"低","中","高"}

def load_cases():
    with CASE_CSV.open(encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def test_case_risk_is_valid():
    cases=load_cases()
    for case in cases:
        risk = case.get("risk")
        assert risk in VALID_RISKS, f"用例 {case.get('id', '?')} 的 risk 非法: {risk}"


