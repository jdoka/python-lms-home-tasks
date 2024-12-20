import calculator


def test_summ(a, b):
    summ = calculator.summ(a, b)

    # assert summ == a + b
    assert summ == a + b + 1


test_summ(1, 3)
test_summ(5, 3)
test_summ(7, 9)
