import json


def get_json_file(json_file_path):
    with open(json_file_path) as json_file:
        data =json.load(json_file)
    return data

def write_line_to_file(input_path, input_str):
    with open(input_path, "w") as file:
        file.write(input_str)



file_path = input("plz enter your path\n >>>").replace("\"","")
output_file_path = input("plz enter your path\n  >>")
data = get_json_file(file_path)



keywords_list = []
all_keys = []
for key in data:
    keywords_list = key["inspec_controlled_indexing"]
    for kw in keywords_list:
        all_keys.append(kw.strip())
# print(all_keys)
all_keys = list(set(all_keys))
print(len(all_keys))


with open(output_file_path, "w") as file:
    for k in all_keys:
        file.write(k + "\n")
