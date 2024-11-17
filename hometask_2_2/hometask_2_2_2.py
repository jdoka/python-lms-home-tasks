def print_query_statistic(queries):
    word_to_query_count = {}
    for query in queries:
        word_count = len(query.split(' '))
        query_count = word_to_query_count.get(word_count, 0)
        word_to_query_count[word_count] = query_count + 1
    result = {}
    for word_count in word_to_query_count.keys():
        result[word_count] = format((word_to_query_count[word_count] * 100 / len(queries)), '.2f') + '%'
    print(result)


queries1 = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

queries2 = []

print_query_statistic(queries1)
print_query_statistic(queries2)
