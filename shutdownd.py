#!/usr/bin/python3

import os
import seeed_python_reterminal.core as rt
import seeed_python_reterminal.button as rt_btn
device = rt.get_button_device()

def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
	
while 1:
  for event in device.read_loop():
    buttonEvent = rt_btn.ButtonEvent(event)
    if buttonEvent.name ==  rt_btn.ButtonName.O:
    #if buttonEvent.name ==  rt_btn.ButtonName.F1:
      os.system("sudo shutdown -h now")
    elif buttonEvent.name ==  rt_btn.ButtonName.F1:
      os.system("/home/pi/Documents/arduino-1.8.19/arduino")
    # lightSense = rt.illuminance
    # if lightSense != 0:
      
