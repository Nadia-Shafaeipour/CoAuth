import json


def get_json_file(json_file_path):
    with open(json_file_path) as json_file:
        data=json.load(json_file)
    return(data)


def write_line_to_file(input_path, input_str):
    with open(input_path, "w") as file:
        file.write(input_str)


jour_path = input("plz enter your journal path>>> ")
conf_path = input("plz enter your conferance path>>> ")
author_polarity_path = input("plz enter your author pilarity path>>> ")


author_inf_jour = get_json_file(jour_path)
author_inf_conf = get_json_file(conf_path)


authors_name = list(author_inf_jour)
authors_name.extend(list(author_inf_conf))


polarity = dict()

cntr=0
conf_len = 0
auth_len=len(authors_name)
for author in authors_name:
    cntr+=1
    print("\r{}/{}".format(cntr,auth_len), end="")

    jour_years = author_inf_jour[author]["years"]
    conf_years = author_inf_conf[author]["years"]

    for step in range(1,11):
        for conf_year in conf_years:
            step_list = list(range(int(conf_year), int(conf_year)-step, -1))
            if author_inf_conf.get(author) == None:
                polarity[author][year] = 1
            else:
                conf_len = len(author_inf_conf[author]["years"])
                # print(conf_len)
        for jour_year in jour_years:
            step_list = list(range(int(jour_year), int(jour_year)-step, -1))
            if author_inf_jour.get(author) == None:
                polarity[author][year] = 0
            else:
                jour_len = len(author_inf_jour[author]["years"])
        polarity[author][year][step] = jour_len/(conf_len+jour_len)


write_line_to_file(author_polarity_path, json.dumps(polarity))
