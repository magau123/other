import os
from collections import defaultdict

file = open("long_text.txt").readlines()
result = {"name":"" ,'lei': "",'sub_fund': []}
result["name"] = file[0][:-1]
result["lei"] = file[1][:-1]
temp = {"title":"","isin":[]}
for i in file[2:]:
    i = i[:-1]
    if i[1:3] == ". ":
        if temp["title"] == "":
            temp["title"] = i[3:]
        else:
            result['sub_fund'].append(temp)
            temp = {"title":"","isin":[]}
            temp["title"] = i[3:]
    else:
        temp["isin"].append(i)
result['sub_fund'].append(temp)
print(result)