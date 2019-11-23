import pandas as pd
import json
import collections

################################################

def get_json_file(json_file_path):
    with open(json_file_path) as json_file:
        data =json.load(json_file)
    return data


def write_line_to_file(input_path, input_str):
    with open(input_path, "w") as file:
        file.write(input_str)

################################################


authors_info_file_path = input("plz enter authors info file path >>> ")
community_info_file_path = input("plz enter community info file path >>> ")
author_focusness_path = input("plz enter your focusness info file path >>>")


df = pd.read_csv(community_info_file_path)

comm_dict = dict()

for i in range(len(df)):
    comm_dict[df.iloc[i]["label"]] = df.iloc[i]["modularity_class"]
# print(comm_dict)
# print(comm_dict.get("markov processes"))
# exit()

authors_inf = get_json_file(authors_info_file_path)

author_name_for_test = "Zhang Jie" # Fumiyuki Adachi |  Faisal Kaleem | Fumiyuki Adachi | Zhang Jie

focusness_authors = dict()
cntr=0
lnauth=len(authors_inf)
for author in authors_inf:
    cntr+=1
    print("\r{}/{}".format(cntr,lnauth), end="")
    years = set(authors_inf[author]["years"])

    # years = list(range(2010, 2018))

    # years = list(authors_inf[author])
    # years.remove("years")
    # print(type(list(years)[0]))
    # exit()
    if focusness_authors.get(author) == None:
        focusness_authors[author] = dict()
    for year in years:
        year = "{}".format(year)
        test_var = 0
        for step in range(1,11):
            comm_list = list()
            focusness_year = dict()
            step_list = list(range(int(year), int(year)-step, -1))
            keywords = []
            for year_step in step_list:
                if authors_inf[author].get(str(year_step)) == None or authors_inf[author].get(str(year_step)).get("keywords") == None:
                    continue
                keywords.extend(authors_inf[author][str(year_step)]["keywords"])
            # if author == author_name_for_test:
            #     print("year: {} | step: {} | keywords: {}\n".format(year, step, keywords))
            for list_keyword in keywords:
                for keyword in list_keyword:
                    try:
                        comm_list.append(comm_dict[keyword.lower()])
                    except Exception as e:
                        pass
                        # raise
            # if author == author_name_for_test:
            #     print("year: {} | step: {} | keywords: {}\n".format(year, step, comm_list))
            if len(comm_list) > 0:
                # if author == author_name_for_test:
                #     print(comm_list)
                focusness = collections.Counter(comm_list).most_common(1)[0][1]/len(comm_list)
                # if step > 1:
                #     if test_var != focusness:
                #         print("Author Name: {} | year: {}, step: {}".format(author, year, step))
                #         exit()
                # test_var = focusness

                if focusness_authors.get(author).get(year) == None:
                    focusness_authors[author][year] = dict()
                # focusness_year[year] = focusness

                focusness_authors[author][year][step] = focusness

write_line_to_file(author_focusness_path, json.dumps(focusness_authors))












#
