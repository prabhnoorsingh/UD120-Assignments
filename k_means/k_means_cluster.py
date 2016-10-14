#!/usr/bin/python 

""" 
    skeleton code for k-means clustering mini-project

"""


import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.preprocessing import MinMaxScaler




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than 4 clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)


### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
# feature_3 = "total_payments"

poi  = "poi"
features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )


### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, line below assumes 2 features)
# for f1, f2 in finance_features:
#     plt.scatter( f1, f2)
# plt.show()

sal = []
ex_stock = []
for users in data_dict:
    vals = data_dict[users]['salary']
    val = data_dict[users]['exercised_stock_options']
    if val == 'NaN':
        continue
    if vals == 'NaN':
        continue
    ex_stock.append(val)
    sal.append(vals)
# stockDiff = max(ex_stock) - min(ex_stock)
# salDiff = max(sal) - min(sal) 
# asal = float(200000 - min(sal))/salDiff
# astock = float(1000000 - min(ex_stock))/stockDiff

# print asal
# print astock

salaryArr = [min(sal), 200000.0 , max(sal)]
stockArr = [min(ex_stock), 1000000.0 , max(ex_stock)]

salNumpy = numpy.array([[e] for e in salaryArr])
stockNumpy = numpy.array([[e] for e in stockArr])

sal_Numpy = MinMaxScaler()
stock_Numpy = MinMaxScaler()

print sal_Numpy.fit_transform(salNumpy)
print stock_Numpy.fit_transform(stockNumpy)

# from sklearn.cluster import KMeans
# clf = KMeans(n_clusters=2)
# pred = clf.fit_predict( finance_features )


# ### cluster here; create predictions of the cluster labels
# ### for the data and store them to a list called pred

# try:
#     Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
# except NameError:
#     print "no predictions object named pred found, no clusters to plot"