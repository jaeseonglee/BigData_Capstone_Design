# 애플리케이션에서 사료 공급을 작동시키는 코드

import RPi.GPIO as GPIO         # GPIO 모듈
import time                     # time 모듈

m  = 16                         # 사용하는 pin 번호 16

GPIO.setmode(GPIO.BOARD)        # BOARD 기준
GPIO.setup(m, GPIO.OUT)         # 출력으로 설정

pwm1 = GPIO.PWM(m, 50)          # 50Hz로 설정
pwm1.start(7)                   # 7의 위치에서 시작
time.sleep(1)

pwm1.ChangeDutyCycle(11)      # 모터가 동작하면서 사료통의 입구 개폐
time.sleep(3)

pwm1.ChangeDutyCycle(7)
time.sleep(3)

pwm1.stop()                     # 작동이 끝나면 stop을 통해 해제

GPIO.cleanup(m)                 # 동작이 끝나면 cleanup
