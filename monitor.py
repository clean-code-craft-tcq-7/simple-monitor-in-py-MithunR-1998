
from time import sleep
import sys

def Print_Output(Message):
  print(Message)
  for i in range(6):
    print('\r* ', end='')
    sys.stdout.flush()
    sleep(1)
    print('\r *', end='')
    sys.stdout.flush()
    sleep(1)

def temp_check(temperature):
  if temperature > 102 or temperature < 95:
    Print_Output('Temperature critical!')
    return False
   return True 

def pulse_check(pulseRate):
  if pulseRate < 60 or pulseRate > 100:
    Print_Output('Pulse Rate is out of range!')
    return False
  return True  

def spo2_check(spo2):
  if spo2 < 90:
    Print_Output('Oxygen Saturation out of range!')
    return False
  return True 

def vitals_ok(temperature, pulseRate, spo2):
  if temp_check(temperature) and pulse_check(pulseRate) and spo2_check(spo2):
    return True
  return False
#vitals_ok(110,50,80)
