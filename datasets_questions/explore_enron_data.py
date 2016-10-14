#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
scount = 0
ecount = 0
pcount = 0
print len(enron_data)
for i in enron_data.values():
	if i['poi']==True and i['total_stock_value']=='NaN':
		pcount+=1
	# if i['email_address']=='NaN':
	# 	ecount +=1
print pcount
print (pcount)
# x =  ((pcount+10)*100)/(len(enron_data)+10)
# print x
# print enron_data.values()[1]
# print enron_data['SKILLING JEFFREY K']['total_payments']
# print enron_data['FASTOW ANDREW S']['total_payments']
# print enron_data['LAY KENNETH L']['total_payments']

# print len(enron_data.values()[0].keys())
# for i in enron_data.values():
# 	# print i['poi']
# 	if i['poi']==True:
# 		count = count + 1
# print count
		
# with open("../final_project/poi_names.txt", "r") as f:

# 	for line in f:
# 		if line[:1]=='(':
# 			count +=1
# 	print count



