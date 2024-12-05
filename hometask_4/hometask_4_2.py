import json


def get_user_to_category_dict():
    result = {}
    with open("purchase_log.txt") as file:
        for line in file:
            json_line = json.loads(line)
            result[json_line["user_id"]] = json_line["category"]
    file.close()
    return result


def write_result():
    source_file = open("visit_log.csv", "r")
    destination_file = open("funnel.csv", "w")
    user_to_category = get_user_to_category_dict()
    for line in source_file:
        user, source = line.split(",")
        if user_to_category.__contains__(user):
            pieces = [user, source[:-1], user_to_category[user]]
            destination_file.write(",".join(pieces) + "\n")
    source_file.close()
    destination_file.close()


write_result()
