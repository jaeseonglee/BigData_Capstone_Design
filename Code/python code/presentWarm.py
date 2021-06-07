# 애플리케이션의 열선 ON/OFF를 알려주는 코드

import RPi.GPIO as GPIO         # GPIO 모듈

GPIO.setmode(GPIO.BOARD)        # BOARD 기준 pin 번호
GPIO.setup(12, GPIO.OUT)        # 출력으로 설정

value = int(GPIO.input(12))     # GPIO.input을 통해 출력 pin의 상태값을 확인
                                # HIGH -> 1 , LOW -> 0

if value == 1:                  # HIGH, 즉 온열매트가 작동중이면 
    print("ON")                 # ON을 출력
else:                           # 작동중이 아니면 
    print("OFF")                # OFF를 출력

GPIO.cleanup()                  # 출력이 끝나면 cleanup