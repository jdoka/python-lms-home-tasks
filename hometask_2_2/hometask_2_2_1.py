def print_unique_values(id_to_geo_dict):
    result = set()
    for user_values in id_to_geo_dict.values():
        for user_value in user_values:
            result.add(user_value)
    print(result)


ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
ids1 = {}
print_unique_values(ids)
print_unique_values(ids1)
