from die import Die

import pygal

#创建一个D6和一个D10
die_1 = Die()
die_2 = Die(10)

#掷骰子多次，并将结果储存在一个列表中
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#分析结果
frequencise = []
max_result = die_1.num_sides + die_2.num_sides#num_sides我们默认的是6，在die模块里
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencise.append(frequency)

#可视化结果
hist = pygal.Bar()

hist.title = "D6和D10的骰子随机掷50000次的统计"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title = "结果"
hist.y_title = "点和次数"

hist.add("D6 + D10",frequencise)
hist.render_to_file('D6+D10.svg')