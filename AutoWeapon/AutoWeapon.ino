#include <LiquidCrystal.h>

String x_servo_angle;
String y_servo_angle;

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup()
{
  Serial.begin(9600);
  lcd.begin(16, 2);
}

void loop()
{
  if (Serial.available() > 0)
  {    
    lcd.clear();
    x_servo_angle = "";
    y_servo_angle = "";
    String a = Serial.readString();
    //lcd.print(a);
    int index_comma = (a.indexOf(','));
    for (int i = 0; i < index_comma; i++)
    {
      x_servo_angle += a[i];
    }
    for (int i = index_comma + 1; i < a.length(); i++)      
    {
      y_servo_angle += a[i];
    }

    lcd.print("X Servo: " + x_servo_angle);
    lcd.setCursor(0,1);
    lcd.print("Y Servo: " + y_servo_angle);
  }
}
