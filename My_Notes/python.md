# Python 教程
根据 [Python教程- 廖雪峰的官方网站](https://liaoxuefeng.com/books/python/introduction/index.html) 整理
## 1.第一个Python程序
### 1.1 I/O
#### print
```python
print('hello world') # Output: hello world
print('1','2','3') # Output: 1 2 3
print(300) # Output: 300
print(200+100) # Output: 300
```
#### input
```python
a=input()
print(a)
```
'#'为注释,4个空格缩进
## 2.Python基础
### 2.1 数据类型和变量
#### 整数
```python
#一般整数
a_int=1
a_int=100
a_int=-1
a_int=0
#十六进制
a_int=0xffee
#大数的写法 十六进制同理
a_int=10_000_000_000 #==>10000000000
#Python的整数没有大小限制
```
#### 位运算
```python
a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0
 
c = a & b        # Output: 12 = 0000 1100
print ("1 - c 的值为：", c)#与
 
c = a | b        # Output: 61 = 0011 1101 
print ("2 - c 的值为：", c)#或
 
c = a ^ b        # Output: 49 = 0011 0001
print ("3 - c 的值为：", c)#异或
 
c = ~a           # Output: -61 = 1100 0011
print ("4 - c 的值为：", c)#按位取反（非）
 
c = a << 2       # Output: 240 = 1111 0000
print ("5 - c 的值为：", c)#左移 高位丢弃，低位补0
 
c = a >> 2       # Output: 15 = 0000 1111
print ("6 - c 的值为：", c)#右移
```
#### 浮点数
```python
a_float=0.01
# a_float=12.3e8
a_float=1.2e-5 #==>0.000012
#Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf
```
#### 字符串
```python
a_string='abc'
a_string="I'm OK"
a_string='I\'m \"OK\"!' #转义
#\n表示换行，\t表示制表符，字符\本身转义，\\表示的字符就是\
a_string='\\\n\\'
#'''...'''表示多行内容
a_string=('''
          1
          2
          3''')
# a_string=(r'''
#           1
#           2\n
#           3''')
# print(a_string)
```
#### 布尔值
True/False,and、or和not运算
#### 空值
None不能理解为0，因为0是有意义的，而None是一个特殊的空值
#### 变量
```python
#变量名必须是大小写英文、数字和_的组合，且不能用数字开头
a=1
a='123'
a=True
#变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言
```
#### 常量
```python
#全部大写的变量名表示常量只是一个习惯上的用法
PI = 3.14159265359
```
#### / 和 // 和 %
### 2.2 字符编码
|   |ASCII|Unicode|UTF-8|
|----|----|----|----|
|A|01000001|00000000 01000001|01000001|
|中|x|01001110 00101101|11100100 10111000 10101101|
#### Python的字符串
```python
print(ord('A')) # Output: 65
print(ord('中')) # Output: 20013


print(chr(66)) # Output: B
print(chr(25991)) # Output: 文
print('\u4e2d\u6587') # Output: 中文

#把str变为以字节为单位的bytes
a=b'abc' #bytes的每个字符都只占用一个字节

#以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('abc'.encode('ascii')) # Output: b'abc'
print('中文'.encode('utf-8')) # Output: b'\xe4\xb8\xad\xe6\x96\x87'
# print('中文'.encode('ascii')) 中文编码的范围超过了ASCII编码的范围
#在bytes中，无法显示为ASCII字符的字节，用\x##显示

#要把bytes变为str，就需要用decode()
print(b'ABC'.decode('ascii')) # Output: ABC
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')) # Output: 中文
print(b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore')) # Output: 中

#计算str包含多少个字符，可以用len()函数
print(len('ABC')) # Output: 3
print(len('中文')) # Output: 2
#如果换成bytes，len()函数就计算字节数
print(len(b'\xe4\xb8\xad\xe6\x96\x87')) # Output: 6
```
#### 格式化
```python
print('hello,%s' % 'world') # Output: hello,world
print('hello %s,you have%d' % ('Michael', 1000000)) # Output: hello Michael,you have1000000
#%d	整数 %f	浮点数 %s 字符串 %x 十六进制整数
#%s永远起作用 %%来表示一个%

#fromat
print( 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)) # Output: Hello, 小明, 成绩提升了 17.1%

#f-string
# 字符串如果包含{xxx}，就会以对应的变量替换
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}') # Output: The area of a circle with radius 2.5 is 19.62
```
### 2.3 list,tuple
#### list
```python
a=[1,2,3]

print(a) # Output: [1,2,3]
print(len(a))#元素的个数   Output: 3
print(a[0])#索引从0开始 Output: 1
##最后一个元素的索引是len(a) - 1
print(a[-1])#-1最后一个元素 Output: 3
print(a[-2])#倒数第2个 Output: 2

a.append(4)#追加元素到末尾
a.insert(0,0)#把元素插入到指定的位置  list.insert(index,value)
a.pop()#删除末尾的元素
a.pop(0)#pop(index)删除指定位置的元素
a[0]=1#替换
a=[1,'2',True]#数据类型可以不同
a=[1,2,3,[4,5,6]]
print(a[3][0]) # Output: 4
a=[]#空
```
#### tuple
```python
a=(1,2)#tuple不可变

a=(1)
print(a) # Output: 1    int
a=(1,)
print(a) # Output: (1,) tuple

a=(1,2,[3,4])
a[2][0]=5
print(a) # Output: (1, 2, [5, 4])
#tuple的每个元素，指向不变    变的不是tuple的元素

#元组可以拆分
tup = (4, 5, 6)
a, b, c = tup
print(b) # Output: 5

values = 1, 2, 3, 4, 5
a, b, *rest = values
print(rest) # Output: [3, 4, 5]

#统计某个值得出现频率
a = (1, 2, 2, 2, 3, 4, 2)
print(a.count(2)) # Output: 4


```
### 2.4 条件判断
```python
flag=1
if flag==1:
    pass
elif flag==2:
    pass
elif flag==3:
    pass
else:
    pass

x=0
if x:
    print('1')#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False

#三元表达式

# 传统的if-else语句
if a > b:
max_value = a
else:
max_value = b

# 使用三元表达式
max_value = a if a > b else b
```
### 2.5 模式匹配
```python
a=1

#if
if a==1:
    print(1)
elif a==2:
    print(2)
else:
    print(0)

#match
match a:#匹配字符串和数字
    case x if x>100:#x>100匹配，且变量a赋值给变量x
        print(1)
    case 2:#匹配单个值
        print(2)
    case 1000|2000|3000:#匹配多个值
        print('?')
    case _:# _表示匹配到其他任何情况
        print(0)

a_list=[1,2,3]
match a_list:#匹配列表
    case [1]:
        print(1)
```
### 2.6 循环
#### for
```python
a_list=[1,2,3]
print(list(range(5))) # Output: [0, 1, 2, 3, 4]
for i in a_list:
    print(i) # Output: 1  2  3
```
#### while
```python
#只要条件满足，不断循环
a=100
n=0
while a<=0:
    n+=1
    print(n)
    a-1
```
#### break
```python
#提前退出循环
for i in range(100):
    if i>10:
        break
    print(i) # Output: 1,2,3,4,5,6,7,8,9,10
```
#### continue
```python
for i in range(10):
    if i%2==0:
        continue
    print(i) # Output:1 3 5 7 9    奇数
```
死循环Ctrl+C退出程序
### 2.7 dict,set
#### dict
```python
a={1:1,2:2,3:3,4:4}
print(a[1])

a[5]=5 # Output: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}  
a[0]=0 # Output: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 0: 0}

a.get(3) # Output: 3 key不存在，返回None或者自己指定的value
a.get(6,-1) # Output: -1

a.pop(1) # Output: {2: 2, 3: 3, 4: 4, 5: 5, 0: 0}
```

dict的key必须是不可变对象
这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：
```python
key = [1, 2, 3]
a[key] = 'a list'
'''
Output: 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
'''
```
##### 可变对象
a = ['c', 'b', 'a'];a.sort() ---------->['a', 'b', 'c']
##### 不可变对象
a = 'abc';a.replace('a', 'A')----------->'abc'
b=a.replace('a', 'A')--------------->'Abc'
对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。

和list比较，dict有以下几个特点：
查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。       空间来换取时间

而list相反：
查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
#### set 数学意义上的无序和无重复元素的集合
```python
a=set([3,2,1,4]) # Output: {1, 2, 3, 4} 这个set内部有1,2,3,4这3个元素 不表示set是有序

a=set([1,1,2,2,3,3]) # Output: {1, 2, 3}

a.remove(1) # Output: {2,3}

a1=set([1,2,3])
a2=set([2,3,4])
print(a1&a2) # Output: {2, 3}
print(a1|a2) # Output: {1, 2, 3, 4}
```
## 3.函数
### 3.1 调用函数
```python
abs(-5)

#abs(-5,-1)
#调用函数的时候，如果传入的参数数量不对，会报TypeError的错误

#abs('1')
#如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError的错误

int('1')
float(1)
str(1)
bool(1)

a=abs# 变量a指向abs函数
a(1)
```
### 3.2 定义函数
```python
def abss(a):
    if a>=0:
        return a
    else:
        return -a
#没有return语句，函数执行完毕后也会返回结果，只是结果为None
```
#### 空函数
```python
def nope():
    pass
```
#### 参数检查
```python
def abs_(a):
    if not isinstance(a,(int,float)):
        raise TypeError('???')
    if a>=0:
        return a
    else:
        return -a
```
#### 返回多个值
```python
def a(x,y):
    return x+y,x-y
b,c=a(1,2)
print(b,c) # Output: 3 -1
print(a(1,2)) # Output: (3,-1)返回一个tuple
```
### 3.3 函数的参数
#### 位置参数
```python
def power(x,n):#x和n是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n
    return x**n
```
#### 默认参数
```python
def power(x,n=2):
    return x**n
# 必选参数在前，默认参数在后
# 变化大的参数放前面，变化小的参数放后面
```
```python
def add_end(L=[]):
    L.append('END')
    return L
print(add_end()) # Output: ['END']
print(add_end()) # Output: ['END', 'END']
```
Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
默认参数必须指向不变对象！
      |
      ↓
```python
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
```
#### 可变参数
```python
def sum(*x):#参数x接收到的是一个tuple
    res=0
    for i in x:
        res+=i
    return res
a=[1,2,3]
print(sum(*a)) # Output:6  把list或tuple的元素变成可变参数
```
#### 关键字参数
```python
#关键字参数在函数内部自动组装为一个dict
def person(name,age,**kw):
    print('name:', name, 'age:', age, 'other:', kw)
print(person('Bob', 35, city='Beijing')) # Output: name: Bob age: 35 other: {'city': 'Beijing'}
print(person('Adam', 45, gender='M', job='Engineer')) # Output: name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}

extra = {'city': 'Beijing', 'job': 'Engineer'}
# print(person(**extra))
```
#### 命名关键字参数
```python
def person(name, age, *, city, job):#只接收city和job作为关键字参数,*后面的参数被视为命名关键字参数
    print(name, age, city, job)

def person(name, age, *args, city, job):#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
    print(name, age, args, city, job)

#命名关键字参数必须传入参数名
#对于任意函数，都可以通过类似func(*args, **kw)的形式调用它
```
### 3.4 递归函数
```python
ef fact(n):#如果一个函数在内部调用自身本身，这个函数就是递归函数
    if n==1:
        return 1
    return n * fact(n - 1)#阶乘

#使用递归函数需要注意防止栈溢出 解决递归调用栈溢出的方法是通过尾递归优化
#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
#遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。
```
## 4.高级特性
### 4.1 切片
pass
### 4.2 迭代
```python
#如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
#只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代

d={'a':1,'b':2,'c':3}
for key in d:
    print(key) 
# Output: a b c
# 如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()

for s in 'abcd':
    print(s) # Output: a b c d    字符串也是可迭代对象

#判断一个对象是可迭代对象
from collections.abc import Iterable
print(isinstance('abc',Iterable)) # Output: True

#对list实现类似Java那样的下标循环
for i,valve in enumerate([1,2,3]):#引用了两个变量
    print(i,valve) # Output: a b c

for x,y in [(1,1),(2,4),(3,9)]:
    print(x,y) # Output: a b c
```
### 4.3 列表生成式
```python
print(list(range(1,11))) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

L=[]
for i in range(1,11):
    L.append(i*i)
print(L)
# Output: [1x1, 2x2, 3x3, ..., 10x10]

#一行语句代替循环生成上面的list
print([x*x for x in range(1,11)]) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#if判断
print([x*x for x in range(1,11) if x%2 == 0]) # Output: [4, 16, 36, 64, 100]
#两层循环
print([m+n for m in 'abc' for n in 'xyz']) # Output: ['ax', 'ay', 'az', 'bx', 'by', 'bz', 'cx', 'cy', 'cz']

import os
print([a for a in os.listdir('.')])

#使用两个变量
print([x+str(y) for x,y in {'a':1,'b':2}.items()]) # Output: ['a1', 'b2']

print([x for x in range(1, 11) if x % 2 == 0]) # Output: [2, 4, 6, 8, 10]
#[x for x in range(1, 11) if x % 2 == 0 else 0]  Output: Error (不能在最后的if加上else)
print([x if x % 2 == 0 else -x for x in range(1, 11)]) # Output: [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
#[x if x % 2 == 0 for x in range(1, 11)]  Output: Error  把if写在for前面必须加else，否则报错
#for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else
```
### 4.4 生成器
```python
#这种一边循环一边计算的机制，称为生成器

#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
g=(x*x for x in range(1,11))
print(g) # Output: <generator object <genexpr> at 0x?????????????????>
#如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值
print(next(g)) # Output: 1
print(next(g)) # Output: 4
print(next(g)) # Output: 9
print(next(g)) # Output: 16
print(next(g)) # Output: 25

#每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误
#正确的方法是使用for循环
# print(isinstance(g,Iterable))
for n in g:
    print(n)

#如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现
#普通函数
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n+=1
    return 'done'
#a,b=b,a+b
#    ↓
# t = (b, a + b) # t是一个tuple
# a = t[0]
# b = t[1]

#生成器函数
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b #!!!
        a,b=b,a+b
        n+=1
    return 'done'
#定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不是一个generator函数，调用一个generator函数将返回一个generator

#普通函数是顺序执行，遇到return语句或者最后一行函数语句就返回
#变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 2
    print('step 3')
    yield 3

#请务必注意：调用generator函数会创建一个generator对象，多次调用generator函数会创建多个相互独立的generator。
next(odd()) # Output: 1
next(odd()) # Output: 1
next(odd()) # Output: 1

#odd()会创建一个新的generator对象
#正确的写法是创建一个generator对象
o=odd()

for i in fib(6):
    print(i)
# Output: 

# 1
# 1
# 2
# 3
# 5
# 8

#拿不到generator的return语句的返回值
g=fib(6)
while True:
    try:
        i=next(g)
        print(i)
    except StopIteration as e:
        print('return',e.value)
        break
#必须捕获StopIteration错误
```
### 4.5 迭代器
```python
from collections.abc import Iterator
#list、dict、str虽然是Iterable，却不是Iterator
print(isinstance((x*x for x in range (10)),Iterator)) # Output: True
#把list、dict、str等Iterable变成Iterator可以使用iter()函数
print(isinstance(iter('abc'),Iterator)) # Output: True

#Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算
#Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

for x in [1, 2, 3, 4, 5]:
    pass

# 实际上完全等价于：

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
```
## 5.函数式编程
### 5.1 高阶函数
```python
x=abs  # Output: <built-in function abs>  函数本身也可以赋值给变量
#函数名其实就是指向函数的变量
# abs=10 #abs(-10) error

def add(x,y,f):
    return f(x)+f(y)
print(add(-5,-6,abs)) # Output: 11
```
一个函数就接收另一个函数作为参数，这种函数就称之为高阶函数
#### 5.1.1 map/reduce
##### map
```python
#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x*x
r=list(map(f,[1,2,3,4,5,6,7,8,9]))
print(r) # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(list(map(str,[1,2,3,4,5,6,7,8,9]))) # Output: ['1', '2', '3', '4', '5', '6', '7', '8', '9']
```
##### reduce
```python
#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def add(x,y):
    return x+y
print(reduce(add,[1,2,3,4,5])) # Output: 15
#把序列[1, 3, 5, 7, 9]变换成整数13579
def add2(x,y):
    return x*10+y
print(reduce(add2,[1,2,3,4,5])) # Output: 12345
```
#### 5.1.2 filter
```python
#用于过滤序列

def odd(x):
    return x%2==1
print(list(filter(odd,[1,2,3,4,5]))) # Output: [1, 3, 5]

#由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。
```
#### 5.1.3 sorted
```python
print(sorted([1,2,3,-4,-5])) # Output: [-5, -4, 1, 2, 3]
print(sorted([1,2,3,-4,-5],key=abs)) # Output: [1, 2, 3, -4, -5]
print(sorted(['bob', 'about', 'Zoo', 'Credit'])) # Output: ['Credit', 'Zoo', 'about', 'bob']按照ASCII的大小比较
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower)) # Output: ['about', 'bob', 'Credit', 'Zoo']
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True)) # Output: ['Zoo', 'Credit', 'bob', 'about']  反向
```
### 5.2 返回函数
```python
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax+=n
        return ax
    return sum
f=lazy_sum(1,3,5,7,9)  # Output: <function lazy_Sum.<locals>.sum at 0x??????????????????>
print(f()) # Output: 25

#在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
#我们调用lazy_sum()时，每次调用都会返回一个新的函数
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9) # f1!=f2
```
#### 闭包
```python
#注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(),f2(),f3()) # Output: 9 9 9            事实上fs的内容<function count.<locals>.f at 0x0000023225699B20> <function count.<locals>.f at 0x000002322569A480> <function count.<locals>.f at 0x0000023225698860>
# 到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
#返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

#如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count():
    def g(j):
        def f():
            return j*j
        return f
    fs = []
    for i in range(1, 4):
        fs.append(g(i))
    return fs
f1, f2, f3 = count()
print(f1(),f2(),f3()) # Output: 1 4 9
```
#### nonlocal
```python
#使用闭包，就是内层函数引用了外层函数的局部变量。如果只是读外层变量的值，我们会发现返回的闭包函数调用一切正常
def inc():
    x = 0
    def fn():
        # 仅读取x的值:
        return x + 1
    return fn

f = inc()
print(f()) # Output: 1
print(f()) # Output: 1

def inc():
    x = 0
    def fn():
        nonlocal x
        x = x + 1
        return x
    return fn

f = inc()
print(f()) # Output: 1
print(f()) # Output: 2

#原因是x作为局部变量并没有初始化，直接计算x+1是不行的。但我们其实是想引用inc()函数内部的x，所以需要在fn()函数内部加一个nonlocal x的声明。加上这个声明后，解释器把fn()的x看作外层函数的局部变量，它已经被初始化了，可以正确计算x+1。
#使用闭包时，对外层变量赋值前，需要先使用nonlocal声明该变量不是当前函数的局部变量。
```
### 5.3 匿名函数
#### lambda
```python
# lambda
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))) # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81]

# 通过对比可以看出，匿名函数lambda x: x * x实际上就是：
# def f(x):
#     return x * x
#关键字lambda表示匿名函数，冒号前面的x表示函数参数。
#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

def build(x, y):
    return lambda: x * x + y * y
```
### 5.4 装饰器
```python
import functools
#在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
#本质上，decorator就是一个返回函数的高阶函数。
def log(func):
    # @functools.wraps(func) 完整的decorator的写法
    def w(*args, **kw):
        print(func.__name__)# a.__name__#'a'
        return func(*args, **kw)
    return w

@log
def a():
    print('11111')
a() # Output: 
#相当于a = log(a)

#如果decorator本身需要传入参数
def log(text):
    def decorator(func):
        # @functools.wraps(func) 完整的decorator的写法
        def w(*args, **kw):
            print(text)
            return func(*args, **kw)
        return w
    return decorator
@log('awa')
def a():
    print('11111')
a() # Output: awa 111111
#相当于now = log('execute')(now)
print(a.__name__) # Output: 'w'
#因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
```
### 5.5 偏函数
```python
#假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：
# def int2(x,base=2):
#     return int(x,base)
#相当于
int2=functools.partial(int,base=2)
#相当于
# kw = { 'base': 2 }
# int(x, **kw)

max2=functools.partial(max,10)
max2(5, 6, 7)
#相当于
# args = (10, 5, 6, 7)
# max(*args)
```
## 6.模块
为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里，这样，每个文件包含的代码就相对较少，很多编程语言都采用这种组织代码的方式。在Python中，一个.py文件就称之为一个模块（Module）。
最大的好处是大大提高了代码的可维护性。其次，编写代码不必从零开始。当一个模块编写完毕，就可以被其他地方引用。
可以避免函数名和变量名冲突

如果不同的人编写的模块名相同怎么办？为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）

现在，假设我们的abc和xyz这两个模块名字与其他模块冲突了，于是我们可以通过包来组织模块，避免冲突。方法是选择一个顶层包名，比如mycompany，按照如下目录存放：
```
mycompany
├─ __init__.py
├─ abc.py
└─ xyz.py
```
引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。现在，abc.py模块的名字就变成了mycompany.abc，类似的，xyz.py的模块名变成了mycompany.xyz。

请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany。

类似的，可以有多级目录，组成多级层次的包结构。比如如下的目录结构：
```
mycompany
 ├─ web
 │  ├─ __init__.py
 │  ├─ utils.py
 │  └─ www.py
 ├─ __init__.py
 ├─ abc.py
 └─ utils.py
 ```
文件www.py的模块名就是mycompany.web.www，两个文件utils.py的模块名分别是mycompany.utils和mycompany.web.utils。

自己创建模块时要注意命名，不能和Python自带的模块名称冲突。例如，系统自带了sys模块，自己的模块就不可命名为sys.py，否则将无法导入系统自带的sys模块。
### 6.1 使用模块
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()
```
第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；

第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；

第6行使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；

最后，注意到这两行代码：
```python
if __name__=='__main__':
    test()
```
当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让**一个模块通过命令行运行时执行一些额外的代码**，最常见的就是运行测试。
#### 作用域
在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。

类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；

类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；

之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。

private函数或变量不应该被别人引用，那它们有什么用呢？请看例子：
```python
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
```
我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：

外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。
### 6.2 安装第三方模块
略
## 7.面向对象编程
### 7.1 类和实例
```python
class student(object):#定义类
    def __init__(self,name,score) -> None:#特殊方法“__init__”前后分别有两个下划线！！！   __init__方法的第一个参数永远是self，表示创建的实例本身
        self.__name=name# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
        self.__score=score
        #需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
    def print_score(self):
        print(self.__name,self.__score)
    def get_name(self):#但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：
        print(self.__name)
    def get_score(self):
        print(self.__score)
    def set_score(self,score):#如果又要允许外部代码修改score怎么办？可以再给Student类增加set_score方法：
        self.__score=score
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'
bart=student('Bart Simpson', 59)#创建实例
bart.get_name() # Output: 
bart.get_score() # Output: 
#和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。
```
#### 数据封装
既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了
```python
bart.print_score()
```
我们从外部看Student类，就只需要知道，创建实例需要给出name和score，而如何打印，都是在Student类的内部定义的，这些数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节。
### 7.2 访问限制
```python
bart.get_name() # Output: 'Bart Simpson'
bart.__name='abc'
bart.get_name() # Output: 'Bart Simpson'
#表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。不信试试：
```
### 7.3 继承和多态
```python
class animal(object):
    def run(self):
        print('running')
class dog(animal):
    pass
dogg=dog()
dogg.run() # Output: running      继承
class cat(animal):
    def run(self):
        print('cat running')
catt=cat()
catt.run() # Output: cat running        当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。
print(isinstance(catt,animal)) # Output: True
#在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类

def run_twice(animal):
    animal.run()
    animal.run()
class Tortoise(animal):
    def run(self):
        print('Tortoise is running slowly...')
run_twice(Tortoise())
# 多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思：
# 对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：
# 对扩展开放：允许新增Animal子类；
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
# 继承还可以一级一级地继承下来，就好比从爷爷到爸爸、再到儿子这样的关系。而任何类，最终都可以追溯到根类object，这些继承关系看上去就像一颗倒着的树。比如如下的继承树：

#静态语言 vs 动态语言
# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
```
### 7.4 获取对象信息
#### type
```python
print(type(123)) # Output: <class 'int'>
print(type('abc')) # Output: <class 'str'>
print(type(abs)) # Output: <class 'builtin_function_or_method'>
import types
# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量
```
#### isinstance()
```python
#能用type()判断的基本类型也可以用isinstance()判断
#并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
print(isinstance([1,2,3],(list,tuple))) # Output: True
#总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
```
#### dir()
```python
#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法
print(dir('abc')) # Output: ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
#类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法
#下面的代码是等价的
print(len('abc')) # Output: 3
print('abc'.__len__()) # Output: 3

class a(object):
    def __len__(self):
        return 2
b=a()
print(len(b)) # Output: 2

class myobject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x
a_object=myobject()
print(hasattr(a_object,'x'))# 有属性'x'吗？  Output: true
print(hasattr(a_object,'y'))# 有属性'y'吗？  Output: false
setattr(a_object,'y',1)# 设置一个属性'y'
print(hasattr(a_object,'y')) # Output: true
print(getattr(a_object,'y')) # Output: 1
print(a_object.y) # Output: 1
print(getattr(a_object,'z',404)) # Output: 404  可以传入一个default参数，如果属性不存在，就返回默认值         404

#获得对象的方法
print(hasattr(a_object,'power'))# 有属性'power'吗？  Output: true
print(getattr(a_object,'power'))#获取属性'power'  Output: <bound method myobject.power of <__main__.myobject object at 0x000001974998CBC0>>
```
### 7.5 实例属性和类属性
```python
class student(object):
    name='awa'
s=student()
print(s.name)# 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性    Output: awa
print(student.name)# 打印类的name属性   Output: awa
s.name='qwq'# 给实例绑定name属性
print(s.name)# 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性   Output: qwq
print(student.name)# 但是类属性并未消失，用Student.name仍然可以访问   Output: awa
del s.name# 如果删除实例的name属性
print(s.name)# 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了   Output: awa
#从上面的例子可以看出，在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
```
## 8.面向对象高级编程
### 8.1 使用__slots__
```python
class student(object):
    pass
s=student()
s.name='111'# 动态给实例绑定一个属性
print(s.name) # Output: 111

def set_age(self,age):# 定义一个函数作为实例方法
    self.age=age
from types import MethodType
s.set_age=MethodType(set_age,s)# 给实例绑定一个方法
s.set_age(25)# 调用实例方法
print(s.age) # Output: 25

# 只允许对Student实例添加name和age属性
class student(object):
    __slots__=('name','age')
s=student()
# s.score=999999999999
#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(student):
    pass
a=GraduateStudent()
a.score=99999999999
```
### 8.2 使用@property
```python
Python内置的@property装饰器就是负责把一个方法变成属性调用的
class Student:
    def __init__(self):
        self._age = None
    @property
    def age(self):
        print('获取属性时执行的代码')
        return self._age
    @age.setter
    def age(self, age):
        print('设置属性时执行的代码')
        self._age = age
    @age.deleter
    def age(self):
        print('删除属性时执行的代码')
        del self._age
    @property#还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
    def name(self):
        pass
student = Student()
# 设置属性
student.age = 18
"""
Output: 
设置属性时执行的代码
"""
# 获取属性
print('学生年龄为：' + str(student.age))
"""
Output: 
获取属性时执行的代码
学生年龄为：18
"""
# 删除属性
del student.age
"""
Output: 
删除属性时执行的代码
"""

#要特别注意：属性的方法名不要和实例变量重名。例如，以下的代码是错误的：
# class student(object):
#     @property
#     def brith(self):
#         return self.brith
#这是因为调用s.birth时，首先转换为方法调用，在执行return self.birth时，又视为访问self的属性，于是又转换为方法调用，造成无限递归，最终导致栈溢出报错RecursionError。
```
### 8.3 多重继承
```python
class Animal(object):
    pass
# 大类:
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
class Runnable(object):
    def run(self):
        print('Running...')
class Flyable(object):
    def fly(self):
        print('Flying...')
# 各种动物:
class Dog(Mammal,Runnable):#多重继承
    pass
class Bat(Mammal,Flyable):#多重继承
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass

#MixIn
#在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。
```
### 8.4 定制类
#### \_\_str\_\_
```python
class student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self) -> str:
        return self.name
                    #直接敲变量不用print，打印出来的实例还是不好看
    __repr__=__str__#两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
                    #解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法
