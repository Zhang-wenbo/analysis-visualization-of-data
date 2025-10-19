import matplotlib.pyplot as plt#导入matplotlib.pyplot模块并起别名

input_value = [1, 2, 3, 4, 5]#定义横坐标的值，不然横坐标是从0开始的
squares = [1, 4, 9, 16, 25]#定义一个列表squares，用于存储平方数
plt.plot(input_value,squares,linewidth=5)#使用plt.plot()函数绘制折线图,并传入横坐标参数
plt.title("Square Numbers",fontsize=24)#设置标题为"Square Numbers"，字体大小为24
plt.xlabel("Value", fontsize=14)#设置X轴标题为"Value"，字体大小为14
plt.ylabel("Square of Value", fontsize=14)#设置Y轴标题为"Square of Value"，字体大小为14
plt.tick_params(axis='both', labelsize=14)#值越大，刻度标签越大，图越小
plt.show()