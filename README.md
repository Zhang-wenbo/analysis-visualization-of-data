# 一.基础知识
**Jupyter 常用快捷键**

| 快捷键 | 功能 |
| --- | --- |
| Esc | 从输入模式退出到命令模式 |
| a | 在当前cell上面创建一个新的cell |
| b | 在当前cell下面创建一个新的cel |
| dd | 删除当前cell |
| m | 切换到markdown模式 |
| y | 切换到code模式 |
| Ctry+回车 | 运行cell |
| Shift+回车 | 运行当前cell并创建一个新的cell |


# 二.Numpy
## 1.简介
numpy是Python中科学计算的基础包

它是一个Python库，提供多维数组对象、各种派生对象（例如掩码数组和矩阵）以及用于对数组进行快速操作的各种方法，包括数学、逻辑、形状操作、排序、选择、I/O、离散傅里叶变换、基本线性代数、基本统计运算、随机模拟等等。

numpy的部分功能如下：

1. ndarray，一个具有矢量算术运算和复杂广播能力的快速且节省空间的多维数组
2. 用于对整组数据进行快速运算的标准数学函数（无需编写循环）
3. 用于读写磁盘数据的工具以及用于操作内存映射文件的工具
4. 线性代数、随机数生成以及傅里叶变换功能
5. 用于集成由C、C++、Fortran等语言编写的代码的API

## 2.ndarray 类型
Numpy 数组 (ndarray) 的核心特性

多维性：支持0维（标量）、1维（向量）、2维（矩阵）及更高维数组

同质性：所有元素类型必须一致（通过dtype 指定）

高效性：基于连续内存块存储，支持向量化运算

## 3.ndarray 的属性
| 属性名称 | 通俗解释 | 使用示例 |
| --- | --- | --- |
| shape | 数组的形状：行数和列数（或更高维度的尺寸） | arr.shape |
| ndim | 维度数量：数组是几维的（1维、2维、3维等） | arr.ndim |
| size | 总元素个数：数组中所有元素的总数 | arr.size |
| dtype | 元素类型：数组中元素的类型（整数、浮点数等） | arr.dtype |
| T | 转置：行变列，列变行 | arr.T |
| itemsize | 单个元素占用的内存字节数 | arr.itemsize |
| nbytes | 数组总内存占用量：size*itemsize | arr.nbytes |
| flags | 内存存储方式：是否连续存储（高级优化） | arr.flags |


## 4.ndarry 的创建
1.基础构造：适用于手动构建小规模数组或复制已有数据

2.预定义形状填充：用于快速初始化固定形状的数组（如全0占位、全1初始化）

3.基于数值范围生成：生成数值序列，常用于模拟时间序列、坐标网格等

4.特殊矩阵生成：数学运算专用（如线性代数中的单位矩阵）

5.随机数组生成：模拟实验数据、初始化神经网络权重等场景

6.高级构造方法：处理非结构化数据（如文件、字符串）或通过函数生成复杂数组



| 用途 | 方法 | | | |
| :---: | :---: | --- | --- | --- |
| 基础构造 | **np.array()** | **np.copy()** | | |
| 预定义形状填充 | **np.zeros()** | **np.ones()** | **np.empty()** | **np.full()** |
| 基于数值范围生成 | **np.arange()** | **np.linespace()** | **np.logspace()** | |
| 特殊矩阵生成 | **np.eye()** | **np.diag()** | | |
| 随机数组生成 | **np.random.rand()** | **np.random.randon()** | **np.random.randint()** | |
| 高级构造方法 | **np.array()** | **np.loadtxt()** | **np.fromfunction()** | |


| 名称 | 维度 | 示例 | 备注 |
| --- | --- | --- | --- |
| 标量 | 0 | 5，3.14 | 单个数字，无行列 |
| 向量 | 1 | [1,2,3] | 只有行或列（一维数组） |
| 矩阵 | 2 | [[1,2],[3,4]] | 严格的行列结构（二维表） |
| 张量 | ≥3 | [[[1,2],[3,4]]] | 高阶数组（如RGB图像 |


**矩阵**

矩阵是一个由 行（row）和 列（column）排列成的矩形数组

$$ A = \begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix}
 $$

形状（shape）：这个矩阵有 2行3列，记作 2x3 矩阵

元素（entry）：矩阵中的每个数字称为元素

**几种特殊矩阵**

| 矩阵类型 | 定义 | 例子 |
| --- | --- | --- |
| 零矩阵 | 所有元素为0 | $$ \begin{bmatrix} 0 & 0 \\ 0 & 0  \end{bmatrix} $$ |
| 单位矩阵 | 对角线上为1，其余为0 | $$ \begin{bmatrix} 1 & 0 \\ 0 & 1  \end{bmatrix} $$ |
| 对角矩阵 | 只有对角线有非零值 | $$ \begin{bmatrix} 2 & 0 \\ 0 & 3  \end{bmatrix} $$ |
| 对称矩阵 | A = A<sup>T</sup> | $$ \begin{bmatrix} 1 & 2 \\ 2 & 3  \end{bmatrix} $$ |


