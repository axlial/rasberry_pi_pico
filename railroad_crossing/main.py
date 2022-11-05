from machine import Pin
from time import sleep

###Сигнализация
SIGNALING = Pin(27, Pin.OUT)

#Кнопка
BUTTON = Pin(18, Pin.IN, Pin.PULL_UP)

###Светофор A
GREEN = Pin(3, Pin.OUT)
YELLOW = Pin(4, Pin.OUT)
RED = Pin(5, Pin.OUT)
LED = Pin(25, Pin.OUT)

#Светофор B
GREEN_B = Pin(11, Pin.OUT)
YELLOW_B = Pin(12, Pin.OUT)
RED_B = Pin(13, Pin.OUT)

def start_signaling():
    '''Включаем сигнализацию'''
    print('Включаем сигнализацию')
    SIGNALING.high()
    
def stop_signaling():
    '''Выключаем сигнализацию'''
    print('Выключаем сигнализацию')
    SIGNALING.low()

def green_trafficlight():
    '''Включаем зеленый свет'''
    print('Включаем зеленый свет')
    GREEN.high()
    YELLOW.low()
    RED.low()
    GREEN_B.high()
    YELLOW_B.low()
    RED_B.low()

def yellow_trafficlight():
    '''Включаем желтый свет'''
    print('Включаем желтый свет')
    GREEN.low()
    YELLOW.high()
    RED.low()
    GREEN_B.low()
    YELLOW_B.high()
    RED_B.low()

def red_trafficlight():
    '''Включаем красный свет'''
    print('Включаем красный свет')
    GREEN.low()
    YELLOW.low()
    RED.high()
    GREEN_B.low()
    YELLOW_B.low()
    RED_B.high()
    
def stop_trafficlight():
    '''Выключаем светофор'''
    print('Выключаем светофор')
    GREEN.low()
    YELLOW.low()
    RED.low()
    GREEN_B.low()
    YELLOW_B.low()
    RED_B.low()
    
###Шлагбаум А
#Присваиваем входам номера пинов
IN3 = Pin(16, Pin.OUT)
IN4 = Pin(17, Pin.OUT)

###Шлагбаум B
#Присваиваем входам номера пинов
IN1 = Pin(14, Pin.OUT)
IN2 = Pin(15, Pin.OUT)

def barrier_up():
    '''Поднимаем шлагбаум'''
    IN1.high()
    IN2.low()
    sleep(1)
    IN1.low()
    IN2.low()
    sleep(1)
    IN3.high()
    IN4.low()
    sleep(1)
    IN3.low()
    IN4.low()
    print('Поднимаем шлагбаум')
    sleep(.5)

def barrier_down():
    '''Опускаем шлагбаум'''
    IN1.low()
    IN2.high()
    sleep(1)
    IN1.low()
    IN2.low()
    sleep(1)
    IN3.low()
    IN4.high()
    sleep(1)
    IN3.low()
    IN4.low()
    print('Опускаем шлагбаум')
    sleep(.5)

def barrier_stop(seconds=60):
    '''Останаливаем работу шлагбаума'''
    IN1.low()
    IN2.low()
    IN3.low()
    IN4.low()
    print('Останавливаем шлагбаум')
    sleep(seconds)

if __name__ == '__main__':
    while True:
        if BUTTON.value() == 0:
            if RED.value() == 0:
                #Переключаем на желтый сигнал светофора
                yellow_trafficlight()
                sleep(2)
                #Включаем красный сигнал светофора
                red_trafficlight()
            elif RED.value() == 1:
                continue
            #Включаем сигнализацию
            start_signaling()
            #Опускаем шлагбаум
            barrier_down()
            barrier_stop(2)
            x = 0
            while x <= 100:
                RED.low()
                RED_B.low()
                sleep(.5)
                RED.high()
                RED_B.high()
                sleep(.5)
                x += 1
        if BUTTON.value() == 1:
            if GREEN.value() == 0:
                #Переключаем на желтый сигнал светофора
                yellow_trafficlight()
                sleep(2)
                #Включаем зеленый сигнал светфора
                green_trafficlight()
                sleep(2)
            elif GREEN.value() == 1:    
                continue
            #Выключаем сигнализацию
            stop_signaling()
            #Поднимаем шлагбаум
            barrier_up()
            barrier_stop(2)