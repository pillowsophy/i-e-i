
def paragraph(sent, wordlist, testword = ""):
    ret = dict()
    for w in wordlist:
        ret[w] = ""
        for i, s in enumerate(sent):
            if(s.lower().find(" " + w + " ",0,-1) != -1):
                if(len(s) < 10 | len(s) > 300):
                    continue
                if(i > 0):
                    ret[w] += sent[i-1] + "."
                ret[w] += sent[i] + "."
                if(i < len(sent)):
                    ret[w] += sent[i+1] + "."
                break
    return ret
            