## 5.ndarray 的数据类型
| 数据类型 | 说明 |
| --- | --- |
| bool | 布尔类型 |
| int8、uint8<br/>int16、uint16<br/>int32、uint32<br/>int64、uint64 | 有符号、无符号的8位（1字节）整型<br/>有符号、无符号的16位（2字节）整型<br/>有符号、无符号的32位（4字节）整型<br/>有符号、无符号的64位（8字节）整型 |
| | |
| | |
| | |
| float16<br/>float32<br/>float64 | 半精度浮点型<br/>单精度浮点型<br/>双精度浮点型 |
| | |
| | |
| complex64<br/>complex128 | 用两个32位浮点数表示的复数<br/>用两个64位浮点数表示的复数 |
| | |


## 6.索引和切片
| 索引/切片类型 | 描述/用法 |
| --- | --- |
| 基本索引 | 通过整数索引直接访问元素。索引从0开始 |
| 行/列切片 | 使用冒号：切片语法选择行或列的子集 |
| 连续切片 | 从起始索引到结束索引按步长切片 |
| 使用 slice 函数 | 通过 slice(start, stop, step) 定义切片规则 |
| 布尔索引 | 通过布尔条件筛选满足条件的元素。支持逻辑运算符 &（与）、|（或） |


## 7.Numpy 常用函数
| 基   本   数   学 | np.sqrt(x) | 统   计 | np.sum(x) | 比   较 | np.greater(a, b) | 排   序 | np.sort(x) |
| :---: | --- | --- | --- | --- | --- | --- | --- |
| | np.exp(x) | | np.mean(x) | | np.less(a, b) | | x.sort() |
| | np.log(x) | | np.median(x) | | np.equal(a, b) | | np.argsort(x) |
| | np.sin(x) | | np.std(x) | | np.logical_and(a, b) | | np.lexsort(keys) |
| | np.abs(x) | | np.var(x) | | np.where(condition, x, y) | 其   它 | np.concatenate((a, b))      np.split(x, indices)      np.reshape(x, shape)      np.copy(x)      np.isnan(x) |
| | np.power(a, b) | | np.min(x) / np.max(x) | 去   重 | np.unique(x) | | |
| | np.round(x, n) | | np.percentile(x, q) | | np.in1d(a, b) | | |


# 三.Pandas
### 1.简介
Pandas是Python 数据分析工具链中最核心的库，充当数据读取、清洗、分析，统计、输出的高效工具。

Pandas提供了易于使用的数据结构和数据分析工具，！特别适用于处理结构化数据，如表格型数据（类似于Excel表格），Pandas是数据科学和分析领域中常用的工具之一，它使得用户能够轻松地从各种数据源中导入数据，并对数据进行高效的操作和分析。

Pandas是基于NumPy构建的专门为处理表格和混杂数据设计的Python库，核心设计理念包括：

-标签化数据结构：提供带标签的轴

-灵活处理缺失数据：内置NaN处理机制

-智能数据对齐：自动按标签对齐数据

-强大IO工具：支持从CSV、Excel、SQL等20+数据源读写

-时间序列处理：原生支持日期时间处理和频率转换

| 特性 | Series | DataFrame |
| :---: | :---: | :---: |
| 维度 | 一维 | 二维 |
| 索引 | 单索引 | 行索引+列名 |
| 数据存储 | 同质化数据类型 | 各列可不同数据类型 |
| 类比 | Excel单列 | 整张Excel工作表 |
| 创建方式 | pd.Series([1,2,3]) | pd.DataFrame({'col':[1,2,3]}) |


## 2.Series 的属性
| 属性 | 说明 | 属性 | 说明 |
| --- | --- | --- | --- |
| index | Series的索引对象 | loc[ ] | 显式索引，按标签索引或切片 |
| values | Series的值 | iloc[ ] | 隐式索引，按位置索引或切片 |
| dtype或dtypes | Series的元素类型 | at[ ] | 使用标签访问单个元素 |
| shape | Series的形状 | iat[ ] | 使用位置访问单个元素 |
| ndim | Series的维度 |  |  |
| size | Series的元素个数 |  |  |
| name | Series的名称 |  |  |


