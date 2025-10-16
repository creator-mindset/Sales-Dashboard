import matplotlib.pyplot as plt
import numpy as np

month = np.array(["Jan","Feb","Mar","Apr","May","Jun"])
sales = np.array([45000,47000,52000,61000,58000,63000])
profit = np.array([5000,6000,5500,7200,7000,6800])
categories = np.array(["Electronics","Clothes","Furniture"])
cat_sales = np.array([120000,100000,90000])
regions = np.array(["North","South","East","West"])
region_sales = np.array([10000,90000,120000,80000])

plt.suptitle("Sales Dashboard",fontsize=16,fontweight = 'bold')
plt.subplot(2,2,1)
plt.plot(month,sales,marker="o",color="royalblue")
plt.title("Monthly Sales")

plt.subplot(2,2,2)
plt.bar(categories,cat_sales,color=["red","green","blue"])
plt.title("Categories Sales")

plt.subplot(2,2,3)
plt.pie(region_sales,labels=regions,startangle=140)
plt.title("Regional Sales")

plt.subplot(2,2,4)
plt.scatter(sales,profit,color="seagreen",s=70)
plt.title("Profit vs Sales")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.tight_layout(rect=[0,0,1,0.95])
plt.show()
