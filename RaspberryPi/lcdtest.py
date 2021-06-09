import RPi_I2C_driver
from time import *




text1=[
    0B00100,
    0B11111,
    0B01110,
    0B10001,
    0B10001,
    0B01110,
    0B00100,
    0B11111
        ]
text2=[
    0B01000,
    0B01000,
    0B01000,
    0B01000,
    0B01000,
    0B01111,
    0B01000,
    0B01000
        ]
text3=[
    0B00000,
    0B01110,
    0B10001,
    0B10001,
    0B10001,
    0B01110,
    0B00000,
    0B00000
        ]
text4=[
    0B00000,
    0B00100,
    0B00100,
    0B01010,
    0B01010,
    0B10001,
    0B10001,
    0B00000
        ]
text5=[
    0B00100,
    0B00100,
    0B00100,
    0B00100,
    0B11100,
    0B00100,
    0B00100,
    0B00100
        ]
text6=[
    0B00000,
    0B11111,
    0B01010,
    0B01010,
    0B10000,
    0B10000,
    0B10000,
    0B11111
        ]
text7=[
    0B00000,
    0B00000,
    0B00000,
    0B00000,
    0B00000,
    0B00000,
    0B00000,
    0B00000
    ]

lcd = RPi_I2C_driver.lcd(0x27)



lcd.createChar(0, text1)
lcd.createChar(1, text2)
lcd.createChar(2, text3)
lcd.createChar(3, text4)
lcd.createChar(4, text5)
lcd.createChar(5, text6)
lcd.createChar(6, text7)


lcd.setCursor(0,0)
lcd.write(0)
lcd.write(1)
lcd.write(6)
lcd.write(3)
lcd.write(4)
lcd.write(6)
lcd.write(2)

lcd.setCursor(0,1)
lcd.write(6)
lcd.write(2)
lcd.write(6)
lcd.write(6)
lcd.write(2)
lcd.write(6)
lcd.write(5)




sleep(2)

