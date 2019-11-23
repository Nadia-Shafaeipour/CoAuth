import json

def get_json_file(json_file_path):
    with open(json_file_path) as json_file:
        data =json.load(json_file)
    return data

def write_line_to_file(input_path, input_str):
    with open(input_path, "w") as file:
        file.write(input_str)


file_path = input("pls enter your path\n   >>> ")
output_file_path = input("pls enter your output path\n   >>> ")

data = get_json_file(file_path)


ids=dict()
cntr = 10000000
for author in data:
    cntr+=1
    ids[author] = cntr

print(len(list(ids)))

write_line_to_file(output_file_path, json.dumps(ids))
