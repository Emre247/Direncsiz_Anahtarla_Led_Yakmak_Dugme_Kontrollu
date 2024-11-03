from time import sleep
import RPi.GPIO as GPIO
GPIO.cleanup()
bekleme=1
girisPin=40
cikisPin=38
GPIO.setmode(GPIO.BOARD)
GPIO.setup(cikisPin,GPIO.OUT)
GPIO.setup(girisPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
LedDurum=0
dugmeDurum=0
dugmeDurumEski=1
try:
    while True:
        dugmeDurum=GPIO.input(cikisPin)
        print(dugmeDurum)
        if dugmeDurum==1 and dugmeDurumEski==0:
            LedDurum = not LedDurum
            GPIO.output(cikisPin,LedDurum)
        dugmeDurumEski=dugmeDurum
        sleep(bekleme)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Başarılı bir şekilde program kapatıldı")