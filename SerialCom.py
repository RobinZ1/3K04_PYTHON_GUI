

import tkinter as tk
import tkinter.messagebox
import os
import serial
from serial.tools import list_ports

from struct import *
import time,threading
from math import np



global Sercom
global ports
global Parameters
Parameters = [0x16,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

Sercom = serial.Serial()
paradata = 'para_data.txt'
def connect():
    
    ports = list(list_ports.comports())
    Sercom = serial.Serial('COM3',115200)
    Sercom.port = ports[0].device
    #Sercom.open()
    device = tk.Tk();
    device.title("Device")
    device.geometry('300x200')
    device,mainloop()
    tk.Label(device, text="Device name:",fg='blue').place(x=10, y = 70)
        
    tk.Label(device, text=ports[0].device).place(x=120, y = 70)
    
    tk.Label(device, text="Description:",fg='blue').place(x=10, y =110)
    
    tk.Label(device, text=ports[0].description).place(x=120, y = 110)
    
    tk.Label(device, text="Manufacturer",fg='blue').place(x=10, y = 150)
    
    tk.Label(device, text=ports[0].manufacturer).place(x=120, y = 150)

    if Sercom.is_open:
        tkinter.messagebox.showinfo(title="Device Connection", message="The Device is connected")
        
    else:
        tkinter.messagebox.showerror("Device Connection", "The Device is not connected")



""" def checkDeviceInfo():
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
        tkinter.messagebox.showerror("System Message", "The device is not connected") """


def disconnect():
    Sercom.close()





def storePara(LRL,URL,MSR,FAVD,AA,VA,APW,VPW,ARP,VRP,AT,RT,RF,RecT,Mode):
    Parameters[0] = 1
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
    """ Parameters.append(0x16)
    Parameters.append(LRL)
    Parameters.append(URL)
    Parameters.append(MSR)
    Parameters.append(FAVD)
    Parameters.append(AA)
    Parameters.append(VA)
    Parameters.append(APW)
    Parameters.append(VPW)
    Parameters.append(ARP)
    Parameters.append(VRP)
    Parameters.append(AT)
    Parameters.append(RT)
    Parameters.append(RF)
    Parameters.append(RecT)
    Parameters.append(Mode) """

    
    f = open(paradata,'w')
    for i in range(0,16):
        f.write(str(Parameters[i]))
        f.write('\n')
    f.close()



def transferPara():
    bytePara = bytes(Parameters)
    print(bytePara)
    #Sercom.write(bytePara)

#connect()
storePara(50,100,101,120,103,40,60,70,80,102,100,200,200,100,1)
transferPara()