# 정해진 시간에 사료와 물을 동시에 공급하는 코드

from multiprocessing import Process         # 멀티 스레딩을 위한 Process 모듈
import datetime as dt                       # 현재 시간을 얻기위한 datetime
import time                                 # time 모듈
import RPi.GPIO as GPIO                     # GPIO 모듈

def feed():                                 # 서보모터를 작동시키는 feed 함수
    motorPin = 16                           # 서보 모터의 핀 번호 16
    GPIO.setup(motorPin, GPIO.OUT)          # 출력으로 설정 
    
    motor = GPIO.PWM(motorPin,50)           # 50Hz로 설정
    motor.start(7)                          # 7의 위치에서 시작
    
    motor.ChangeDutyCycle(11)               # 모터가 동작하면서 사료통의 입구 개폐 
    time.sleep(2)

    motor.ChangeDutyCycle(7)

    motor.stop()                            # 작동이 끝나면 stop을 통해 해제
    

def water():                                # 워터 펌프를 작동시키는 water 함수
    pumpPin = 12                            # 워터 펌프의 핀 번호 12

    GPIO.setup(pumpPin, GPIO.OUT)           # 출력으로 설정
    GPIO.output(pumpPin, GPIO.LOW)          # LOW 상태에서 시작
    
    GPIO.output(pumpPin, GPIO.HIGH)         # HIGHT로 설정하여 워터 펌프 동작
    time.sleep(3)                           # 해당 코드에서는 3초 동안 동작
    GPIO.output(pumpPin, GPIO.LOW)          # 공급이 끝나면 다시 LOW로 설정
    

if __name__ == "__main__":                  # main 코드
    feedProcess = Process(target = feed)    # 사료 공급 함수 feed 함수에 대한 스레딩 설정
    waterProcess = Process(target = water)  # 물 공급 함수 water 함수에 대한 스레딩 설정
    
    while True :                            # 무한 반복문을 통해 정해진 시간 마다 사료와 물 공급
        GPIO.setmode(GPIO.BOARD)            # GPIO 사용은 BOARD 기준으로 설정
        t = dt.datetime.now()               # 현재 시간을 dt.datetime.now() 를 통해 얻고 
        h = t.hour                          # 그 중 현재 시간(hour)와
        m = t.minute                        # 현재 분(minute)을 얻는다.

        if m == 0 :                         # 매 정각마다 확인한다.
            if h == 8 or h == 12 or h == 18 :   # 현재 코드는 8시, 12시 , 18시 정각마다 사료와 물을 공급
                feedProcess.start()         # 멀티 스레딩을 구현함으로 동시에 작동하도록 설정
                waterProcess.start()
                
                feedProcess.join()          # join을 통해 각 함수 동작
                waterProcess.join()
        else :
            sleepMinute = 60 - m            # 정각이 아니라면
            time.sleep(sleepMinute * 60)    # 다음 정각까지의 시간을 구하여 time.sleep 한다.
    