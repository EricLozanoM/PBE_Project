from rpi_lcd import LCD
import time
import sys

lcd = LCD()
inputlist = sys.stdin.readlines()
msg = [x.strip() for x in inputlist]
lcd.text_multilinia(msg)




	