print(student('111')) # Output: 111
s=student('222')
print(s) # Output: 222
```
#### \_\_iter\_\_
```python
#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
class fib(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a>10000:
            raise StopIteration()
        return self.a
for i in fib():
    print(i)
# Output: 1 1 2 ...... 6765
```
#### \_\_getitem\_\_
```python
#Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行
class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
```
#### \_\_getattr\_\_
```python
#动态返回一个属性
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
        elif attr=='age':
            return lambda:25
        #此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
s=Student()
print(s.score) # Output: 99
print(s.age()) # Output: 25
#这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
```
#### \_\_call\_\_
```python
#直接在实例本身上调用
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
s = Student('Michael')
s() # Output: My name is Michael.
#把对象看成函数，把函数看成对象
#怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
print(callable(s)) # Output: true
print(callable(10)) # Output: false
```
### 8.5 使用枚举类
```python
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value) # Output: 
#value属性则是自动赋给成员的int常量，默认从1开始计数。

#如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3 
    Thu = 4
    Fri = 5
    Sat = 6
#@unique装饰器可以帮助我们检查保证没有重复值。
# 访问这些枚举类型可以有若干种方法：

# >>> day1 = Weekday.Mon
# >>> print(day1)
# Weekday.Mon
# >>> print(Weekday.Tue)
# Weekday.Tue
# >>> print(Weekday['Tue'])
# Weekday.Tue
# >>> print(Weekday.Tue.value)
# 2
# >>> print(day1 == Weekday.Mon)
# True
# >>> print(day1 == Weekday.Tue)
# False
# >>> print(Weekday(1))
# Weekday.Mon
# >>> print(day1 == Weekday(1))
# True
# >>> Weekday(7)
# Traceback (most recent call last):
#   ...
# ValueError: 7 is not a valid Weekday
# >>> for name, member in Weekday.__members__.items():
# ...     print(name, '=>', member)
# ...
# Sun => Weekday.Sun
# Mon => Weekday.Mon
# Tue => Weekday.Tue
# Wed => Weekday.Wed
# Thu => Weekday.Thu
# Fri => Weekday.Fri
# Sat => Weekday.Sat
```
### 8.6 使用元类
略
## 9.错误、调试和测试
### 9.1 错误处理
#### try
```python
try:
    print('try')
    r=10/0
    print('result',r)
