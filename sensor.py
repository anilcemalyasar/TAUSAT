import random
import time
# import serial
import  csv
import datetime

# ser = serial.Serial('COM3', 115200)
# ser.flushInput()



global roll
global pitch
global yaw
global temperature
global pressure

global yükseklik_1
global yükseklik_2
global irtifa_farkı
global raw_msg

takim_no = 31715


fields = ["no", "yaw" , "pitch", "roll" , "temperature" , "time"]





def dumbPressure():

    while True:
        return random.uniform(0,400)


def getPressure():
    pressure = dumbPressure()
    return pressure


def getYAW():
    return yaw


def getPITCH():
    return pitch

def getROLL():
    return roll


def getTemp():
    return temperature


def getYükseklik_1():
    return random.uniform(0,700)

def getYükseklik_2():
    return random.uniform(0,700)


def getIrtifa_farkı():
    irtifa_farkı = abs(getYükseklik_2() - getYükseklik_1())
    return irtifa_farkı


with open("test_data_1.csv", "a", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(fields)




    while True:
        try:
            #ser_bytes = ser.readline()
            # decoded_bytes = ser_bytes.decode("utf-8").lstrip('b').rstrip('\r\n')
            #print(decoded_bytes)
            #raw_msg = decoded_bytes.rsplit("|")
            tel = ",".join(raw_msg)
            tm = datetime.datetime.now()
            raw_msg.append(tm)
            raw_msg.insert(0, takim_no)


            writer.writerow(raw_msg)

            #roll = raw_msg[0]
            #pitch = raw_msg[1]
            #yaw = raw_msg[2]
            #temperature = raw_msg[3]
        except:
            print("Keyboard Interrupt")
            break