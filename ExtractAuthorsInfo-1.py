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


url_name = "conf_url" # conf_url or article_url
jour_conf = "conf" #jour
jc_year = "conf_year" # conf_year or year
file_path = input("pls enter your path\n   >>> ")
key_file = "inspec_controlled_indexing" #inspec_non_controlled_indexing
# file_path = "data/"
# conf_name = input("pls enter your conf_name:  ")

from os import walk

f=list(walk(file_path))[0][2]
# for (dirpath, dirnames, filenames) in walk (file_path):
#     f.extend(filenames)
#     break

file_paths = []

for file_name in f:
    file_paths.append(file_path + "/" + file_name)

Articles=[]
for fp in file_paths:
    Articles.extend(get_json_file(fp))
    print("COMPLETED: {}".format(fp))

print(len(Articles))

checked_arts = set()

authors_dict = dict()
cntr = 0
lnArt = len(Articles)
for art in Articles:
    cntr += 1
    print("\r{}/{}".format(cntr,lnArt), end="")
    if art["{}".format(url_name)] in checked_arts:
        continue
    checked_arts.add(art["{}".format(url_name)])
    year = art["{}".format(jc_year)]
    if art.get("author_aff") == None:
        continue
    auth_aff = art["author_aff"]
    try:
        keywords = art["{}".format(key_file)]
    except Exception as e:
        keywords = []
    auths_name=list(set([ath["name"] for ath in art["author_aff"]]))
    auths_name = [an.strip() for an in auths_name]
    if "" in auths_name:
        auths_name.remove("")

    auths_len = len(auths_name)
    for an,i in zip(auths_name, range(auths_len, 0, -1)):
        if authors_dict.get(an) == None:
            authors_dict[an]={"years":[]}
        authors_dict[an]["years"].append(year)
        if authors_dict[an].get(str(year)) == None:
            authors_dict[an][str(year)] = {"keywords": [], "co_authors": [], "pscore": []}

        # if an == 'Ming-Hsuan Yang':
        #     print("-----------------------------------")
        #     print(art["conf_url"])
        #     print(year)
        #     print(keywords)

        authors_dict[an][str(year)]["keywords"].append(keywords)
        co_authors = list(auths_name)
        try:
            co_authors.remove(an)
        except Exception as e:
            print("-----------------")
            print(auths_name)
            print(co_authors)
            print("author_name: {}".format(an))
            print(e)
            print("-----------------")
            break

        authors_dict[an][str(year)]["co_authors"].append(co_authors)
        authors_dict[an][str(year)]["pscore"].append(i/auths_len)
    if an == 'Ming-Hsuan Yang':
        print("-----------------------------------")
        print(art["{}".format(url_name)])
        print(year)
        print(authors_dict[an][str(year)]["co_authors"])
final = json.dumps(authors_dict)
write_line_to_file("D:/Research/AuthorsKeywords/confAuthorsInfo.json", final)
# write_line_to_file("AuthorsInfo.json", final)









































#
