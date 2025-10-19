import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk()  # 实例存储在rw中
    rw.fill_walk()

    #设置绘图窗口的尺寸
    plt.figure(figsize=(10,6))#单位为英寸

    point_numbers = list(range(rw.num_points))
    # c一般指要映射的列表，与camp参数连用
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    # 突出起点和终点
    plt.scatter(0, 0, c='green', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴
    ax = plt.gca()  # 获取当前的Axes实例，gca是"get current axes"的缩写
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break