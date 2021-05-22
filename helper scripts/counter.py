from collections import defaultdict
import pandas as pd

def countAndStore(inp, out):
    sub = defaultdict(lambda: 0)                                                                                                                                                                                       
    pred = defaultdict(lambda: 0)                                                                                                                                                                                      
    obj = defaultdict(lambda: 0)                                                                                                                                                                                       
    sub_obj = defaultdict(lambda: 0)                                                                                                                                                                                   
    total = defaultdict(lambda: 0)                                                                                                                                                                                     
    file = open(inp, 'r')
    lines = file.readlines()                                                                                                                                                                                           
    for line in lines:
        s, p, o = line.split('\t')
        if s[-1] == '\n':
            s = s[:-1]
        if p[-1] == '\n':
            p = p[:-1]
        if o[-1] == '\n':
            o = o[:-1]
        sub[s] += 1                                                                                                                                                                                  
        pred[p] += 1
        obj[o] += 1
        sub_obj[s] += 1
        sub_obj[o] += 1
        total[s] += 1
        total[o] += 1
        total[p] += 1
    list_dic = {"sub":sub, "pred": pred, "obj": obj, "sub_obj": sub_obj, "total": total}                                                                                                                               
    for mydict in list_dic.keys():    
        (pd.DataFrame.from_dict(data=dict(sorted(list_dic[mydict].items(), key=lambda x: x[1], reverse=True)), orient='index') \
            .to_csv(out+"/"+mydict+'.csv', header=False))
