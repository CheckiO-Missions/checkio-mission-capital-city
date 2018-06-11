init_code = """
if not "Capital" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Capital'?")

Capital = USER_GLOBAL['Capital']
"""

run_test = """
RET['code_result'] = {}
"""

def prepare_test(test="", answer=None, middle_code="", show_code=None):
    if show_code is None:
        show_code = middle_code + "\n" + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}


TESTS = {
    "Ukraine": [
        prepare_test(middle_code='''capital_1 = Capital('Kyiv')
capital_2 = Capital('London')
capital_3 = Capital('Dubai')''',
                     test="capital_3.name()",
                     answer="Kyiv")],
    "Russia": [
        prepare_test(middle_code='''capital_1 = Capital('Moscow')
capital_2 = Capital('Warsaw')
capital_3 = Capital('Paris')''',
                     test="capital_3.name()",
                     answer="Moscow")],
    "France": [
        prepare_test(middle_code='''capital_1 = Capital('Paris')
capital_2 = Capital('Sydney')''',
                     test="capital_2.name()",
                     answer="Paris")],
    "Japan": [
        prepare_test(middle_code='''capital_1 = Capital('Tokyo')
capital_2 = Capital('New-York')
capital_3 = Capital('Lviv')''',
                     test="capital_3.name()",
                     answer="Tokyo")],
    "USA": [
        prepare_test(middle_code='''capital_1 = Capital('Washington')
capital_2 = Capital('Orlando')
capital_3 = Capital('Denver')''',
                     test="capital_3.name()",
                     answer="Washington")
    ]

}
