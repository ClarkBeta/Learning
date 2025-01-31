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
```