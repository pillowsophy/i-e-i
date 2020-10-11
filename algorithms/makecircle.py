import pandas as pd
import networkx as nx
import algorithms.visualization as vis

class Circle:
    def __init__(self, IG, weights):
        self.IG = IG
        self.weights = weights
        self.nodesize = 100

    ##algorithm
    def makeCircle(self, newlist):
        if(len(newlist) < 7):
            outercircle = []
            for w in newlist:
                outercircle.append({"name": w, "size": str(self.weights[w]*self.nodesize)})
            return outercircle
        
        SG = self.IG.subgraph(newlist) # 기존 그래프가 있어야 간편
        vis.communityGraph(SG)
        newcomms = nx.get_node_attributes(SG, 'comm')
        
        newweights = {}
        for k, v in newcomms.items():
            newweights[k] = self.weights[k]
            
        pdc = pd.Series(newcomms, name='comm')
        pdw = pd.Series(newweights, name='weight')
        df = pd.concat([pdc, pdw], axis=1)
        df = df.sort_values(by=['comm','weight'], ascending=[True, False])
        
        outercircle = []
        idx = 0
        for c in range(len(df.groupby('comm').size())):
            newList = []
            # make new list by each commynities
            for j, w in enumerate(df.index[df['comm'] == c]):
                if (j == 0):
                    innercircle = {"name": df.iloc[idx].name, "size": str(df.iloc[idx]["weight"]*self.nodesize)}
                    idx += df.groupby('comm').size()[c]
                else:
                    newList.append(w)
            innercircle["children"] = self.makeCircle(newList)
            outercircle.append(innercircle)
                
        return outercircle