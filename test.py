topwords = 100

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
_IG = vis.initialGraph(cnt_draw,g_words)

if(topwords > len(g_words)):
    topwords = len(g_words)
IG = _IG.subgraph(g_words[:topwords])

vis.communityGraph(IG)
comms = nx.get_node_attributes(IG, 'comm')
subnodes = keywords_to_nodes(mainkeywords)
nx.set_node_attributes(IG, subnodes)
weights = nx.get_node_attributes(IG, 'weight')

from algorithms.makecircle import Circle

MC = Circle(IG, weights, comms)

outercircle = {"name": "The Ethics of Information"}
outercircle["children"] = MC.makeCircle(wordlist)

import json
with open("d3/new.json", "w") as json_file:
    json.dump(outercircle, json_file, indent=4)
