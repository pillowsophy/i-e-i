level = 3
numofkeys = 5 #the number of mainkeywords   #2**level -1 #sum of G.P. with common ratio = 2

from algorithms.preprocessing import get_data, word_by_sent, wbys_to_word, word_to_idx, idx_by_sent
# text = get_data('data/EI_original copy.txt')
text = get_data()
wbys = word_by_sent(text)
wordlist = wbys_to_word(wbys)
wtoi = word_to_idx(wordlist)
ibys = idx_by_sent(wbys, wtoi)

from algorithms.textrank import count_window, textrank_keyword, textrank_allwords
counter = count_window(ibys, 5)
# mainkeywords = textrank_keyword(ibys, wordlist,numofkeys)
# keywords = textrank_allwords(ibys, wordlist)
# print(keywords)

import algorithms.visualization as vis
cnt_draw = vis.counter_draw(counter,wordlist)
IG = vis.initialGraph(cnt_draw,wordlist)

import community
comm = community.best_partition(IG)

isUsed = 0
data = []
for key, value in comm.items():
    if isUsed & (1<<value): # already used community
        for circle in data:
            if circle["children"][0]["name"] == value:
                circle["children"][0]["children"].append({"name": key, "size": 10})
    else:# first to be used
        isUsed |= (1<<value)
        circle = {}
        circle["name"] = key
        circle["children"] = [{"name": value, "children": []}]
        data.append(circle)

import json
with open("d3/my_cp.json", "w") as json_file:
   json.dump(data, json_file, indent=4)
