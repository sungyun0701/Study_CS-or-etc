import I2C_LCD_driver
from time import *
mylcd = I2C_LCD_driver.lcd()
mylcd.lcd_display_string("Hello World",1)

mylcd.lcd_display_string("안녕하세요",2)
sleep(1)

mylcd.lcd_clear()

mylcd.lcd_display_string("This is how you", 1)
mylcd.lcd_display_string(" Hello World!", 2, 3)
sleep(1)

mylcd.lcd_clear()

mylcd.lcd_display_string("clear the screen", 1)
sleep(1)

mylcd.lcd_clear()

str_pad =  " " * 16
my_long_string = "This is a string that needs to scroll"
my_long_string = str_pad + my_long_string

for i in range (0, len(my_long_string)):
    lcd_text = my_long_string[i:(i+16)]
    mylcd.lcd_display_string(lcd_text,1)
    sleep(0.4)
    mylcd.lcd_display_string(str_pad,1)