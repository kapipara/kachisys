#! /usr/bin/env python3
#! coding:utf-8

'''
電気スイッチカチカチ君 for Procon Room < kachi-sys >
made by kapipara 2018

Release Note:
    ver1.00: make this program. (2018/05/08)
    ver1.01: change gpio pin. (2018/05/10)
    ver2.00: change curcuit. and use inverter for LED. (2018/05/23)
'''

import RPi.GPIO as GPIO
import pigpio
from time import sleep

# ALL BCM number
# インジケータLEDピン
# HIGH = RedLED, LOW = GreenLED
led1 =  5  # GPIO number = 21
led2 =  6  #             = 22
led3 = 13  #             = 23
led4 = 19  #             = 24

# 切替スイッチピン
sw1 = 18   # GPIO number =  1
sw2 = 23   #             =  4
sw3 = 24   #             =  5
sw4 = 25   #             =  6
sw5 = 21   #             = 29

# サーボモータピン(Soft PWM)
sv1 =  3   # GPIO number = 5
sv2 =  4   #             = 7
sv3 = 16   #             = 36
sv4 = 12   #             = 32
# サーボモータ回転パルス定義
# SG90は50Hz駆動で20msあるが，駆動パルス範囲は0.5-2.4msとなっている
# なので2.5-12.0%のデューティ比で動作
# PiGPIOではHIGHレベルの秒数[us]を引数として渡すことでサーボモータを制御する
# 550us-2400us程度で0-180度
# 各値は実測値なのでいじらないでね
sv1_on  =  950
sv1_off = 1750
sv2_on  = 1050
sv2_off = 1750
sv3_on  = 1700
sv3_off = 1100
sv4_on  = 1700
sv4_off = 1000
sv_avoid = 1400     # サーボ退避用

# スイッチ用flag
# True: SWはON / False: SWはOFF
sw1flag = False
sw2flag = False
sw3flag = False
sw4flag = False
sw5flag = False

