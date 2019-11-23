import json

def get_json_file(json_file_path):
    with open(json_file_path) as json_file:
        data =json.load(json_file)
    return data

def write_line_to_file(input_path, input_str):
    with open(input_path, "w") as file:
        file.write(input_str)

###################################################
file_path = input("pls enter your path\n   >>> ")

data = get_json_file(file_path)

# print(data['Melanie Bouroche'])
# print("---------------------------------")
# print(data['Gregor Goessler'])
# print("---------------------------------")
# print(data['Marius Bozga'])
# print("---------------------------------")
# print(data['Sanjay Kumar Madria'])
# print("---------------------------------")
# print(data['Santhosh Muthyapu'])
# print("---------------------------------")
# print(data['Yadu Kishore K'])


author_names = list(data)[:200]

for an in author_names:
    value = data[an]
    years = list(value)
    years.remove("years")
    for y in years:
        # print(y)
        info = value[y]
        print(info["keywords"])
        print("\n\n")


#print(len(author_names))
# authrs_set = set(author_names)
#print(len(authrs_set))

# author_ids = dict()
# counter = 10000000
# for author in author_names:
#     author_ids[author] = counter
#     counter+=1
# print(author_ids)
#
# final = json.dumps(author_ids)
# write_line_to_file("D:/Research/AuthorsKeywords/AuthorsIds.json", final)