## 3.Series 的常用方法
| 方法 | 说明 |
| --- | --- |
| head() | 查看前 n 行数据，默认 5 行 |
| tail() | 查看后 n 行数据，默认 5 行 |
| isin() | 判定元素是否包含在参数集合中 |
| isna() | 判定是否缺失值（如 NaN 或 None） |
| sum() | 求和，自动忽略缺失值 |
| mean() | 平均值 |
| min() | 最小值 |
| max() | 最大值 |
| var() | 方差 |
| std() | 标准差 |
| median() | 中位数 |
| mode() | 众数（可返回多个） |
| quantile(q) | 分位数，q 取 0~1 之间 |
| describe() | 常见统计信息（count、mean、std、min、25%、50%、75%、max） |
| value_counts() | 每个唯一值的出现次数 |
| count() | 非缺失值数量 |
| nunique() | 唯一值个数（去重） |
| unique() | 获取去重后的值数组 |
| drop_duplicates() | 去除重复项 |
| sample() | 随机抽样 |
| sort_index() | 按索引排序 |
| sort_values() | 按值排序 |
| replace() | 替换值 |
| keys() | 返回Series的索引l对象 |




## 4.DataFrame
![](https://cdn.nlark.com/yuque/0/2025/png/42519851/1755320018092-b9c3da8a-f758-4469-97a8-a7aeca5faea0.png)

## 5.DateFrame 的属性
| 属性 | 说明 | 属性 | 说明 |
| --- | --- | --- | --- |
| index | DataFrame的行索引 | loc[ ] | 显式索引，按行列标签索引或切片 |
| values | DataFrame的值 | iloc[ ] | 隐式索引，按行列位置索引或切片 |
| dtypes | DataFrame的元素类型 | at[ ] | 使用行列标签访问单个元素 |
| shape | DataFrame的形状 | iat[ ] | 使用行列位置访问单个元素 |
| ndim | DataFrame的维度 | T | 行列转置 |
| size | DataFrame的元素个数 |  |  |
| columns | DataFrame的列标签 |  |  |


## 6.常用方法
| 方法 | 说明 | 方法 | 说明 |
| --- | --- | --- | --- |
| head() | 查看前 n 行数据，默认 5 行 | max() | 最大值 |
| tail() | 查看后 n 行数据，默认 5 行 | var() | 方差 |
| isin() | 判断元素是否包含在参数集合中 | std() | 标准差 |
| isna() | 判断是否为缺失值（如 NaN 或 None） | median() | 中位数 |
| sum() | 求和，自动忽略缺失值 | mode() | 众数（可返回多个） |
| mean() | 平均值 | quantile(q) | 分位数，q 取 0~1 之间 |
| min() | 最小值 | describe() | 常见统计信息（count、mean、std、min、25%、50%、75%、max） |
| value_counts() | 每个唯一值的出现次数 | sort_values() | 按值排序 |
| count() | 非缺失值数量 | replace() | 替换值 |
| duplicated() | 是否重复 | nlargest() | 返回某列最大的 n 条数据 |
| drop_duplicates() | 去除重复项 | nsmallest() | 返回某列最小的 n 条数据 |
| replace() | 替换值 | sample() | 随机抽样 |
| sort_index() | 按索引排序 |  |  |


# 四.数据分析
# 五.数据可视化
## 1.工具简介
| 工具 | 说明 | 优点 | 缺点 |
| :---: | --- | --- | --- |
| matplotlib | Python 最基础可视化库 | 灵活强大、定制性强 | 代码多、风格基础 |
| seaborn | 基于 matplotlib 的高级接口 | 风格美观、统计图方便 | 对简单图略繁琐 |
| pandas plot | 快速图表，调用 .plot() | 快捷、适合 EDA | 图表样式较少 |


# 六.项目实战-房地产市场洞察与价值评估
## 1.数据源介绍
| 字段名 | 含义 | 说明 |
| :---: | :---: | --- |
| city | 城市 | 房屋所在的城市名称，例如：合肥、重庆等 |
| address | 详细地址 | 房屋的具体位置，包含街道、交叉口等信息 |
| area | 面积 | 房屋的面积，单位为平方米(m<sup>2</sup>) |
| floor | 楼层 | 房屋所在的楼层信息，例如：中层(共18层) |
| name | 小区名字 | 房屋所在的小区或楼盘名称 |
| price | 价格 | 房屋的总价，单位为“万”或“元” |
| province | 省份 | 房屋所在的省份或直辖市名称 |
| rooms | 户型 | 房屋的户型结构，例如：3室2厅 |
| toward | 朝向 | 房屋的朝向，例如：南北向、南向等 |
| unit | 单价 | 房屋的单价，单位为：元/m<sup>2</sup> |
| year | 建造年份 | 房屋的建造年份，例如：2025 年建 |
| origin_url | 原始链接 | 房屋信息的来源网页链接 |


## 2.分析和统计问题
| 编号 | 问题 | 分析主题 |
| --- | --- | --- |
| A1 | 哪些变量最影响房价？面积、楼层、房间数哪个影响更大? | 特征相关性 |
| A2 | 全国房价总体分布是怎样的？是否存在极端值？ | 描述性统计 |
| A3 | 哪些城市房价最高？直辖市与非直辖市差异如何？ | 城市对比 |
| A4 | 高价房在面积、楼层等方面有什么特征？ | 价格分层 |
| A5 | 哪种户型最受欢迎？三室比两室贵多少？ | 户型分析 |

