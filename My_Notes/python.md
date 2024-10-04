# Python 教程
根据 [Python教程- 廖雪峰的官方网站](https://liaoxuefeng.com/books/python/introduction/index.html) 整理
## 1.第一个Python程序
### 1.1 I/O
#### print
```python
print('hello world')
print('1','2','3')
print(300)
print(200+100)
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
 
c = a & b        # 12 = 0000 1100
print ("1 - c 的值为：", c)#与
 
c = a | b        # 61 = 0011 1101 
print ("2 - c 的值为：", c)#或
 
c = a ^ b        # 49 = 0011 0001
print ("3 - c 的值为：", c)#异或
 
c = ~a           # -61 = 1100 0011
print ("4 - c 的值为：", c)#按位取反（非）
 
c = a << 2       # 240 = 1111 0000
print ("5 - c 的值为：", c)#左移 高位丢弃，低位补0
 
c = a >> 2       # 15 = 0000 1111
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
print(ord('A'))
print(ord('中'))

print(chr(66))
print(chr(25991))
print('\u4e2d\u6587') #==>'中文'

#把str变为以字节为单位的bytes
a=b'abc' #bytes的每个字符都只占用一个字节

#以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('abc'.encode('ascii'))
print('中文'.encode('utf-8'))
# print('中文'.encode('ascii')) 中文编码的范围超过了ASCII编码的范围
#在bytes中，无法显示为ASCII字符的字节，用\x##显示

#要把bytes变为str，就需要用decode()
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore'))

#计算str包含多少个字符，可以用len()函数
print(len('ABC'))
print(len('中文'))
#如果换成bytes，len()函数就计算字节数
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
```
#### 格式化
```python
print('hello,%s' % 'world')
print('hello %s,you have%d' % ('Michael', 1000000))
#%d	整数 %f	浮点数 %s 字符串 %x 十六进制整数
#%s永远起作用 %%来表示一个%

#fromat
print( 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

#f-string
# 字符串如果包含{xxx}，就会以对应的变量替换
r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with radius {r} is {s:.2f}')
```
### 2.3 list,tuple
#### list
```python
a=[1,2,3]

print(a)#->[1,2,3]
print(len(a))#元素的个数 --> 3
print(a[0])#索引从0开始 --> 1
##最后一个元素的索引是len(a) - 1
print(a[-1])#-1最后一个元素 --> 3
print(a[-2])#倒数第2个

a.append(4)#追加元素到末尾
a.insert(0,0)#把元素插入到指定的位置  list.insert(index,value)
a.pop()#删除末尾的元素
a.pop(0)#pop(index)删除指定位置的元素
a[0]=1#替换
a=[1,'2',True]#数据类型可以不同
a=[1,2,3,[4,5,6]]
print(a[3][0])#-->4
a=[]#空
```
#### tuple
```python
a=(1,2)#tuple不可变

a=(1)
print(a)#-->1    int
a=(1,)
print(a)#-->(1,) tuple

a=(1,2,[3,4])
a[2][0]=5
print(a)#-->(1, 2, [5, 4])
#tuple的每个元素，指向不变    变的不是tuple的元素
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
print(list(range(5)))#[0, 1, 2, 3, 4]
for i in a_list:
    print(i)#1  2  3
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
    print(i)#1,2,3,4,5,6,7,8,9,10
```
#### continue
```python
for i in range(10):
    if i%2==0:
        continue
    print(i)#奇数
```
死循环Ctrl+C退出程序
### 2.7 dict,set
#### dict
```python
a={1:1,2:2,3:3,4:4}
print(a[1])

a[5]=5#{1: 1, 2: 2, 3: 3, 4: 4, 5: 5}  
a[0]=0#{1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 0: 0}

a.get(3)#3 key不存在，返回None或者自己指定的value
a.get(6,-1)#-1

a.pop(1)#{2: 2, 3: 3, 4: 4, 5: 5, 0: 0}
```

dict的key必须是不可变对象
这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：
```python
key = [1, 2, 3]
a[key] = 'a list'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
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
a=set([3,2,1,4])#{1, 2, 3, 4} 这个set内部有1,2,3,4这3个元素 不表示set是有序

a=set([1,1,2,2,3,3])#{1, 2, 3}

a.remove(1)#{2,3}

a1=set([1,2,3])
a2=set([2,3,4])
print(a1&a2)#{2, 3}
print(a1|a2)#{1, 2, 3, 4}
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
print(b,c)#3 -1
print(a(1,2))#(3,-1)返回一个tuple
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
print(add_end())#['END']
print(add_end())#['END', 'END']
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
sum(*a)#把list或tuple的元素变成可变参数
```
#### 关键字参数
```python
#关键字参数在函数内部自动组装为一个dict
def person(name,age,**kw):
    print('name:', name, 'age:', age, 'other:', kw)
print(person('Bob', 35, city='Beijing'))#name: Bob age: 35 other: {'city': 'Beijing'}
print(person('Adam', 45, gender='M', job='Engineer'))#name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}

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
# 如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()

for s in 'abcd':
    print(s)#字符串也是可迭代对象

#判断一个对象是可迭代对象
from collections.abc import Iterable
print(isinstance('abc',Iterable))

#对list实现类似Java那样的下标循环
for i,valve in enumerate([1,2,3]):#引用了两个变量
    print(i,valve)

for x,y in [(1,1),(2,4),(3,9)]:
    print(x,y)
```
### 4.3 列表生成式
```python
#生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(1,11)))
#生成[1x1, 2x2, 3x3, ..., 10x10]
L=[]
for i in range(1,11):
    L.append(i*i)
print(L)

#一行语句代替循环生成上面的list
print([x*x for x in range(1,11)])
#if判断
print([x*x for x in range(1,11) if x%2 == 0])
#两层循环
print([m+n for m in 'abc' for n in 'xyz'])

import os
print([a for a in os.listdir('.')])

#使用两个变量
print([x+str(y) for x,y in {'a':1,'b':2}.items()])

print([x for x in range(1, 11) if x % 2 == 0])#正常
#[x for x in range(1, 11) if x % 2 == 0 else 0] 报错 (不能在最后的if加上else)
print([x if x % 2 == 0 else -x for x in range(1, 11)])#正常
#[x if x % 2 == 0 for x in range(1, 11)] 把if写在for前面必须加else，否则报错
#for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else
```
### 4.4 生成器
```python
#这种一边循环一边计算的机制，称为生成器

#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
g=(x*x for x in range(1,11))
print(g)# <generator object <genexpr> at 0x?????????????????>
#如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

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
next(odd())
next(odd())
next(odd())
#每次都返回1
#odd()会创建一个新的generator对象
#正确的写法是创建一个generator对象
o=odd()

for i in fib(6):
    print(i)
#Result:

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
print(isinstance((x*x for x in range (10)),Iterator))#True
#把list、dict、str等Iterable变成Iterator可以使用iter()函数
print(isinstance(iter('abc'),Iterator))#True

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
x=abs #<built-in function abs>  函数本身也可以赋值给变量
#函数名其实就是指向函数的变量
# abs=10 #abs(-10) error

def add(x,y,f):
    return f(x)+f(y)
print(add(-5,-6,abs))
```
一个函数就接收另一个函数作为参数，这种函数就称之为高阶函数
#### 5.1.1 map/reduce
##### map
```python
#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x*x
r=list(map(f,[1,2,3,4,5,6,7,8,9]))
print(r)#[1, 4, 9, 16, 25, 36, 49, 64, 81]
print(list(map(str,[1,2,3,4,5,6,7,8,9])))
```
##### reduce
```python
#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def add(x,y):
    return x+y
print(reduce(add,[1,2,3,4,5]))#15
#把序列[1, 3, 5, 7, 9]变换成整数13579
def add2(x,y):
    return x*10+y
print(reduce(add2,[1,2,3,4,5]))
```
#### 5.1.2 filter
```python
#用于过滤序列

def odd(x):
    return x%2==1
print(list(filter(odd,[1,2,3,4,5])))#[1, 3, 5]

#由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。
```
#### 5.1.3 sorted
```python
print(sorted([1,2,3,-4,-5]))#[-5, -4, 1, 2, 3]
print(sorted([1,2,3,-4,-5],key=abs))#[1, 2, 3, -4, -5]
print(sorted(['bob', 'about', 'Zoo', 'Credit']))#['Credit', 'Zoo', 'about', 'bob']按照ASCII的大小比较
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))#['about', 'bob', 'Credit', 'Zoo']
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True))# 反向
```
### 5.2 返回函数