#执行API调用，找到GitHub上星级最高的python项目
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,RotateStyle as RS

#执行API调用并存储响应
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("状态代码:",r.status_code)#打印API的响应状态，200为正常

#将API响应存储在一个变量中
response_dict = r.json()#response响应字典
print("存储库总数:",response_dict['total_count'])

#探索有关仓库的信息
"""
与items相关的是一个列表，里面包含许多字典，每一个字典都存储着一个python库的信息
"""
repo_dicts = response_dict['items']#可以去查看API，items是一个列表，里面存储的是多组字典，每个字典内还有多组键值对信息

names,plot_dicts = [],[]#names用于x轴调用，plot_dicts用于y轴的高度及其工具提示
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
#此循环将每个项目都创建了plot_dict字典，星级用value存储，描述用label存储，并将其加入到polt_dicts的末尾
    plot_dict = {
        'value':repo_dict['stargazers_count'],#字典星级
        'label':repo_dict['description'],#字典描述
        'xlink':repo_dict['html_url'],#Pygal根据与键'xlink'相关联的URL将每个条形都转换为活跃的链接
        }
    plot_dicts.append(plot_dict)

#可视化
my_style = RS('#333399', base_style=LCS)#第一个参数为海军蓝的十六进制（设置为基本色），第二个参数为为LCS类

my_config = pygal.Config()#创建Pygal类的Config实例
#修改my_config的属性
my_config.x_label_rotation = 45#x坐标倾斜45度
my_config.show_legend = False#图例显示与否
my_config.title_font_size = 24#图表标题字体大小
my_config.label_font_size = 14#副标签字体大小（x轴的项目名及y轴上的大部分数字）
my_config.major_label_font_size = 18#主标签（y轴上5000倍数的刻度）
my_config.truncate_label = 15#将较长的项目名缩短为15个字符（如果你将鼠标指向屏幕上被截短的项目名，将显示完整的项目名）
my_config.show_y_guides = False#隐藏水平线
my_config.width = 1000


chart = pygal.Bar(my_config, style=my_style)#xmy_config作为第一个实参，从而通过一个实参传递了所有的 配置设置。
chart.title = "最受欢迎的GitHub仓库"
chart.x_labels = names

chart.add('',plot_dicts)#不需要给这个数据系列添加标签
chart.render_to_file('Python储存库（自动生成plot_dicts,可点击链接）.svg')