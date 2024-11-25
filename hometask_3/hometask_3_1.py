def sum_distance(from_inclusive, to_inclusive):
    if from_inclusive > to_inclusive:
        temp = from_inclusive
        from_inclusive = to_inclusive
        to_inclusive = temp
    count = 1 + to_inclusive - from_inclusive
    return (from_inclusive + to_inclusive) * count / 2


print(sum_distance(5, 7))  # 18
print(sum_distance(6, 7))  # 13
print(sum_distance(7, 5))  # 18
print(sum_distance(5, 5))  # 5
print(sum_distance(-5, -3))  # -12
print(sum_distance(-3, -5))  # -12
print(sum_distance(0, 0))  # 0
print(sum_distance(0, 1))  # 1
print(sum_distance(0, -1))  # -1
