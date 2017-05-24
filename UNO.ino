int val;//定义变量val  
int ledpin=13;//定义数字接口13  
void setup()  
{  
  Serial.begin(115200);
  pinMode(ledpin,OUTPUT);//设置数字13 口为输出接口，Arduino 上我们用到的I/O 口都要进行类似这样的定义。 
}  
  
void loop()  
{  
  val=Serial.read();//读取PC 机发送给Arduino 的指令或字符，并将该指令或字符赋给val  
  if(val == 'O')//判断接收到的指令或字符是否是“R”。  
  {//如果接收到的是“R”字符  
    Serial.println("turn on");
    digitalWrite(ledpin,HIGH);//点亮数字13 口LED。  
    //delay(500);  
  }  
  if(val == 'C')
  {
      Serial.println("turn off");
      digitalWrite(ledpin,LOW);//熄灭数字13 口LED。
  }
}
