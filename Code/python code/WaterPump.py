# 애플리케이션에서 물 공급을 작동시키는 코드

import RPi.GPIO as GPIO         # GPIO 모듈
import time                     # time 모듈

w = 12                          # 사용하는 pin 번호 12

GPIO.setmode(GPIO.BOARD)        # BOARD 기준
GPIO.setup(w, GPIO.OUT)         # 출력으로 설정
GPIO.output(w, GPIO.LOW)        # LOW 상태에서 시작
time.sleep(1)               

GPIO.output(w , GPIO.HIGH)      # HIGH로 설정하여 워터펌프 동작
time.sleep(3)                   # 해당 코드에서는 3초 동안 동작

GPIO.output(w, GPIO.LOW)        # 공급이 끝나면 다시 LOW로 설정

GPIO.cleanup()                  # 동작이 끝나면 cleanup