# GPIO初期化
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)    # GPIO使用中エラーがうるさいので黙らせる 無視して上書きすれば動く
pi = pigpio.pi()
# GPIOを出力モードに設定(LED)
GPIO.setup(led1, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(led2, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(led3, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(led4, GPIO.OUT, initial=GPIO.HIGH)
# GPIOをプルアップ入力に設定(switch)
GPIO.setup(sw1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(sw5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# サーボを平行位置に退避
pi.set_servo_pulsewidth(sv1, sv_avoid)
pi.set_servo_pulsewidth(sv2, sv_avoid)
pi.set_servo_pulsewidth(sv3, sv_avoid)
pi.set_servo_pulsewidth(sv4, sv_avoid)

# LEDとサーボの動作処理本体
def sw1Callback(pin):
    global sw1flag                                  # swflagがグローバルなのを教える
    sw1flag = not sw1flag                           # 現在の状態から変える(バグらなければON/OFFちゃんとしてくれる)
    if not sw1flag:                                 # LOWなら(スイッチがONなら)
        GPIO.output(led1, GPIO.LOW)                     # HIGHにする(スイッチをOFF)
        pi.set_servo_pulsewidth(sv1, sv1_off)           # servoをOFFの角度に回す
        sleep(0.1)
        pi.set_PWM_dutycycle(sv1, 0)
        print("switch1 to OFF OK.\n")
    elif sw1flag:                                   # HIGHなら(スイッチがOFFなら)
        GPIO.output(led1, GPIO.HIGH)                    # LOWにする(スイッチをON)
        pi.set_servo_pulsewidth(sv1, sv1_on)            # servoをONの角度に回す
        sleep(0.1)
        pi.set_PWM_dutycycle(sv1, 0)
        print("switch1 to ON OK.\n")
    else:                                           # なんかエラったら
        print("oh! you're noob!")                       # ユーザを煽る

def sw2Callback(pin):
    global sw2flag                                  # swflagがグローバルなのを教える
    sw2flag = not sw2flag                           # 現在の状態から変える(バグらなければON/OFFちゃんとしてくれる)
    if not sw2flag:                                 # LOWなら(スイッチがONなら)
        GPIO.output(led2, GPIO.LOW)                     # HIGHにする(スイッチをOFF)
        pi.set_servo_pulsewidth(sv2, sv2_off)           # servoをOFFの角度に回す
        sleep(0.1)
        pi.set_PWM_dutycycle(sv2, 0)
        print("switch2 to OFF OK.\n")
    elif sw2flag:                                   # HIGHなら(スイッチがOFFなら)
        GPIO.output(led2, GPIO.HIGH)                    # LOWにする(スイッチをON)
        pi.set_servo_pulsewidth(sv2, sv2_on)            # servoをONの角度に回す
        sleep(0.1)
        pi.set_PWM_dutycycle(sv2, 0)
        print("switch2 to ON OK.\n")
    else:                                           # なんかエラったら
        print("oh! you're noob!")                       # ユーザを煽る

def sw3Callback(pin):
    global sw3flag                                  # swflagがグローバルなのを教える
    sw3flag = not sw3flag                           # 現在の状態から変える(バグらなければON/OFFちゃんとしてくれる)
    if not sw3flag:                                 # LOWなら(スイッチがONなら)
        GPIO.output(led3, GPIO.LOW)                     # HIGHにする(スイッチをOFF)
        pi.set_servo_pulsewidth(sv3, sv3_off)           # servoをOFFの角度に回す
        sleep(0.1)
        pi.set_PWM_dutycycle(sv3, 0)
        print("switch3 to OFF OK.\n")
    elif sw3flag:                                   # HIGHなら(スイッチがOFFなら)
        GPIO.output(led3, GPIO.HIGH)                    # LOWにする(スイッチをON)
        pi.set_servo_pulsewidth(sv3, sv3_on)            # servoをONの角度に回す
        sleep(0.1)
        pi.set_PWM_dutycycle(sv3, 0)
        print("switch3 to ON OK.\n")
    else:                                           # なんかエラったら
        print("oh! you're noob!")                       # ユーザを煽る

def sw4Callback(pin):
    global sw4flag                                  # swflagがグローバルなのを教える
    sw4flag = not sw4flag                           # 現在の状態から変える(バグらなければON/OFFちゃんとしてくれる)
    if not sw4flag:                                 # LOWなら(スイッチがONなら)
        GPIO.output(led4, GPIO.LOW)                     # HIGHにする(スイッチをOFF)
        pi.set_servo_pulsewidth(sv4, sv4_off)           # servoをOFFの角度に回す
        sleep(0.1)
        pi.set_PWM_dutycycle(sv4, 0)
        print("switch4 to OFF OK.\n")
    elif sw4flag:                                   # HIGHなら(スイッチがOFFなら)
        GPIO.output(led4, GPIO.HIGH)                    # LOWにする(スイッチをON)
        pi.set_servo_pulsewidth(sv4, sv4_on)            # servoをONの角度に回す
        sleep(0.1)
        pi.set_PWM_dutycycle(sv4, 0)
        print("switch4 to ON OK.\n")
    else:                                           # なんかエラったら
        print("oh! you're noob!")                       # ユーザを煽る

def sw5Callback(pin):
    global sw1flag
    global sw2flag
    global sw3flag
    global sw4flag
    global sw5flag
    sw5flag = not sw5flag
    sw1flag = sw5flag
    sw2flag = sw5flag
    sw3flag = sw5flag
    sw4flag = sw5flag
    if not sw5flag:
        GPIO.output(led1, GPIO.LOW)
        GPIO.output(led2, GPIO.LOW)
        GPIO.output(led3, GPIO.LOW)
        GPIO.output(led4, GPIO.LOW)
        pi.set_servo_pulsewidth(sv1, sv1_off)
        sleep(0.1)
        pi.set_PWM_dutycycle(sv1, 0)
        pi.set_servo_pulsewidth(sv2, sv2_off)
        sleep(0.1)
        pi.set_PWM_dutycycle(sv2, 0)
        pi.set_servo_pulsewidth(sv3, sv3_off)
        sleep(0.1)
        pi.set_PWM_dutycycle(sv3, 0)
        pi.set_servo_pulsewidth(sv4, sv4_off)
        sleep(0.1)
        pi.set_PWM_dutycycle(sv4, 0)
        print("ALL switches to OFF OK.\n")
    elif sw5flag:
        GPIO.output(led1, GPIO.HIGH)
        GPIO.output(led2, GPIO.HIGH)
        GPIO.output(led3, GPIO.HIGH)
        GPIO.output(led4, GPIO.HIGH)
        pi.set_servo_pulsewidth(sv1, sv1_on)
        sleep(0.1)
        pi.set_PWM_dutycycle(sv1, 0)
        pi.set_servo_pulsewidth(sv2, sv2_on) 
        sleep(0.1)
        pi.set_PWM_dutycycle(sv2, 0)
        pi.set_servo_pulsewidth(sv3, sv3_on) 
        sleep(0.1)
        pi.set_PWM_dutycycle(sv3, 0)
        pi.set_servo_pulsewidth(sv4, sv4_on) 
        sleep(0.1)
        pi.set_PWM_dutycycle(sv4, 0)
        print("ALL switches to ON OK.\n")
    else:
        print("Oh! you're noob!")

# スイッチの割込処理と，割込後の無応答時間の設定
GPIO.add_event_detect(sw1, GPIO.RISING, callback=sw1Callback, bouncetime=1000)
GPIO.add_event_detect(sw2, GPIO.RISING, callback=sw2Callback, bouncetime=1000)
GPIO.add_event_detect(sw3, GPIO.RISING, callback=sw3Callback, bouncetime=1000)
GPIO.add_event_detect(sw4, GPIO.RISING, callback=sw4Callback, bouncetime=1000)
GPIO.add_event_detect(sw5, GPIO.RISING, callback=sw5Callback, bouncetime=3000)

def initialize():
    for i in range(3):
        GPIO.output(led1, GPIO.LOW)
        GPIO.output(led2, GPIO.LOW)
        sleep(0.5)
        GPIO.output(led3, GPIO.LOW)
        GPIO.output(led4, GPIO.LOW)
        GPIO.output(led1, GPIO.HIGH)
        GPIO.output(led2, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(led3, GPIO.HIGH)
        GPIO.output(led4, GPIO.HIGH)

    print("initializing.....OK!")


try:
    initialize()
    while True:
        sleep(0.01)
except KeyboardInterrupt:
    GPIO.cleanup()
