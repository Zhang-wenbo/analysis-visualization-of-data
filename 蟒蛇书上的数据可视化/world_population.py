import json
import pygal
from pygal.style import LightColorizedStyle as LCS,RotateStyle as RS#整改整个表的主题,样式设置
from country_codes import get_country_code

#将数据加载到一个列表中
filename = 'population_data.json'#查看这个json文件，本书就是一个列表，里面的每一个元素都是一组字典
with open(filename) as f:
    pop_data = json.load(f)#将数据转换成python能处理的格式，这里是一个列表

cc_populations = {}#创建一个包含人口数量的字典
#打印每个国家2010年的人口数据
for pop_dict in pop_data:
    if pop_dict['Year'] == '2000':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

#根据人口数量将所有的国家分为三组
cc_pops_1,cc_pops_2,cc_pops_3 = {},{},{}
for cc,pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

#看看每组分别包含多少个国家
print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))

wm_style = RS('#336699', base_style=LCS)#十六进制的RGB色彩，基于LCS的颜色
wm = pygal.maps.world.World(style=wm_style)
wm.title = "按组别的完整的世界人口地图(2010)"
wm.add('0-10m',cc_pops_1)
wm.add('10m-1bn',cc_pops_2)
wm.add('>10bn',cc_pops_3)

wm.render_to_file("A按组别的完整的世界人口地图.svg")