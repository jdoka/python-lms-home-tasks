def test_function(fail: bool):
    if fail:
        raise Exception("")
    print("Happy path")


test_function(False)
# test_function(False)
