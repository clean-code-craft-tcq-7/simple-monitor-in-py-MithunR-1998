
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

def vitals_ok(temperature, pulseRate, spo2):
  if temperature > 102 or temperature < 95:
    Print_Output('Temperature critical!')
  if pulseRate < 60 or pulseRate > 100:
    Print_Output('Pulse Rate is out of range!')
  if spo2 < 90:
    Print_Output('Oxygen Saturation out of range!')
#vitals_ok(110,50,80)
