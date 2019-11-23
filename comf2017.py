import pandas as pd


df = pd.read_csv("D:/test/comf2017Edges.csv")

lines = []

cntr=0
for line in df.iterrows():
    cntr += 1
    print(   " \r    {}/{}".format(cntr, len(df)) , end=""  )
    lines.append("{} {}".format(line[1]["Source"],line[1]["Target"]))

with open("D:/result.txt", "w") as file:
    for l in lines:
        file.write(l + "\n")
