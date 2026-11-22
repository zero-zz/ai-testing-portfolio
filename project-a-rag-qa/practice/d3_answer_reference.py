"""D3 主块①参考答案——练习卡住超过 3 分钟再看，看完合上凭理解写

对应练习文件：d3_if_for_func.py
"""
import csv
from pathlib import Path

CASES_CSV = Path(__file__).parent.parent / "test_data" / "cases.csv"


def load_cases():
    with CASES_CSV.open(encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def make_numbered_ids(cases):
    result = []
    for index, case in enumerate(cases, start=1):
        result.append(f"{index}. {case['id']}")
    return result


def risk_to_priority(risk):
    if risk == "低":
        return "P3"
    elif risk == "中":
        return "P2"
    elif risk == "高":
        return "P1"
    else:
        return "P0"


def filter_cases(cases, tag="正常问答"):
    result = []
    for case in cases:
        if case["tag"] == tag:
            result.append(case)
    return result


if __name__ == "__main__":
    cases = load_cases()

    numbered = make_numbered_ids(cases)
    assert isinstance(numbered, list)
    assert len(numbered) == len(cases) == 21
    assert numbered[0] == f"1. {cases[0]['id']}"
    assert numbered[-1] == f"{len(cases)}. {cases[-1]['id']}"
    assert all("." in item for item in numbered)

    assert risk_to_priority("低") == "P3"
    assert risk_to_priority("中") == "P2"
    assert risk_to_priority("高") == "P1"
    assert risk_to_priority("很高") == "P0"
    assert risk_to_priority("") == "P0"

    normal = filter_cases(cases)
    assert len(normal) == 8
    assert all(c["tag"] == "正常问答" for c in normal)
    assert len(filter_cases(cases, tag="安全/对抗")) == 3
    assert filter_cases(cases, tag="不存在的标签") == []

    print("D3 主块①练习：全部通过")
