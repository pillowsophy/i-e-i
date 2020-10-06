level = 3
numofkeys = 5 #the number of mainkeywords   #2**level -1 #sum of G.P. with common ratio = 2

from algorithms.preprocessing import get_data, word_by_sent, wbys_to_word, word_to_idx, idx_by_sent
text = get_data('data/EI_original copy.txt')
# text = get_data()
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

cnt_draw = vis.counter_draw(counter,g_words)
IG = vis.initialGraph(cnt_draw,g_words)

vis.communityGraph(IG)
comms = nx.get_node_attributes(IG, 'comm')

subnodes = keywords_to_nodes(mainkeywords)
nx.set_node_attributes(IG, subnodes)
weights = nx.get_node_attributes(IG, 'weight')

import pandas as pd
pdc = pd.Series(comms, name='comm')
pdw = pd.Series(weights, name='weight')
data = pd.concat([pdc, pdw], axis=1)
data = data.sort_values(by=['comm','weight'], ascending=[True, False])

from algorithms.makecircle import Circle

MC = Circle(IG, weights)

outercircle = {"name": "my_cp_v2", "children": []}
idx = 0
for c in range(2): #len(df.groupby('comm').size())
    newList = []
    # make new list by each commynities
    for j, w in enumerate(data.index[data['comm'] == c]):
        if (j == 0):
            innercircle = {"name": data.iloc[idx].name}
            idx += data.groupby('comm').size()[c]
        else:
            newList.append(w)
    innercircle["children"] = MC.makeCircle(newList)
    outercircle["children"].append(innercircle)


import json
with open("d3/my_cp_2.json", "w") as json_file:
    json.dump(outercircle, json_file, indent=4)
