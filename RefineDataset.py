import json
# def get_file_lines(file_path):
#     lines = []
#     with open(file_path,"r") as file:
#         lines = file.readlines()
#     return lines
def get_json_file(json_file_path):
    with open(json_file_path) as json_file:
        data =json.load(json_file)
    return data

def write_line_to_file(input_path, input_str):
    with open(input_path, "w") as file:
        file.write(input_str)

pub_name = "conf_name" #"jour_name"

jour_conf = "conf" #"jour"


file_path = input("pls enter your path\n   >>> ").replace("\"","")
file_output_path = input("plz enter your output path >>")
# conf_name = input("pls enter your conf_name:  ")

from os import walk

f = list(walk(file_path))[0][2]
# for (dirpath, dirnames, filenames) in walk (file_path):
#     f.extend(filenames)
#     break

file_paths = []

for file_name in f:
    file_paths.append(file_path + "/" + file_name)

Articles=[]
for fp in file_paths:
    Articles.extend(get_json_file(fp))

print(len(Articles))


# Extract Journals names
jour_names = set()
cntr=0
lnart=len(Articles)
for article in Articles:
    cntr += 1
    print("\r{}/{}".format(cntr,lnart), end="")
    jour_names.add(article[pub_name])


write_line_to_file("D:\\{}_names.txt".format(jour_conf), str(jour_names))

exit()
conf_names = set()
with open("d:/Research/{}_names.txt".format(jour_conf)) as json_file:
    data = json.load(json_file).get("{}_names".format(jour_conf))
    conf_names = set(data)
    print(*data, sep="\n")



confs = dict()
for key in list(conf_names):
    confs[key] = []

cntr=0
lnart=len(Articles)
for art in Articles:
    cntr += 1
    print("\r{}/{}".format(cntr,lnart), end="")
    confs[art.get("{}_name".format(jour_conf))].append(art)

for conf in confs:
    try:
        write_line_to_file("{}/{}.txt".format(file_output_path, conf.replace("/","-")), json.dumps(list(confs.get(conf))))
    except Exception as e:
        print(conf)
        raise







## Extract conference names
# for article in Articles:
#     conf_names.add(article["conf_name"])
#
# write_line_to_file("D:\\conf_names.txt", str(conf_names))









# lines = get_file_lines(file_path)
# count = 0
# for line in lines:
#     if conf_name.lower() in lines.lower():
#         count += 1
#
# print(lines[count:])
