#!/usr/bin/python3
"""
reTerminal user button "o" -> shutdown
$ sudo pip3 install seeed-python-reterminal
"""
import os
import seeed_python_reterminal.core as rt
import seeed_python_reterminal.button as rt_btn
device = rt.get_button_device()
while 1:
  for event in device.read_loop():
    buttonEvent = rt_btn.ButtonEvent(event)
    if buttonEvent.name ==  rt_btn.ButtonName.O:
    #if buttonEvent.name ==  rt_btn.ButtonName.F1:
      os.system("sudo shutdown -h now")

