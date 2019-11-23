import json
import pandas as pd


def get_json_file(json_file_path):
    with open(json_file_path) as json_file:
        data =json.load(json_file)
    return data

def write_line_to_file(input_path, input_str):
    with open(input_path, "w") as file:
        file.write(input_str)

def write_lines(input_path, input_list):
    with open(input_path, "w", encoding="utf-8") as file:
        for line in input_list:
            file.write(line)



authors_info_file_path = input("plz enter authors info file path\n  >>> ")
output_file_path = input("plz enter output file path without extension: \n  >>> ")
data = get_json_file(authors_info_file_path)

print("Creating edges list . . .")
edges_list = []
cntr = 0
lndata = len(list(data))
for author_name in data:
    cntr += 1
    print("\r  {}/{} | authors checked".format(cntr, lndata), end='')
    co_authors = []
    years = list(set(data[author_name]["years"]))
    for year in years:
        co_authors = data[author_name][str(year)]["co_authors"]
        for co_auths in co_authors:
            peers = [author_name]
            peers.extend(co_auths)
            lnlst = (len(peers)-1)
            for i in range(lnlst):
                for person in peers[1:]:
                    edge = [peers[0],person,int(year)]
                    edges_list.append(edge)

                del(peers[0])


nodes = {}
for edge in edges_list:
    nodes[edge[0]]={"id":0 , "years":[]}
    nodes[edge[1]]={"id":0 , "years":[]}
    # print(nodes)
author_names = list(nodes)
for auth,i in zip(author_names, range(len(author_names))):
    nodes[auth]["id"] = i + 10000000
# print(nodes)


print("\nAdd year to nodes . . .")
lnaths= len(author_names)
lnedgs= len(edges_list)
cntrath = 0
cntredge = 0
for auth in author_names:
    cntrath += 1
    nodes[auth]["years"].extend(list(set(data[auth]["years"])))
    # for edge in edges_list:
    #     cntredge += 1
    #     print("\r {}/{}   |   {}/{}".format(cntrath, lnaths, cntredge, lnedgs), end='')
    #     if (edge[0] == auth) or (edge[1] == auth):
    #         nodes[auth]["years"].append(edge[2])
# print(nodes)


'''
###################################
 Extracting edges
 ** Nodes remain in the network after
    they join to the network.
###################################askljdhalkjshdljkas
'''
edges_by_year = dict()
for year in range(2000, 2018):
    edges_by_year["{}".format(year)] = []

for year in range(2000, 2018):
    print("\nExtracting year({}) edges . . .".format(year))
    cntr = 0
    output_edges_df = pd.DataFrame(columns=["Source", "Target"])
    lnedges = len(edges_list)
    sources = []
    targets = []
    for edge in edges_list:
        cntr += 1
        print("\r  {}/{}".format(cntr, lnedges), end="")
        if edge[2] <= year:
            sources.append(nodes[edge[0]]["id"])
            targets.append(nodes[edge[1]]["id"])


    output_edges_df["Source"] = sources
    output_edges_df["Target"] = targets
    output_edges_df.to_csv("{}-{}.csv".format(output_file_path, year), index=False)


'''
###################################
 Extracting edges
###################################
'''

# years_nodes = dict()
# for year in range(2000, 2018):
#     years_nodes["{}".format(year)] = set()
#
# for auth in author_names:
#     nodes[auth]["years"]= [int(year) for year in list(set(nodes[auth]["years"]))]
#     for year in range(min(nodes[auth]["years"]), max(nodes[auth]["years"])+1):
#         years_nodes["{}".format(year)].add(nodes[auth]["id"])
#     # print(nodes[auth]["years"][0])
#     # print(type(nodes[auth]["years"][0]))
#     # break
#
# for year in range(2000, 2018):
#     print("Len {}: {}".format(year, len(years_nodes["{}".format(year)])))
#
#
# for year in range(2000, 2018):
#     print()
#     print("Extracting year({}) edges . . .".format(year))
#     output_edges_df = pd.DataFrame(columns=["Source", "Target"])
#     lnedges = len(edges_list)
#     sources = []
#     targets = []
#     for edge,i in zip(edges_list, range(lnedges)):
#         print("\r  {}/{}".format(i+1, lnedges), end="")
#         if nodes[edge[0]]["id"] in years_nodes["{}".format(year)] and nodes[edge[1]]["id"] in years_nodes["{}".format(year)]:
#             sources.append(nodes[edge[0]]["id"])
#             targets.append(nodes[edge[1]]["id"])
#
#     output_edges_df["Source"] = sources
#     output_edges_df["Target"] = targets
#
#     output_edges_df.to_csv("{}-{}.csv".format(output_file_path, year), index=False)

exit()
print("\nExtracting gexf file . . .\n")
lines = []
lines.append("<?xml version=\"1.0\" encoding=\"UTF-8\"?>"+ "\n")
lines.append('<gexf xmlns="http://www.gexf.net/1.3" version="1.3" xmlns:viz="http://www.gexf.net/1.3/viz" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.gexf.net/1.3 http://www.gexf.net/1.3/gexf.xsd">\n')
lines.append('  <meta lastmodifieddate="2019-09-18">\n')
lines.append('    <creator>Gephi 0.9</creator>\n')
lines.append('    <description></description>\n')
lines.append('  </meta>\n')
lines.append('  <graph defaultedgetype="undirected" timeformat="double" timerepresentation="timestamp" mode="dynamic">\n')
lines.append('    <attributes class="node" mode="dynamic">\n')
lines.append('      <attribute id="score" title="score" type="integer"></attribute>\n')
lines.append('    </attributes>\n')
lines.append('    <nodes>\n')
lnans = len(author_names)
cntr = 0
print("Adding Nodes . . .")
for auth in author_names:
    cntr+=1
    print("\r  {}/{}".format(cntr, lnans), end='')
    line = '      <node id="{}" label="{}">\n'.format(nodes[auth]["id"], auth)
    lines.append(line)
    lines.append('        <spells>\n')
    for year in sorted(nodes[auth]["years"]):
        line='          <spell timestamp="{}"></spell>\n'.format(year)
        lines.append(line)
    lines.append('        </spells>\n')
    lines.append('        <attvalues>\n')
    for year in sorted(nodes[auth]["years"]):
        line='          <attvalue for="score" value="1" timestamp="{}"></attvalue>\n' .format(year)
        lines.append(line)
    lines.append('        </attvalues>\n')
    lines.append('      </node>\n')
lines.append("    </nodes>\n")
lines.append("    <edges>\n")
print("\nAdding edges . . . ")
lnans = len(edges_list)
cntr = 0
for edge,i in zip(edges_list,range(len(edges_list))):
    cntr += 1
    print("\r  {}/{}".format(cntr, lnans), end='')
    line='      <edge id="{}" source="{}" target="{}"></edge>\n'.format(i+1,nodes[edge[0]]["id"], nodes[edge[1]]["id"])
    lines.append(line)
lines.append("    </edges>\n")
lines.append("  </graph>\n")
lines.append("</gexf>\n")


write_lines(output_file_path + ".gexf", lines)

# print(*lines,sep="\n")
# print(*edges_list, sep="\n")
