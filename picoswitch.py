from machine import Pin
import time

ledA = Pin(18, Pin.OUT)
ledB = Pin(19, Pin.OUT)
ledC = Pin(13, Pin.OUT)
ledD = Pin(14, Pin.OUT)
ledE = Pin(15, Pin.OUT)
ledF = Pin(17, Pin.OUT)
ledG = Pin(16, Pin.OUT)
ledDp = Pin(12, Pin.OUT)

dip0 = Pin(6, Pin.IN, Pin.PULL_DOWN)
dip1 = Pin(7, Pin.IN, Pin.PULL_DOWN)
dip2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
dip3 = Pin(9, Pin.IN, Pin.PULL_DOWN)

def clearLEDs():
    ledA.value(1)
    ledB.value(1)
    ledC.value(1)
    ledD.value(1)
    ledE.value(1)
    ledF.value(1)
    ledG.value(1)
    ledDp.value(1)
    
def display1():
    clearLEDs()
    ledB.value(0)
    ledC.value(0)

def display2():
    clearLEDs()
    ledA.value(0)
    ledB.value(0)
    ledD.value(0)
    ledE.value(0)
    ledG.value(0)
    
def display3():
    clearLEDs()
    ledA.value(0)
    ledB.value(0)
    ledC.value(0)
    ledD.value(0)
    ledG.value(0)
    
def display4():
    clearLEDs()
    ledB.value(0)
    ledC.value(0)
    ledG.value(0)
    ledF.value(0)
    
def display5():
    clearLEDs()
    ledA.value(0)
    ledC.value(0)
    ledD.value(0)
    ledG.value(0)
    ledF.value(0)


def display6():
    clearLEDs()
    ledA.value(0)
    ledC.value(0)
    ledD.value(0)
    ledE.value(0)
    ledF.value(0)
    ledG.value(0)
    
def display7():
    clearLEDs()
    ledA.value(0)
    ledB.value(0)
    ledC.value(0)
    
def display8():
    clearLEDs()
    ledA.value(0)
    ledB.value(0)
    ledC.value(0)
    ledD.value(0)
    ledE.value(0)
    ledF.value(0)
    ledG.value(0)
    
def display9():
    clearLEDs()
    ledA.value(0)
    ledB.value(0)
    ledC.value(0)
    ledD.value(0)
    ledF.value(0)
    ledG.value(0)
    
def display0():
    clearLEDs()
    ledA.value(0)
    ledB.value(0)
    ledC.value(0)
    ledD.value(0)
    ledE.value(0)
    ledF.value(0)
    
def displayA():
    clearLEDs()
    ledA.value(0)
    ledB.value(0)
    ledC.value(0)
    ledE.value(0)
    ledF.value(0)
    ledG.value(0)
    
def displayB():
    clearLEDs()
    ledC.value(0)
    ledD.value(0)
    ledE.value(0)
    ledF.value(0)
    ledG.value(0)
    
def displayC():
    clearLEDs()
    ledA.value(0)
    ledD.value(0)
    ledE.value(0)
    ledF.value(0)
    
def displayD():
    clearLEDs()
    ledB.value(0)
    ledC.value(0)
    ledD.value(0)
    ledE.value(0)
    ledG.value(0)
    
def displayE():
    clearLEDs()
    ledA.value(0)
    ledD.value(0)
    ledE.value(0)
    ledF.value(0)
    ledG.value(0)
    
def displayF():
    clearLEDs()
    ledA.value(0)
    ledE.value(0)
    ledF.value(0)
    ledG.value(0)

    


while (True):
    displayVal = 0;
    if dip3.value():
        displayVal = displayVal + 8
    if dip2.value():
        displayVal = displayVal + 4
    if dip1.value():
        displayVal = displayVal + 2
    if dip0.value():
        displayVal = displayVal + 1
        
    if displayVal == 0:
        display0()
    elif displayVal == 1:
        display1()
    elif displayVal == 2:
        display2()
    elif displayVal == 3:
        display3()
    elif displayVal == 4:
        display4()
    elif displayVal == 5:
        display5()
    elif displayVal == 6:
        display6()
    elif displayVal == 7:
        display7()
    elif displayVal == 8:
        display8()
    elif displayVal == 9:
        display9()
    elif displayVal == 10:
        displayA()
    elif displayVal == 11:
        displayB()
    elif displayVal == 12:
        displayC()
    elif displayVal == 13:
        displayD()
    elif displayVal == 14:
        displayE()
    elif displayVal == 15:
        displayF()        
    time.sleep(1)