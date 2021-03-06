#!/usr/bin/python



import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from pprint import pprint
### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop('TOTAL',0)
data = featureFormat(data_dict, features)
print data.max()
# print data_dict['TOTAL']

### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )
    for k in data_dict.keys():
    	if data_dict[k]['salary']==int(salary):
    		x = k + " " + str(salary)+ " " + str(bonus)
    		matplotlib.pyplot.text( salary, bonus,x)
    		# print k

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.grid(True)
matplotlib.pyplot.show()

# outliers = []
# for key in data_dict:
# 	val = data_dict[key]['salary']
# 	if val =='NaN':
# 		continue
# 	outliers.append((key, int(val))

# pprint(sorted(outliers,key=lambda x:x[1],reverse=True)[:2])
# # outliers = sorted(outliers, key=lambda x:x[1], reverse=True)
# # print(outliers][:2])

outliers = []
for key in data_dict:
    val = data_dict[key]['salary']
    if val == 'NaN':
        continue
    outliers.append((key,int(val)))

pprint(sorted(outliers,key=lambda x:x[1],reverse=True)[:2])
