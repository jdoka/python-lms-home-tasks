def print_middle(word: str):
    l: int = len(word)
    from_in = int((l - 1) / 2)
    to_exc = from_in + 2 - (l % 2)
    print(word[from_in:to_exc])


print_middle("test")  # es
print_middle("testing")  # t
print_middle("t")  # t
print_middle("et")  # et
print_middle("")  #
