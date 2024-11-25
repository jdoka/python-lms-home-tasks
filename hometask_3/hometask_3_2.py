def trim_and_repeat(string="", offset=0, repetitions=1):
    return string[offset:] * repetitions


print(trim_and_repeat("dfg", 1, 5))  # fgfgfgfgfg
print(trim_and_repeat("dfg", 2, 3))  # ggg
print(trim_and_repeat("dfg", 3, 3))  # ""
print(trim_and_repeat("dfg", 1))  # fg
print(trim_and_repeat(string="dfg", repetitions=3))  # dfgdfgdfg
print(trim_and_repeat("dfg"))  # dfg
print(trim_and_repeat(""))  # ""
print(trim_and_repeat())  # ""
