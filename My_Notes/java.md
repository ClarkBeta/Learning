# Java
根据[Java教程-廖雪峰的官方网站](https://liaoxuefeng.com/books/java/introduction/index.html)整理
# 1.快速入门
## 1.1 Java程序基础
### 1.1.1 Java程序基本结构
```java
/**
 * 可以用来自动创建文档的注释
 * @author minos
 */
public class Main {// 类名是Main
    //public是访问修饰符，表示该class是公开的
    public static void main(String[] args) {//这里的方法名是main，返回值是void，表示没有任何返回值。
        //Java入口程序规定的方法必须是静态方法，方法名必须为main，括号内的参数必须是String数组。
        // 向屏幕输出文本:
        System.out.println("Hello, world!");//每一行语句必须以分号结束
        /* 多行注释开始
        注释内容
        注释结束 */
    }// 方法定义结束
} // class定义结束
```
### 1.1.2 变量和数据类型
#### 变量
在Java中，变量分为两种：基本类型的变量和引用类型的变量。
```java
public class Main {
    public static void main(String[] args) {
        int x=100;// 定义int类型变量x，并赋予初始值100
        System.out.println(x);// 打印该变量的值
        x=200;// 重新赋值为200(不能指定变量类型int)
        System.out.println(x);
        //变量可以反复赋值
    }
}
```
#### 基本数据类型
整数类型：byte，short，int，long
浮点数类型：float，double
字符类型：char
布尔类型：boolean
#### 整型
对于整型类型，Java只定义了带符号的整型，因此，最高位的bit表示符号位（0表示正数，1表示负数）。各种整型能表示的最大范围如下：

byte：-128 ~ 127
short: -32768 ~ 32767
int: -2147483648 ~ 2147483647
long: -9223372036854775808 ~ 9223372036854775807
```java
public class Main {
    public static void main(String[] args) {
        int i = 2147483647;
        int i2 = -2147483648;
        int i3 = 2_000_000_000; // 加下划线更容易识别
        int i4 = 0xff0000; // 十六进制表示的16711680
        int i5 = 0b1000000000; // 二进制表示的512

        long n1 = 9000000000000000000L; // long型的结尾需要加L
        long n2 = 900; // 没有加L，此处900为int，但int类型可以赋值给long
        int i6 = 900L; // 错误：不能把long型赋值给int
    }
}
```
#### 浮点型
```java
public class Main {

    public static void main(String[] args) {
        float f1 = 3.14f;
        float f2 = 3.14e38f; // 科学计数法表示的3.14x10^38
        float f3 = 1.0; // 错误：不带f结尾的是double类型，不能赋值给float

        double d = 1.79e308;
        double d2 = -1.79e308;
        double d3 = 4.9e-324; // 科学计数法表示的4.9x10^-324
    }
}
```
对于float类型，需要加上f后缀。
浮点数可表示的范围非常大，float类型可最大表示3.4x1038，而double类型可最大表示1.79x10308。

#### 布尔类型
```java
public class Main {

    public static void main(String[] args) {
        boolean b1 = true;
        boolean b2 = false;
        boolean isGreater = 5 > 3; // 计算结果为true
        int age = 12;
        boolean isAdult = age >= 18; // 计算结果为false
    }
}
```
#### 字符类型
字符类型char表示一个字符。
```java
public class Main {
    public static void main(String[] args) {
        char a = 'A';
        char zh = '中';
        System.out.println(a);
        System.out.println(zh);
    }
}
```
注意char类型使用单引号'，且仅有一个字符，要和双引号"的字符串类型区分开。
#### 引用类型
```java
String s = "hello";
```
