from die import Die
import pygal

#创建一个D6
die=Die()

#掷几次骰子，并将结果存储在一个列表中
results=[]
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#分析结果
frequencise = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencise.append(frequency)

#对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
#add()将一系列值添加到图表中(向它传递要给添加的值指定的标签，还有一个列表，其中包含将出现在图表中的值)
hist.add('D6',frequencise)
#图表渲染为一个SVG文件，这种文件的扩展名必须为.svg。
hist.render_to_file('die_visual.svg')