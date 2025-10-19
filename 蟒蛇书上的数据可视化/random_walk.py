from random import choice

class RandomWalk():
    """一个生成随机漫步数据的类"""

    def __init__(self,num_points=5000):#def定义的叫类
        """初始化随机漫步的属性"""
        self.num_points = num_points
        #所有随机漫步都始于(0,0)
        #创建两个存储x和y值的列表
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        #不断漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            x_direction = choice([1,-1])#使用choice为x_direction选择一个值，判断左右漫步方向
            x_distance = choice([0,1,2,3,4])#给定步长选择
            x_step = x_direction * x_distance
            #x_step为正则向右移动，负则向左移动，0将垂直移动
            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance
            # y_step为正则向上移动，负则向下移动，0将水平移动
            if x_step == 0 and y_step == 0:#拒绝原地踏步
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)