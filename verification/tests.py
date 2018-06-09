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
    "Clients": [
        prepare_test(middle_code='''capital_1 = Capital('Kyiv')
capital_2 = Capital('London')
capital_3 = Capital('Dubai')''',
                     test="capital_3.name()",
                     answer="Kyiv")
    ]

}
