# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 10:59:24 2021
Shopify Data Science Challenge Question 1
@author: Rajat Bakshi
"""
import matplotlib.pyplot as plt
import pandas as pd


pd.options.mode.chained_assignment = None #disables 'copying' of dfs, rather modifies original df
pd.set_option('display.max_columns', None) #will display all columns instead of only displaying the first and last few

df=pd.read_csv("2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv")
print(df.head)

print("AOV on unfiltered data: ",df.order_amount.mean()) #calculates average order amount

#Due to a high AOV, order amounts are investigated visually on a plot to 
#get an understanding for its distribution
plt.figure(1)
plt.title('Fig. 1 - Order ID vs. Order Amount')
plt.xlabel('OrderID')
plt.ylabel('Order Amount ($)')
plt.scatter(df.order_id,df.order_amount, alpha = 0.3)
plt.savefig("Q1_Fig1.png",bbox_inches = "tight",dpi=90)

#From examining the Fig 1 Order ID vs. Order Amount plot, it can be seen that a few 
#orders are around $700,000 for the order amount. In addition, some orders around 
#roughly $50,000 average also exist as seen in the plot. To confirm that these orders
#are bulk orders and not erroneous data, an Order Amount vs. Total Items
#plot is created.
plt.figure(2)
plt.title('Fig 2. - Total Items Per Order vs. Order Amount')
plt.xlabel('Total Items per order')
plt.ylabel('Order Amount ($)')
plt.scatter(df.total_items,df.order_amount, alpha = 0.3)
plt.savefig("Q1_Fig2.png",bbox_inches = "tight",dpi=90)

#From the Fig 2 Total Items per Order vs. Order Amount plot, it can be seen that two groups
# of data points exist; one on the low range of total items and one around roughly
#2000 items. It seems strange that some orders where total items are low are totalling
#up to roughly $100,000 or more. 
#Closer examination is done by plotting the same plot, but with custom x and y-axis range so as to
#narrow in on such data points.
plt.figure(3)
plt.title('Fig. 3 - Total Items Per Order vs. Order Amount (Order Amount < $200000 points only)')
plt.xlabel('Total Items per order')
plt.ylabel('Order Amount ($)')
plt.xlim([0,20])
plt.ylim([0,200000])
plt.scatter(df.total_items,df.order_amount, alpha = 0.3)
plt.savefig("Q1_Fig3.png",bbox_inches = "tight",dpi=90)

#From looking at the Fig. 3 Total Items per Order vs. Order Amount plot concentrating on the lower ranged
#data points, it can be seen that several data points with a low Order amount exist while
# a few data points seem to be going up in Order Amount linearly with respect to Total Items Per Order
#This linear relationship could perhaps be one shoe shop selling a very expensive shoe
#and getting multiple orders of varying quantities. Or, it could be erroneous
#data from a shoe shop.

#But first, we take a look at the data points in the lowest Order Amount range ( lets say, <$5000)
#to ensure that these points don't seem erroneous.
plt.figure(4)
plt.title('Fig. 4 - Total Items Per Ordervs. Order Amount (Order Amount < $3000 points only)')
plt.xlabel('Total Items per order')
plt.ylabel('Order Amount ($)')
plt.xlim([0,10])
plt.ylim([0,3000])
plt.scatter(df.total_items,df.order_amount, alpha = 0.3)
plt.savefig("Q1_Fig4.png",bbox_inches = "tight",dpi=90)
#These data points appear normal. Order amount goes up with No. of items ordered and the
#cost seems within reasonable range.

#Now, to determine the meaning of the data points that have incredibly high Order Amount to
# No. of items ratio (ie. cost of each shoe) as found from examining Fig.3 Total Items Per Order vs. Order Amount plot,
# we create a data frame that holds these points only and see how many unique shops are involved.

df_expensiveShoesPoints=df[df.order_amount<200000]
df_expensiveShoesPoints=df_expensiveShoesPoints[df.order_amount>20000]

print("No. of orders where shoe is expensive is :",len(df_expensiveShoesPoints)) #46 orders

print("Shop IDs with such expensive shoes: ",df_expensiveShoesPoints.shop_id.unique())
#It seems that shop with shop_id 78 is the only shop selling such "expensive" shoes.
df_shopID_78=df[df.shop_id==78]
df_shopID_78["cost per shoe"]=df_shopID_78.order_amount/df_shopID_78.total_items
print("Shoe price at shop 78: ",df_shopID_78["cost per shoe"].unique()) #The cost of the shoe per order is the same
#across all orders from this shop per expectation. However, the cost is quite expensive ($25,725)
#It is possible that the shop sells a shoe that is incredibly expensive by design (although not likely uniqueness as
#46 orders of them with one or more pair per order have been ordered). Though it is also possible that the shoe cost in the
#system was inputted erroneously.

print("Range of No. of items ordered per order",df.total_items.unique())
#From this, it is seen that orders range from one item order to 8 items ordered per order with the
#exception of 2000 items ordered per order, which shall be assumed to be a "bulk order"

df_withoutShop_78=df[df.shop_id!=78] #Creating dataframe that does not contain shop 78 data (as it is an anomaly)


df_usualOrders=df_withoutShop_78[df_withoutShop_78.total_items<=8]#Dataframe that contains regular orders
df_bulkOrders=df_withoutShop_78[df_withoutShop_78.total_items>8] #Dataframe that contains bulk orders


usualOrdersAOV=df_usualOrders.order_amount.mean() #AOV for regular orders
bulkOrdersAOV=df_bulkOrders.order_amount.mean() #AOV for bulk orders


print("Usual orders AOV: ",df_usualOrders.order_amount.mean())
print("Bulk orders AOV: ",df_bulkOrders.order_amount.mean())

'''
---------Answers to Question 1-----------------------------------------------
A)
From the analysis above, calculating AOV on the original unfiltered data by averaging the
total_amount column (yielding $3145.13) is not ideal due to two apparent clusters of data
(regular/usual orders that would yield sensible AOV vs. bulk orders that amount to much greater
Order Amounts). In addition, a very small fraction of data points are an anomaly in the data set ("expensive" shoes
of shop_id 78; whether by actual product price, or erroneous data) that are not representative of 
the full dataset and significantly affect AOV as well.

B)
Thus, calculation of two AOVs are proposed; one for normal/regular orders, and one for bulk; both 
omitting data concerning shop with shop_id 78.

C)
The AOV for usual orders was calculated to be $302.58
The AOV for bulk orders was calculated to be $704,000.00
'''


    