except ZeroDivisionError as e:
    print('except',e)
else:
    print('no error')
finally:
    print('finally')
print('end')
#当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
#没有错误发生，所以except语句块不会被执行，但是finally如果有，则一定会被执行（可以没有finally语句)
#Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:#比如函数main()调用bar()，bar()调用foo()，结果foo()出错了，这时，只要main()捕获到了，就可以处理：   
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')
```
#### 调用栈
出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。
#### 记录错误
```python
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main() # Output: ZeroDivisionError: division by zero
print('END')
#同样是出错，但程序打印完错误信息后会继续执行，并正常退出
```
#### 抛出错误
```python
#因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。
# err_raise.py
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0') # Output: FooError: invalid value: 0

#另一种错误处理的方式
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar() # Output: ValueError!

# 其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。

# raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')
```
### 9.2 调试
#### 断言
```python
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0') # Output: 
#assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错
```
#### logging
```python
import logging
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n) # Output: INFO:root:n = 0
print(10 / n) # Output: ZeroDivisionError: division by zero
# 这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。
```
#### pdb
略
### 9.3 单元测试
略
### 9.4 文档测试
略
## 10.IO编程
### 10.1 文件读写
#### 读文件
```python
f=open('1.txt','r')#'r'表示读
#如果文件不存在，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在
print(f.read())#调用read()方法可以一次读取文件的全部内容
f.close()#文件使用完毕后必须关闭

