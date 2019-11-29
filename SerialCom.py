

import tkinter as tk
import tkinter.messagebox
import os
import serial
from serial.tools import list_ports
import matplotlib.animation as animation
from matplotlib import style
from struct import *
import time,threading
import json



global Sercom
global ports
global Parameters

Sercom = serial.Serial()
paradata = 'para_data.txt'
def connect():
    
    ports = list(list_ports.comports())
    Sercom = serial.Serial('COM4',115200)
    Sercom.port = ports[0].device
    Sercom.open()
    if Sercom.is_open:
        tkinter.messagebox.showinfo("Device Connection", "The Device is connected")
    else:
        tkinter.messagebox.showerror("Device Connection", "The Device is not connected")



def checkDeviceInfo():
    if(Sercom.is_open):
        device = tk.Tk();
        device.title("Device")
        tk.Label(device, text="Device name:",fg='blue',anchor='center')
        tk.grid(row=1,column=1)
        tk.Label(device, text=ports[0].device,anchor='center')
        tk.grid(row=1,column=2)
        tk.Label(device, text="Description:",fg='blue',anchor='center')
        tk.grid(row=2,column=1)
        tk.Label(device, text=ports[0].description,anchor='center')
        tk.grid(row=2,column=2)
        tk.Label(device, text="Manufacturer",fg='blue',anchor='center')
        tk.grid(row=3,column=1)
        tk.Label(device, text=ports[0].manufacturer,anchor='center')
        tk.grid(row=3,column=2)
    else:
        tkinter.messagebox.showerror("System Message", "The device is not connected")


def disconnect():
    Sercom.close()





def storePara(LRL,URL,MSR,FAVD,AA,VA,APW,VPW,ARP,VRP,AT,RT,RF,RecT,Mode):
    Parameters[0] = "0X16"
    Parameters[1] = LRL
    Parameters[2] = URL
    Parameters[3] = MSR
    Parameters[4] = FAVD
    Parameters[5] = AA
    Parameters[6] = VA
    Parameters[7] = APW
    Parameters[8] = VPW
    Parameters[9] = ARP
    Parameters[10] = VRP
    Parameters[11] = AT
    Parameters[12] = RT
    Parameters[13] = RF
    Parameters[14] = RecT
    Parameters[15] = Mode

    
    f = open(paradata,'w')
    for i in Parameters:
        f.write(str(Parameters[i]))
        f.write('\n')
    f.close()



def transferPara():
    bytePara = bytes(Parameters)
    Sercom.write(bytePara)
