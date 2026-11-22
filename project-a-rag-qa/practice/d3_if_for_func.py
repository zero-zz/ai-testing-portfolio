"""D3 主块①练习：for + enumerate / if-elif / 函数默认参数

用法（在仓库根目录）：
    .venv/Scripts/python project-a-rag-qa/practice/d3_if_for_func.py
    全部通过会打印：D3 主块①练习：全部通过

规则（沿用 D2 方法）：
    1. 不许打开同目录的 d3_answer_reference.py
    2. 卡住超过 3 分钟再瞄一眼，看完立刻合上，凭理解自己写
    3. 自检区代码不许改——它就是你的"测试用例"

三个练习全部使用真实 cases.csv，练完顺手复习了 D2 的 load_cases()。
"""
import csv
from pathlib import Path

CASES_CSV = Path(__file__).parent.parent / "test_data" / "cases.csv"


def load_cases():
    """D2 已写过：读 CSV 返回用例字典列表（这次凭记忆再写一遍）"""
    # TODO: 补全（提示：utf-8-sig、csv.DictReader）


# ========== 练习 1：for + enumerate ==========
def make_numbered_ids(cases):
    """给用例编号，返回 ['1. TC001', '2. TC002', ...]（编号从 1 开始）

    提示：enumerate 的第二个参数 start 控制起始编号
    """
    result = []
    # TODO: 用 for + enumerate 补全
    return result


# ========== 练习 2：if / elif / else ==========
def risk_to_priority(risk):
    """风险分级：'低'->'P3'，'中'->'P2'，'高'->'P1'，其他任何值->'P0'

    提示：P0 表示非法值，这是"负向用例"思想——测试函数本身要能接住脏数据
    """
    # TODO: if / elif / else 补全


# ========== 练习 3：函数默认参数 ==========
def filter_cases(cases, tag=...):
    """按 tag 筛选用例；调用方不传 tag 时，默认筛 '正常问答'

    提示：默认参数写在函数签名里；`...` 是占位符，改成正确的默认值
    """
    # TODO: 补全（遍历 + if + append）


# ========== 自检区（不要改） ==========
if __name__ == "__main__":
    cases = load_cases()

    # 练习 1 自检
    numbered = make_numbered_ids(cases)
    assert isinstance(numbered, list), "练习1：应返回列表"
    assert len(numbered) == len(cases) == 21, f"练习1：长度应 21，实际 {len(numbered)}"
    assert numbered[0] == f"1. {cases[0]['id']}", f"练习1：首项错误 {numbered[0]!r}"
    assert numbered[-1] == f"{len(cases)}. {cases[-1]['id']}", f"练习1：末项错误 {numbered[-1]!r}"
    assert all("." in item for item in numbered), "练习1：格式应为 '编号. id'"

    # 练习 2 自检
    assert risk_to_priority("低") == "P3", "练习2：低 -> P3"
    assert risk_to_priority("中") == "P2", "练习2：中 -> P2"
    assert risk_to_priority("高") == "P1", "练习2：高 -> P1"
    assert risk_to_priority("很高") == "P0", "练习2：非法值应兜底为 P0"
    assert risk_to_priority("") == "P0", "练习2：空串应兜底为 P0"

    # 练习 3 自检
    normal = filter_cases(cases)
    assert len(normal) == 8, f"练习3：默认'正常问答'应 8 条，实际 {len(normal)}"
    assert all(c["tag"] == "正常问答" for c in normal), "练习3：筛出的 tag 应全为正常问答"
    assert len(filter_cases(cases, tag="安全/对抗")) == 3, "练习3：安全/对抗应 3 条"
    assert filter_cases(cases, tag="不存在的标签") == [], "练习3：无匹配应返回空列表"

    print("D3 主块①练习：全部通过")
