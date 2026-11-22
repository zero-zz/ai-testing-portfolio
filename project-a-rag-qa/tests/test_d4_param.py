"""D4 练习：pytest 参数化 —— 把 21 条用例变成 21 个独立测试

为什么参数化：D2 的 test_case_risk_is_valid 是「一个测试里 for 循环 21 条」，
第一条失败后面全部跳过；参数化后每条用例是独立测试，TC003 挂了不影响 TC004。

核心知识点：
1. @pytest.mark.parametrize("参数名", 数据列表)：列表里有几条数据，
   测试函数就执行几次，每次把一条数据传给参数。
2. ids=[...]：给每条测试起名字，失败时直接显示 TC007 而不是 case17。

需要完成 4 件事（把 ____ 填上，先自己想，卡 3 分钟再看 practice/d4_answer_reference.py）：
1. 从同目录的 D2 模块导入 load_cases（好代码不复制，直接复用）
2. 模块级加载全部用例
3. 补全 parametrize 装饰器：参数名 "case"，数据 ALL_CASES，ids 用每条的 id 字段
4. 断言 input / expected / risk 三个字段非空，失败消息带用例 id 和字段名

写完运行：python -m pytest -q tests/test_d4_param.py
预期输出：21 passed（顺带确认 cases.csv 到底 20 还是 21 条）
"""
import pytest

from test_d2_practice import load_cases          # 1. 同目录的 D2 练习模块
ALL_CASES = load_cases()                  # 2. 模块级加载一次


@pytest.mark.parametrize("case",ALL_CASES,ids=[c.get("id","?")for c in ALL_CASES])   # 3. "case" + 数据 + ids
def test_case_fields_not_empty(case):
    for field in ("input", "expected", "risk"):
        assert case.get(field,"").strip(), f"用例{case.get('id','?')}的{field}字段为空"        # 4. 断言非空，消息带 id 和字段名