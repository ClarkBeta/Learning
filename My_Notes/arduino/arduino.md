# Arduino
## 1.Arduino基础
### 1.1程序结构
```cpp
/*
 Name:		Sketch1.ino
 Created:	2025/1/25 19:53:27
 Author:	clark
*/

// 当您按下复位键或给电路板供电时，设置函数会运行一次。
void setup() {

}

// 循环函数会一直重复运行，直到断电或重置。
void loop() {
  
}
```
### 1.2 c++基础
```cpp
/*
 Name:		Sketch1.ino
 Created:	2025/1/25 19:53:27
 Author:	clark
*/

// 当您按下复位键或给电路板供电时，设置函数会运行一次。
void setup() {
	#define name "data"//  #define 常量名 常量值

	int i;//  类型 变量名
	int i = 95;
	
	//int -32768~32767
	//unsigned int 0~65535
	//long -2^31~2^31-1
	//unsigned long 0~2^32-1
	//short -32768~32767

	char a = '1';//字符型 单引号

	boolean b = false;//布尔型

	//  && and
	//  || or
	//  ! not
	//  ++ 
	//  --
	//其他运算符与python相同

	int c[5];//数组定义 下标访问

	String abc="arduino";//定义字符串

	/*
	if () {

	}
	*/
	
	/*
	if () {

	}
	else{

	}
	*/

	/*
	if () {

	}
	else if (){

	}
	*/

	/*
	switch ()
	{
		case ():
			...
			break;
		default :
			...
			break;

	*/

	/*
	while ()//while (1)死循环
	{
	...
	}
	*/

	/*
	do
	{
	...
	}
	while()
	*/

	/*
	for (初始化;判断;增量){
	...
	}
	*/


}

// 循环函数会一直重复运行，直到断电或重置。
void loop() {
  
}
```
## 数字io
0和1
```cpp
void setup() {

	//pinMode(pin, mode);设置引脚
	// 
	//INPUT 输入
	//OUTPUT 输出
	//INPUT_PULLUP 上拉

	//digitalWrite(pin, value);输出
	// 
	//HIGH
	//LOW


	//digitalRead(pin);输入

}
```