with open('1.txt','r') as f:
    print(f.read())#和前面等效
# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
#如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便
for line in f.readlines():
    print(line.strip())
```
#### file-like Object
像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。
StringIO就是在内存中创建的file-like Object，常用作临时缓冲。
#### 二进制文件
```python
with open('1.txt','rb') as f:#要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
    print(f.read())
```
#### 字符编码
```python
#要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
#遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略
with open('1.txt','r',encoding='gbk',errors='ignore') as f:
    print(f.read())
```
#### 写文件
```python
#写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件
with open('1.txt','w') as f:
    f.write('hello world!')
#以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入。
```
### 10.2 StringIO和BytesIO
#### StringIO
```python
#StringIO顾名思义就是在内存中读写str
from io import StringIO
f=StringIO()
f.write('abc123!@#')
print(f.getvalue()) # Output: abc123!@#    getvalue()方法用于获得写入后的str
#要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取
```
#### BytesIO
```python
from io import BytesIO
f=BytesIO()
f.write('啊'.encode('utf-8'))
print(f.getvalue()) # Output: b'\xe5\x95\x8a'
```
### 10.3 操作文件和目录
```python
#环境变量
print(os.environ)
print(os.environ.get('PATH'))

#操作文件和目录
print(os.path.abspath('.'))#查看当前目录的绝对路径:
print(os.path.join('/Users/michael', 'testdir'))# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.mkdir('/Users/michael/testdir')# 然后创建一个目录:
os.rmdir('/Users/michael/testdir')# 删掉一个目录:

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
# 在Linux/Unix/Mac下，os.path.join()返回这样的字符串：part-1/part-2
# 而Windows下会返回这样的字符串：part-1\part-2
#同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print(os.path.split('/Users/michael/testdir/file.txt'))

