# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import serial 
import numpy
import matplotlib.pyplot as plt
from drawnow import *

current0=[]
current1=[]
arduinoData = serial.Serial('com3',9600)
plt.ion()
cnt=0

def makeFig():
    plt.ylim(500,1000)
    plt.title('My current meter')
    plt.grid(True)
    plt.ylabel('Current of port 0 (mA)')
    plt.plot(current0, 'ro-', label='Port 0')
    plt.legend(loc='upper left')
    plt2=plt.twinx()
    plt2.set_ylim(500,900)
    plt2.plot(current1, 'b^-', label='Port 1')
    plt2.set_ylabel('Current of port 1 (mA)')
    plt2.legend(loc='upper right')
    
while True:
    while (arduinoData.inWaiting()==0):
        pass
    arduinoString = arduinoData.readline()
    dataArray = arduinoString.decode().split(',')
    crnt0 = float(dataArray[0])
    crnt1 = float(dataArray[1])
    current0.append(crnt0)
    current1.append(crnt1)
    drawnow(makeFig)
    plt.pause(.000001)
    cnt=cnt+1
    if(cnt>50):
        current0.pop(0)
        current1.pop(1)