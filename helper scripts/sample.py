import numpy as np
#from rdflib.graph import Graph
import pandas as pd
data = np.array(pd.read_csv('yago-wd-facts.nt', sep='\t', header=None).dropna())[:, :-1]
#g = Graph()
#g.parse("yago-wd-facts.nt", format='turtle')
np.random.shuffle(data)
one_limit = int(0.75*len(data))
second_limit = int(0.85*len(data))
third_limit = int(1*len(data))
train, dev, test = data[:one_limit], data[one_limit:second_limit], data[second_limit:third_limit]
np.savetxt("/data/yago_files/train.tsv", train, delimiter='\t', fmt="%s")
np.savetxt("/data/yago_files/dev.tsv", dev, delimiter='\t', fmt="%s")
np.savetxt("/data/yago_files/test.tsv", test, delimiter='\t', fmt="%s")
print(len(data))