#这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

# 对文件重命名:
os.rename('test.txt', 'test.py')
# 删掉文件:
os.remove('test.py')
```
### 10.4 序列化
```python
#我们把变量从内存中变成可存储或传输的过程称之为序列化
import pickle
d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))#pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。

f=open('dump.txt','wb')
pickle.dump(d,f)#pickle.dump()直接把对象序列化后写入一个file-like Object
f.close()

f=open('dump.txt','rb')
d=pickle.load(f)#用pickle.load()方法从一个file-like Object中直接反序列化出对象
f.close()
print(d)

#JSON
#JSON类型	Python类型
#{}	        dict
#[]	        list
#"string"	str
#1234.56	int或float
#true/false	True/False
#null	    None

import json
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d)) # Output: '{"age": 20, "score": 88, "name": "Bob"}'

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str)) # Output: {'age': 20, 'score': 88, 'name': 'Bob'}
```
#### JSON进阶
```python
#Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化
import json
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student('Bob', 20, 88)
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
print(json.dumps(s, default=student2dict)) # Output: {"name": "Bob", "age": 20, "score": 88}
print(json.dumps(s, default=lambda obj: obj.__dict__)) # Output:  {"name": "Bob", "age": 20, "score": 88}    把任意class的实例变为dict
#因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。

