import json

user_to_category = {}
with open("purchase_log.txt") as file:
    for line in file:
        json_line = json.loads(line)
        user_to_category[json_line["user_id"]] = json_line["category"]
file.close()
user_to_category.pop("user_id")
for k in user_to_category:
    print(k + " " + user_to_category[k])
