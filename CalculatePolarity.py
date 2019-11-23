# the output format:
# {"authorName": {"2017": {"1": 0.6, "2": 0.55, ..... ,"18": 0.24}, "2014": {....}, ....}}
# Calculating Journal-Conference Polarity for each author
# polarity near to ONE means the author mostly contributed in JOURNAL articles and
# polarity near to ZERO means the author mostly contributed in CONFERENCE articles
import json


################################################

def get_json_file(json_file_path):
    with open(json_file_path) as json_file:
        data =json.load(json_file)
    return data


def write_line_to_file(input_path, input_str):
    with open(input_path, "w") as file:
        file.write(input_str)

################################################


authors_info_file_path_jour = input("Please enter the journal authors info file path >>> ").replace("\"", "")
authors_info_file_path_conf = input("Please enter the conferences authors info file path >>> ").replace("\"", "")
output_file_path = input("Please enter the output file path >>> ").replace("\"", "")

authors_info_jour = get_json_file(authors_info_file_path_jour)
authors_info_conf = get_json_file(authors_info_file_path_conf)

author_names = list(authors_info_jour) + list(authors_info_conf)
author_names = list(set(author_names))


cntr = 0
lnathr = len(author_names)
authors_polarity_info = dict()
for author in author_names:
    cntr += 1
    print("\r{}/{}".format(cntr, lnathr), end="")
    author_jour_years = []
    author_conf_years = []
    if authors_polarity_info.get(author) == None:
        authors_polarity_info[author] = dict()
    if authors_info_jour.get(author) != None:
        author_jour_years = authors_info_jour.get(author).get("years")
        author_jour_years = [int(year) for year in author_jour_years]
    if authors_info_conf.get(author) != None:
        author_conf_years = authors_info_conf.get(author).get("years")
        author_conf_years = [int(year) for year in author_conf_years]

    author_years = author_jour_years + author_conf_years

    # print("AuthorYears: {} | {}".format(type(author_years[0]), author_years[:10]))
    # exit()
    author_years = set(author_years)
    for year in author_years:
        # print("Year: {}".format(year))
        if authors_polarity_info.get(author).get(year) == None:
            authors_polarity_info[author][year] = dict()
        for step in range(1, year-2000+1): # Because we have only 18 steps [2000 to 2017]
            jour_count = 0
            conf_count = 0
            for yr in range(year, year - step, -1):
                jour_count += author_jour_years.count(yr)
                conf_count += author_conf_years.count(yr)
            authors_polarity_info[author][year]["{}".format(step)] = jour_count / (jour_count + conf_count)


write_line_to_file(output_file_path, json.dumps(authors_polarity_info))







#