#同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student)) # Output: <__main__.Student object at 0x000001890ECBEE40>
```
## 11.进程和线程
### 11.1 多进程
```python
#multiprocessing
from multiprocessing import Process#multiprocessing模块提供了一个Process类来代表一个进程对象
import os

# 子进程要执行的代码
def run_proc(name):
    print('run %s(%s)' %(name,os.getpid()))
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p=Process(target=run_proc,args=('test',))#创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例
    print('Child process will start.')
    p.start()#用start()方法启动，这样创建进程比fork()还要简单。
    p.join()#join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print('Child process end.')

#Pool
#如果要启动大量的子进程，可以用进程池的方式批量创建子进程
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p=Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()#对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
    print('All subprocesses done.')
#请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。

#子进程
#很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。

import subprocess
print('$ nslookup www.python.org')
r=subprocess.call(['nslookup', 'www.python.org'])#下面的例子演示了如何在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的
print('Exit code:', r)

print('$ nslookup')
p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output,err=p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
print('Exit code:', p.returncode)

#进程间通信
#Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。

from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
```
### 11.2 多线程
```python
#启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)

# 由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命名子线程。名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……

#Lock
#多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。

# multithread
import time, threading

# 假定这是你的银行存款:
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(10000000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
#我们定义了一个共享变量balance，初始值为0，并且启动两个线程，先存后取，理论上结果应该为0，但是，由于线程的调度是由操作系统决定的，当t1、t2交替执行时，只要循环次数足够多，balance的结果就不一定是0了。

# 原因是因为高级语言的一条语句在CPU执行时是若干条语句，即使一个简单的计算：
# balance = balance + n
# 也分两步：
# 计算balance + n，存入临时变量中；
# 将临时变量的值赋给balance。

# 究其原因，是因为修改balance需要多条语句，而执行这几条语句时，线程可能中断，从而导致多个线程把同一个对象的内容改乱了。

# 为了解决这个问题，我们需要给balance加锁，当多个线程同时要修改balance时，只有一个线程能成功地获取锁，然后，把 balance 的值加上或减去指定的数值，最后，释放锁。
balance = 0
lock = threading.Lock()

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()
#多核CPU

#Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。
```
### 11.3 ThreadLocal
```python
# 在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁。
# 但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦

#如果用一个全局dict存放所有的Student对象，然后以thread自身作为key获得线程对应的Student对象如何？
global_dict = {}

def std_thread(name):
    std = Student(name)
    # 把std放到全局变量global_dict中：
    global_dict[threading.current_thread()] = std
    do_task_1()
    do_task_2()

def do_task_1():
    # 不传入std，而是根据当前线程查找：
    std = global_dict[threading.current_thread()]
    ...

def do_task_2():
    # 任何函数都可以查找出当前线程的std变量：
    std = global_dict[threading.current_thread()]
    ...

#ThreadLocal应运而生，不用查找dict，ThreadLocal帮你自动做这件事
import threading
    
# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

#执行结果：

# Hello, Alice (in Thread-A)
# Hello, Bob (in Thread-B)

# 全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，但互不影响。你可以把local_school看成全局变量，但每个属性如local_school.student都是线程的局部变量，可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。
# 可以理解为全局变量local_school是一个dict，不但可以用local_school.student，还可以绑定其他变量，如local_school.teacher等等。
```
### 11.4 进程 vs. 线程
我们介绍了多进程和多线程，这是实现多任务最常用的两种方式。现在，我们来讨论一下这两种方式的优缺点。
首先，要实现多任务，通常我们会设计Master-Worker模式，Master负责分配任务，Worker负责执行任务，因此，多任务环境下，通常是一个Master，多个Worker。
如果用多进程实现Master-Worker，主进程就是Master，其他进程就是Worker。
如果用多线程实现Master-Worker，主线程就是Master，其他线程就是Worker。
多进程模式最大的优点就是稳定性高，因为一个子进程崩溃了，不会影响主进程和其他子进程。（当然主进程挂了所有进程就全挂了，但是Master进程只负责分配任务，挂掉的概率低）著名的Apache最早就是采用多进程模式。
多进程模式的缺点是创建进程的代价大，在Unix/Linux系统下，用fork调用还行，在Windows下创建进程开销巨大。另外，操作系统能同时运行的进程数也是有限的，在内存和CPU的限制下，如果有几千个进程同时运行，操作系统连调度都会成问题。
多线程模式通常比多进程快一点，但是也快不到哪去，而且，多线程模式致命的缺点就是任何一个线程挂掉都可能直接造成整个进程崩溃，因为所有线程共享进程的内存。在Windows上，如果一个线程执行的代码出了问题，你经常可以看到这样的提示：“该程序执行了非法操作，即将关闭”，其实往往是某个线程出了问题，但是操作系统会强制结束整个进程。
在Windows下，多线程的效率比多进程要高，所以微软的IIS服务器默认采用多线程模式。由于多线程存在稳定性的问题，IIS的稳定性就不如Apache。为了缓解这个问题，IIS和Apache现在又有多进程+多线程的混合模式，真是把问题越搞越复杂。

线程切换

无论是多进程还是多线程，只要数量一多，效率肯定上不去，为什么呢？
我们打个比方，假设你不幸正在准备中考，每天晚上需要做语文、数学、英语、物理、化学这5科的作业，每项作业耗时1小时。
如果你先花1小时做语文作业，做完了，再花1小时做数学作业，这样，依次全部做完，一共花5小时，这种方式称为单任务模型，或者批处理任务模型。
假设你打算切换到多任务模型，可以先做1分钟语文，再切换到数学作业，做1分钟，再切换到英语，以此类推，只要切换速度足够快，这种方式就和单核CPU执行多任务是一样的了，以幼儿园小朋友的眼光来看，你就正在同时写5科作业。
但是，切换作业是有代价的，比如从语文切到数学，要先收拾桌子上的语文书本、钢笔（这叫保存现场），然后，打开数学课本、找出圆规直尺（这叫准备新环境），才能开始做数学作业。操作系统在切换进程或者线程时也是一样的，它需要先保存当前执行的现场环境（CPU寄存器状态、内存页等），然后，把新任务的执行环境准备好（恢复上次的寄存器状态，切换内存页等），才能开始执行。这个切换过程虽然很快，但是也需要耗费时间。如果有几千个任务同时进行，操作系统可能就主要忙着切换任务，根本没有多少时间去执行任务了，这种情况最常见的就是硬盘狂响，点窗口无反应，系统处于假死状态。
所以，多任务一旦多到一个限度，就会消耗掉系统所有的资源，结果效率急剧下降，所有任务都做不好。

计算密集型 vs. IO密集型

是否采用多任务的第二个考虑是任务的类型。我们可以把任务分为计算密集型和IO密集型。
计算密集型任务的特点是要进行大量的计算，消耗CPU资源，比如计算圆周率、对视频进行高清解码等等，全靠CPU的运算能力。这种计算密集型任务虽然也可以用多任务完成，但是任务越多，花在任务切换的时间就越多，CPU执行任务的效率就越低，所以，要最高效地利用CPU，计算密集型任务同时进行的数量应当等于CPU的核心数。
计算密集型任务由于主要消耗CPU资源，因此，代码运行效率至关重要。Python这样的脚本语言运行效率很低，完全不适合计算密集型任务。对于计算密集型任务，最好用C语言编写。
第二种任务的类型是IO密集型，涉及到网络、磁盘IO的任务都是IO密集型任务，这类任务的特点是CPU消耗很少，任务的大部分时间都在等待IO操作完成（因为IO的速度远远低于CPU和内存的速度）。对于IO密集型任务，任务越多，CPU效率越高，但也有一个限度。常见的大部分任务都是IO密集型任务，比如Web应用。
IO密集型任务执行期间，99%的时间都花在IO上，花在CPU上的时间很少，因此，用运行速度极快的C语言替换用Python这样运行速度极低的脚本语言，几乎无法提升运行效率。对于IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，脚本语言是首选，C语言开发效率最差。

异步IO

考虑到CPU和IO之间巨大的速度差异，一个任务在执行的过程中大部分时间都在等待IO操作，单进程单线程模型会导致别的任务无法并行执行，因此，我们才需要多进程模型或者多线程模型来支持多任务并发执行。
现代操作系统对IO操作已经做了巨大的改进，最大的特点就是支持异步IO。如果充分利用操作系统提供的异步IO支持，就可以用单进程单线程模型来执行多任务，这种全新的模型称为事件驱动模型，Nginx就是支持异步IO的Web服务器，它在单核CPU上采用单进程模型就可以高效地支持多任务。在多核CPU上，可以运行多个进程（数量与CPU核心数相同），充分利用多核CPU。由于系统总的进程数量十分有限，因此操作系统调度非常高效。用异步IO编程模型来实现多任务是一个主要的趋势。
对应到Python语言，单线程的异步编程模型称为协程，有了协程的支持，就可以基于事件驱动编写高效的多任务程序。我们会在后面讨论如何编写协程。
### 11.5 分布式进程
```python
# 在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。
# Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。由于managers模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。
# 举个例子：如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行，现在，由于处理任务的进程任务繁重，希望把发送任务的进程和处理任务的进程分布到两台机器上。怎么用分布式进程实现？
# 原有的Queue可以继续使用，但是，通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了。
# 我们先看服务进程，服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务：

# task_master.py

import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动Queue:
manager.start()
# 获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去:
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
# 从result队列读取结果:
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)
# 关闭:
manager.shutdown()
print('master exit.')

