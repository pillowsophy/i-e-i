level = 3
numofkeys = 5 #the number of mainkeywords   #2**level -1 #sum of G.P. with common ratio = 2

from algorithms.preprocessing import get_data, word_by_sent, wbys_to_word, word_to_idx, idx_by_sent
# text = get_data('data/EI_original copy.txt')
text = get_data()
wbys = word_by_sent(text)
wordlist = wbys_to_word(wbys)
wtoi = word_to_idx(wordlist)
ibys = idx_by_sent(wbys, wtoi)

from algorithms.textrank import count_window, textrank_keyword, textrank_graph,keywords_to_nodes 
counter = count_window(ibys, 5)
mainkeywords = textrank_keyword(ibys, wordlist)
g_words = textrank_keyword(ibys, wordlist, onlyWords=True)

import algorithms.visualization as vis
import networkx as nx
import community
import random
cnt_draw = vis.counter_draw(counter,g_words)
IG = vis.initialGraph(cnt_draw,g_words)
vis.communityGraph(IG)

subnodes = keywords_to_nodes(mainkeywords)
nx.set_node_attributes(IG, subnodes)

comms = nx.get_node_attributes(IG, 'comm')
weights = nx.get_node_attributes(IG, 'weight')

data = []
isUsed = 0
for word, comm in comms.items():
    if (isUsed & (1<<comm)) == 0:
        data.append({"name":comm, "children": []})
        isUsed |= (1<<comm)
    for d in data:
        if d["name"] == comm:
            if len(d["children"]) == 0:
                d["children"].append({"name": word, "children": []})
            else:
                d["children"][0]["children"].append({"name": word, "size": weights[word]})


import json
result = {"name":"my_cp", "children": data}
with open("d3/my_cp.json", "w") as json_file:
    json.dump(result, json_file, indent=4)
