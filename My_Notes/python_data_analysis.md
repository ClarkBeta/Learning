# Python 数据分析
根据《利用 Python 进行数据分析 · 第 2 版》整理
## 1.准备工作
### 1.1 本书导航
尽管读者各自的工作任务不同，大体可以分为几类：

- 与外部世界交互

阅读编写多种文件格式和数据存储；

- 数据准备

清洗、修改、结合、标准化、重塑、切片、切割、转换数据，以进行分析；

- 转换数据

对旧的数据集进行数学和统计操作，生成新的数据集（例如，通过各组变量聚类成大的表）；

- 建模和计算

将数据绑定统计模型、机器学习算法、或其他计算工具；

- 展示

创建交互式和静态的图表可视化和文本总结。
### 引入惯例
```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import statsmodels as sm
```
### 行话
数据规整（Munge/Munging/Wrangling） 指的是将非结构化和（或）散乱数据处理为结构化或整洁形式的整个过程。这几个词已经悄悄成为当今数据黑客们的行话了。Munge这个词跟Lunge押韵。

伪码（Pseudocode） 算法或过程的“代码式”描述，而这些代码本身并不是实际有效的源代码。

语法糖（Syntactic sugar） 这是一种编程语法，它并不会带来新的特性，但却能使代码更易读、更易写。
## 2.NumPy 基础：数组和矢量计算
### 2.1 NumPy的ndarray：一种多维数组对象
#### 创建ndarray
```python
import numpy as np
data1 = [6, 7.5, 8, 0, 1]
arr1=np.array(data1)
arr1 # Output: [6.  7.5 8.  0.  1. ]

# 嵌套序列（比如由一组等长列表组成的列表）将会被转换为一个多维数组
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
arr2 # Output: array([[1, 2, 3, 4],
     #                [5, 6, 7, 8]])

#因为data2是列表的列表，NumPy数组arr2的两个维度的shape是从data2引入的。可以用属性ndim和shape验证
arr2.ndim # Output: 2
arr2.shape # Output: (2, 4)

#除非特别说明（稍后将会详细介绍），np.array会尝试为新建的这个数组推断出一个较为合适的数据类型。数据类型保存在一个特殊的dtype对象中。
arr1.dtype # Output: dtype('float64')
arr2.dtype # Output: dtype('int32')

np.zeros(10) # Output: array([ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.])
np.zeros((3, 6))
# array([[ 0.,  0.,  0.,  0.,  0.,  0.],
#        [ 0.,  0.,  0.,  0.,  0.,  0.],
#        [ 0.,  0.,  0.,  0.,  0.,  0.]])
np.empty((2, 3, 2))
# array([[[ 0.,  0.],
#         [ 0.,  0.],
#         [ 0.,  0.]],
#        [[ 0.,  0.],
#         [ 0.,  0.],
#         [ 0.,  0.]]])
# 注意：认为np.empty会返回全0数组的想法是不安全的。很多情况下（如前所示），它返回的都是一些未初始化的垃圾值。

np.arange(15) # Output: array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])
```
#### ndarray的数据类型
dtype（数据类型）是一个特殊的对象，它含有ndarray将一块内存解释为特定数据类型所需的信息

dtype是NumPy灵活交互其它系统的源泉之一。多数情况下，它们直接映射到相应的机器表示，这使得“读写磁盘上的二进制数据流”以及“集成低级语言代码（如C、Fortran）”等工作变得更加简单。数值型dtype的命名方式相同：一个类型名（如float或int），后面跟一个用于表示各元素位长的数字。标准的双精度浮点值（即Python中的float对象）需要占用8字节（即64位）。因此，该类型在NumPy中就记作float64。

```python
# 你可以通过ndarray的astype方法明确地将一个数组从一个dtype转换成另一个dtype
arr = np.array([1, 2, 3, 4, 5])
arr.dtype # Output: dtype('float64')
float_arr = arr.astype(np.float64)
float_arr # Output: array([0., 1., 2., 3., 4., 5., 6., 7., 8., 9.])
float_arr.dtype # Output: dtype('float64')

# 注意：使用numpy.string_类型时，一定要小心，因为NumPy的字符串数据是大小固定的，发生截取时，不会发出警告。pandas提供了更多非数值数据的便利的处理方法。
```