# 请注意，当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，但是，在分布式多进程环境下，添加任务到Queue不可以直接对原始的task_queue进行操作，那样就绕过了QueueManager的封装，必须通过manager.get_task_queue()获得的Queue接口添加。
# 然后，在另一台机器上启动任务进程（本机上启动也可以）：

# task_worker.py

import time, sys, queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行task_master.py的机器:
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# 端口和验证码注意保持与task_master.py设置的完全一致:
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# 从网络连接:
m.connect()
# 获取Queue的对象:
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')
# 处理结束:
print('worker exit.')

# 任务进程要通过网络连接到服务进程，所以要指定服务进程的IP。
# 现在，可以试试分布式进程的工作效果了。先启动task_master.py服务进程：

# $ python3 task_master.py 
# Put task 3411...
# Put task 1605...
# Put task 1398...
# Put task 4729...
# Put task 5300...
# Put task 7471...
# Put task 68...
# Put task 4219...
# Put task 339...
# Put task 7866...
# Try get results...

# task_master.py进程发送完任务后，开始等待result队列的结果。现在启动task_worker.py进程：

# $ python3 task_worker.py
# Connect to server 127.0.0.1...
# run task 3411 * 3411...
# run task 1605 * 1605...
# run task 1398 * 1398...
# run task 4729 * 4729...
# run task 5300 * 5300...
# run task 7471 * 7471...
# run task 68 * 68...
# run task 4219 * 4219...
# run task 339 * 339...
# run task 7866 * 7866...
# worker exit.

# task_worker.py进程结束，在task_master.py进程中会继续打印出结果：

# Result: 3411 * 3411 = 11634921
# Result: 1605 * 1605 = 2576025
# Result: 1398 * 1398 = 1954404
# Result: 4729 * 4729 = 22363441
# Result: 5300 * 5300 = 28090000
# Result: 7471 * 7471 = 55815841
# Result: 68 * 68 = 4624
# Result: 4219 * 4219 = 17799961
# Result: 339 * 339 = 114921
# Result: 7866 * 7866 = 61873956

# 这个简单的Master/Worker模型有什么用？其实这就是一个简单但真正的分布式计算，把代码稍加改造，启动多个worker，就可以把任务分布到几台甚至几十台机器上，比如把计算n*n的代码换成发送邮件，就实现了邮件队列的异步发送。
# Queue对象存储在哪？注意到task_worker.py中根本没有创建Queue的代码，所以，Queue对象存储在task_master.py进程中：

#                                              │
# ┌─────────────────────────────────────────┐     ┌──────────────────────────────────────┐
# │task_master.py                           │  │  │task_worker.py                        │
# │                                         │     │                                      │
# │  task = manager.get_task_queue()        │  │  │  task = manager.get_task_queue()     │
# │  result = manager.get_result_queue()    │     │  result = manager.get_result_queue() │
# │              │                          │  │  │              │                       │
# │              │                          │     │              │                       │
# │              ▼                          │  │  │              │                       │
# │  ┌─────────────────────────────────┐    │     │              │                       │
# │  │QueueManager                     │    │  │  │              │                       │
# │  │ ┌────────────┐ ┌──────────────┐ │    │     │              │                       │
# │  │ │ task_queue │ │ result_queue │ │◀───┼──┼──┼──────────────┘                       │
# │  │ └────────────┘ └──────────────┘ │    │     │                                      │
# │  └─────────────────────────────────┘    │  │  │                                      │
# └─────────────────────────────────────────┘     └──────────────────────────────────────┘
#                                              │

#                                           Network
# 而Queue之所以能通过网络访问，就是通过QueueManager实现的。由于QueueManager管理的不止一个Queue，所以，要给每个Queue的网络调用接口起个名字，比如get_task_queue。
# authkey有什么用？这是为了保证两台机器正常通信，不被其他机器恶意干扰。如果task_worker.py的authkey和task_master.py的authkey不一致，肯定连接不上。

# 小结
# Python的分布式进程接口简单，封装良好，适合需要把繁重任务分布到多台机器的环境下。
# 注意Queue的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。比如发送一个处理日志文件的任务，就不要发送几百兆的日志文件本身，而是发送日志文件存放的完整路径，由Worker进程再去共享的磁盘上读取文件。
```
## 12.正则表达式
pass
## 13.异步IO
### 13.1 协程 
```python
# 协程，又称微线程，纤程。英文名Coroutine。
# 协程的概念很早就提出来了，但直到最近几年才在某些语言（如Lua）中得到广泛应用。
# 子程序，或者称为函数，在所有语言中都是层级调用，比如A调用B，B在执行过程中又调用了C，C执行完毕返回，B执行完毕返回，最后是A执行完毕。
# 所以子程序调用是通过栈实现的，一个线程就是执行一个子程序。
# 子程序调用总是一个入口，一次返回，调用顺序是明确的。而协程的调用和子程序不同。
# 协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。
# 注意，在一个子程序中中断，去执行其他子程序，不是函数调用，有点类似CPU的中断。比如子程序A、B：

