#coding:utf-8
#author:L.P 
#time:201509060006

#================fun============#
#
#generate submission file separated with blank or comma or \t and so on.
#
#===============================#
import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import matplotlib.pyplot as plt


#---------load test data---------#
df = pd.read_table('test_items.txt',header=None,names=['item_id'])
print df.head()
print "the row numbers of test set",len(df)

#--------- generate all ones coloumn to mathch 'item_id'----------#

trytest =  DataFrame([i for i in range(len(df))],columns=['item_list'])

print trytest.head()

trytest1 =  DataFrame([i for i in range(len(df))],columns=['item_list1'])

trytest2 =  DataFrame([i for i in range(len(df))],columns=['item_list2'])


#===================generate test data===================#
testData0 = pd.merge(df,trytest,right_index=True,left_index=True)   #merge ,only with two columns.

testData1 = pd.merge(trytest1,trytest2,right_index=True,left_index=True)  



testData = pd.merge(testData0,testData1,right_index=True,left_index=True)
print testData.head()


#========================================write submission====================#	
#1.need to remove header.
#2.need to remove index.
#-------separated with blank--------------#
#testDataSubmission =  testData.to_csv('Submission.txt',sep=' ',index=False,header=False)

#-------separated with commas but the first separate is blank.---------#

#testDataSubmission =  testData.to_csv('Submission.txt')
testDataSubmission =  testData.to_csv('Submission.txt',index=False,header=False)
blank = DataFrame()
blank =  blank.to_csv('Submission1.txt',index=False,header=False)
r = open('Submission1.txt','wb')
with open('Submission.txt') as f:
	for line in f:
		split = line.split(',')
		r.write(split[0]+' '+split[1]+','+split[2]+','+split[3])
f.close()		


