/*
 Input Pullup Serial

 本示例展示如何使用pinMode(INPUT_PULLUP)。通过本程序，Arduino将读取引脚2
 的数字输入并将结果显示在串口监视器中。

 电路：
 * 引脚2连接轻触开关，开关另一端接地
 * 引脚13上安装有开发板内置LED

与使用pinMode(INPUT)不同，我们在使用pinMode(INPUT_PULLUP)时不需要外接上拉或下拉电阻。
开发板内置一个20K欧姆电阻，该电阻将引脚上拉到5V。开关在打开时，引脚读取到高电平。开关闭合后，引脚读取到低电平。

 created 14 March 2012
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/InputPullupSerial
 This example code is in the public domain

 本示例程序的注释文字中文翻译由太极创客提供

www.taichi-maker.com
 */

void setup() {
    //开始串口通讯
    Serial.begin(9600);
    //将引脚2设置为输入上拉模式
    pinMode(2, INPUT_PULLUP);
    pinMode(13, OUTPUT);
}

void loop() {
    //将开关状态数值读取到变量中
    int sensorVal = digitalRead(2);
    //输出开关状态数值
    Serial.println(sensorVal);

    //请留意在上拉模式下，按钮的逻辑状态是反的。
    //即：开关断开时引脚读取到高电平。开关被按下后引脚读取到低电平。
    //按钮被按下后，引脚13连接的LED将被点亮。按钮没有按下时，LED熄灭。

    //如果按钮没有按下，熄灭LED。否则，点亮LED

    if (sensorVal == HIGH) {  //按钮没有按下
        digitalWrite(13, LOW);  //熄灭LED
    }
    else {                  //否则
        digitalWrite(13, HIGH); //点亮LED
    }
}

//在Arduino控制器的2号引脚到GND之前, 连接了一个阻值很大(10kΩ)的电阻。如果没有该电阻, 则当未按下按键时, 2号引脚会一直处于悬空状态, 此时使用digitalRead()函数读取2号引脚的状态会得到一个不稳定的值(可能是高, 也可能是低), 添加这个R1电阻到GND就是为了稳定引脚的电平, 当该引脚悬空时, 就会识别为低电平。而这种将某节点通过电阻接地的做法叫做下拉, 这个电阻叫做下拉电阻。
//
//pinMode(buttonPin, INPUT PULLUP);
//这样就可使能该引脚上的内部上拉电阻, 等效于在该引脚与VCC之间连接了一个阻值为20k~50k的电阻。同下拉电阻一样, 上拉电阻也可以稳定I / O口的电平, 不同的是上拉电阻连接到VCC上, 并将引脚稳定在高电位, 这种电阻叫做上拉电阻。这里使用的是内部上拉电阻, 也可以使用外部上拉电阻来替代。
//
//稳定悬空引脚电平所用的电阻应该尽量选择阻值较大的，一般使用10k电阻。