def A():
    print('1')
    print('2')
    print('3')

def B():
    print('x')
    print('y')
    print('z')
# 假设由协程执行，在执行A的过程中，可以随时中断，去执行B，B也可能在执行过程中中断再去执行A，结果可能是：

# 1
# 2
# x
# y
# 3
# z

# 但是在A中是没有调用B的，所以协程的调用比函数调用理解起来要难一些。
# 看起来A、B的执行有点像多线程，但协程的特点在于是一个线程执行，那和多线程比，协程有何优势？
# 最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
# 第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。
# 因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。
# Python对协程的支持是通过generator实现的。
# 在generator中，我们不但可以通过for循环来迭代，还可以不断调用next()函数获取由yield语句返回的下一个值。
# 但是Python的yield不但可以返回一个值，它还可以接收调用者发出的参数。
# 来看例子：
# 传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，但一不小心就可能死锁。
# 如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产，效率极高：

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
# 执行结果：

# [PRODUCER] Producing 1...
# [CONSUMER] Consuming 1...
# [PRODUCER] Consumer return: 200 OK
# [PRODUCER] Producing 2...
# [CONSUMER] Consuming 2...
# [PRODUCER] Consumer return: 200 OK
# [PRODUCER] Producing 3...
# [CONSUMER] Consuming 3...
# [PRODUCER] Consumer return: 200 OK
# [PRODUCER] Producing 4...
# [CONSUMER] Consuming 4...
# [PRODUCER] Consumer return: 200 OK
# [PRODUCER] Producing 5...
# [CONSUMER] Consuming 5...
# [PRODUCER] Consumer return: 200 OK
# 注意到consumer函数是一个generator，把一个consumer传入produce后：

# 首先调用c.send(None)启动生成器；
# 然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
# consumer通过yield拿到消息，处理，又通过yield把结果传回；
# produce拿到consumer处理的结果，继续生产下一条消息；
# produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
# 整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。

# 最后套用Donald Knuth的一句话总结协程的特点：
# “子程序就是协程的一种特例。”
```
### 13.2 使用asyncio
```python
# asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。
# asyncio的编程模型就是一个消息循环。asyncio模块内部实现了EventLoop，把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
# 用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型，然后在coroutine内部用yield from调用另一个coroutine实现异步操作。
# 为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。
# 用asyncio实现Hello world代码如下：

import asyncio

async def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    await asyncio.sleep(1)
    print("Hello again!")

asyncio.run(hello())
# async把一个函数变成coroutine类型，然后，我们就把这个async函数扔到asyncio.run()中执行。执行结果如下：

# Hello!
# (等待约1秒)
# Hello again!

# hello()会首先打印出Hello world!，然后，await语法可以让我们方便地调用另一个async函数。由于asyncio.sleep()也是一个async函数，所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环。当asyncio.sleep()返回时，就接着执行下一行语句。
# 把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的async函数了，因此可以实现并发执行。
# 上述hello()还没有看出并发执行的特点，我们改写一下，让两个hello()同时并发执行：

# 传入name参数:
async def hello(name):
    # 打印name和当前线程:
    print("Hello %s! (%s)" % (name, threading.current_thread))
    # 异步调用asyncio.sleep(1):
    await asyncio.sleep(1)
    print("Hello %s again! (%s)" % (name, threading.current_thread))
    return name
# 用asyncio.gather()同时调度多个async函数：

async def main():
    L = await asyncio.gather(hello("Bob"), hello("Alice"))
    print(L)

asyncio.run(main())
# 执行结果如下：

# Hello Bob! (<function current_thread at 0x10387d260>)
# Hello Alice! (<function current_thread at 0x10387d260>)
# (等待约1秒)
# Hello Bob again! (<function current_thread at 0x10387d260>)
# Hello Alice again! (<function current_thread at 0x10387d260>)
# ['Bob', 'Alice']

# 从结果可知，用asyncio.run()执行async函数，所有函数均由同一个线程执行。两个hello()是并发执行的，并且可以拿到async函数执行的结果（即return的返回值）。
# 如果把asyncio.sleep()换成真正的IO操作，则多个并发的IO操作实际上可以由一个线程并发执行。
# 我们用asyncio的异步网络连接来获取sina、sohu和163的网站首页：

import asyncio

async def wget(host):
    print(f"wget {host}...")
    # 连接80端口:
    reader, writer = await asyncio.open_connection(host, 80)
    # 发送HTTP请求:
    header = f"GET / HTTP/1.0\r\nHost: {host}\r\n\r\n"
    writer.write(header.encode("utf-8"))
    await writer.drain()

    # 读取HTTP响应:
    while True:
        line = await reader.readline()
        if line == b"\r\n":
            break
        print("%s header > %s" % (host, line.decode("utf-8").rstrip()))
    # Ignore the body, close the socket
    writer.close()
    await writer.wait_closed()
    print(f"Done {host}.")

async def main():
    await asyncio.gather(wget("www.sina.com.cn"), wget("www.sohu.com"), wget("www.163.com"))

asyncio.run(main())
# 执行结果如下：

# wget www.sohu.com...
# wget www.sina.com.cn...
# wget www.163.com...
# (等待一段时间)
# (打印出sohu的header)
# www.sohu.com header > HTTP/1.1 200 OK
# www.sohu.com header > Content-Type: text/html
# ...
# (打印出sina的header)
# www.sina.com.cn header > HTTP/1.1 200 OK
# www.sina.com.cn header > Date: Wed, 20 May 2015 04:56:33 GMT
# ...
# (打印出163的header)
# www.163.com header > HTTP/1.0 302 Moved Temporarily
# www.163.com header > Server: Cdn Cache Server V2.0
# ...
# 可见3个连接由一个线程并发执行3个async函数完成。

# 小结
# asyncio提供了完善的异步IO支持，用asyncio.run()调度一个coroutine；
# 在一个async函数内部，通过await可以调用另一个async函数，这个调用看起来是串行执行的，但实际上是由asyncio内部的消息循环控制；
# 在一个async函数内部，通过await asyncio.gather()可以并发执行若干个async函数。
```
### 13.3 使用aiohttp
```python
# asyncio可以实现单线程并发IO操作。如果仅用在客户端，发挥的威力不大。如果把asyncio用在服务器端，例如Web服务器，由于HTTP连接就是IO操作，因此可以用单线程+async函数实现多用户的高并发支持。
# asyncio实现了TCP、UDP、SSL等协议，aiohttp则是基于asyncio实现的HTTP框架。

# 我们先安装aiohttp：
# $ pip install aiohttp
# 然后编写一个HTTP服务器，分别处理以下URL：
# / - 首页返回Index Page；
# /{name} - 根据URL参数返回文本Hello, {name}!。
# 代码如下：

# app.py
from aiohttp import web

async def index(request):
    text = "<h1>Index Page</h1>"
    return web.Response(text=text, content_type="text/html")

async def hello(request):
    name = request.match_info.get("name", "World")
    text = f"<h1>Hello, {name}</h1>"
    return web.Response(text=text, content_type="text/html")

app = web.Application()

# 添加路由:
app.add_routes([web.get("/", index), web.get("/{name}", hello)])

if __name__ == "__main__":
    web.run_app(app)
```
# ----------------The End----------------