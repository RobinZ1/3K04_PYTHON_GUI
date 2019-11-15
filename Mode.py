import tkinter as tk
import tkinter.messagebox
import pickle
import json



global AOO_LRL1
AOO_LRL1 = -1
AOO_LRL = tk.IntVar()

global AOO_URL1
AOO_URL1 = -1
AOO_URL = tk.IntVar()

global AOO_AA1
AOO_AA1 = -1
AOO_AA = tk.DoubleVar()

global AOO_APW1
AOO_APW1 = -1
AOO_APW = tk.DoubleVar()

#VOO
global VOO_LRL1
VOO_LRL1 = -1
VOO_LRL = tk.IntVar()

global VOO_URL1
VOO_URL1 = -1
VOO_URL = tk.IntVar()

global VOO_VA1
VOO_VA1 = -1
VOO_VA = tk.DoubleVar()

global VOO_VPW1
VOO_VPW1 = -1
VOO_VPW = tk.DoubleVar()

#VVI
global VVI_LRL1
VVI_LRL1 = -1
VVI_LRL = tk.IntVar()

global VVI_URL1
VVI_URL1 = -1
VVI_URL = tk.IntVar()

global VVI_VA1
VVI_VA1 = -1
VVI_VA = tk.DoubleVar()

global VVI_VPW1
VVI_VPW1 = -1
VVI_VPW = tk.DoubleVar()

global VVI_VRP1
VVI_VRP1 = -1
VVI_VRP = tk.DoubleVar()

#AAI
global AAI_LRL1
AAI_LRL1 = -1
AAI_LRL = tk.IntVar()

global AAI_URL1
AAI_URL1 = -1
AAI_URL = tk.IntVar()

global AAI_AA1
AAI_AA1 = -1
AAI_AA = tk.DoubleVar()

global AAI_APW1
AAI_APW1 = -1
AAI_APW = tk.DoubleVar()

global AAI_ARP1
AAI_ARP1 = -1
AAI_ARP = tk.DoubleVar()


global AOOR_LRL1
AOOR_LRL1 = -1
AOOR_LRL = tk.DoubleVar()

global AOOR_URL1
AOOR_URL1 = -1
AOOR_URL = tk.DoubleVar()

global AOOR_MSR
AOOR_MSR1 = -1
AOOR_MSR = tk.DoubleVar()

global AOOR_AA1
AOOR_AA1 = -1
AOOR_AA = tk.DoubleVar()

global AOOR_APW1
AOOR_APW1 = -1
AOOR_APW = tk.DoubleVar()

global AOOR_AT1
AOOR_AT1 = -1
AOOR_AT = tk.DoubleVar()

global AOOR_ReaT1
AOOR_ReaT1 = -1
AOOR_ReaT = tk.DoubleVar()

global AOOR_RF1
AOOR_RF1 = -1
AOOR_RF = tk.DoubleVar()

global AOOR_RecT1
AOOR_RecT1 = -1
AOOR_RecT = tk.DoubleVar()


global DOO_LRL1
DOO_LRL1 = -1
DOO_LRL = tk.IntVar()

global DOO_URL1
DOO_URL1 = -1
DOO_URL = tk.IntVar()

global DOO_FAVD1
DOO_FAVD1 = -1
DOO_FAVD = tk.IntVar()

global DOO_AA1
DOO_AA1 = -1
DOO_AA = tk.IntVar()

global DOO_VA1
DOO_VA1 = -1
DOO_VA = tk.IntVar()

global DOO_APW1
DOO_APW1 = -1
DOO_APW = tk.IntVar()

global DOO_VPW1
DOO_VPW1 = -1
DOO_VPW = tk.IntVar()

global AAIR_LRL1
AAIR_LRL1 = -1
AAIR_LRL = tk.DoubleVar()

global AAIR_URL1
AAIR_URL1 = -1
AAIR_URL = tk.DoubleVar()

global AAIR_MSR
AAIR_MSR1 = -1
AAIR_MSR = tk.DoubleVar()

global AAIR_AA1
AAIR_AA1 = -1
AAIR_AA = tk.DoubleVar()

global AAIR_APW1
AAIR_APW1 = -1
AAIR_APW = tk.DoubleVar()

global AAIR_AT1
AAIR_AT1 = -1
AAIR_AT = tk.DoubleVar()

global AAIR_ReaT1
AAIR_ReaT1 = -1
AAIR_ReaT = tk.DoubleVar()

global AAIR_RF1
AAIR_RF1 = -1
AAIR_RF = tk.DoubleVar()

global AAIR_RecT1
AAIR_RecT1 = -1
AAIR_RecT = tk.DoubleVar()

global AAIR_AS1
AAIR_AS1 = -1
AAIR_AS = tk.DoubleVar()

global AAIR_ARP1
AAIR_ARP1 = -1
AAIR_ARP = tk.DoubleVar()

global AAIR_PVARP1
AAIR_PVARP1 = -1
AAIR_PVARP = tk.DoubleVar()


global VOOR_LRL1
VOOR_LRL1 = -1
VOOR_LRL = tk.DoubleVar()

global VOOR_URL1
VOOR_URL1 = -1
VOOR_URL = tk.DoubleVar()

global VOOR_MSR
VOOR_MSR1 = -1
VOOR_MSR = tk.DoubleVar()

global VOOR_VA1
VOOR_VA1 = -1
VOOR_VA = tk.DoubleVar()

global VOOR_VPW1
VOOR_VPW1 = -1
VOOR_VPW = tk.DoubleVar()

global VOOR_AT1
VOOR_AT1 = -1
VOOR_AT = tk.DoubleVar()

global VOOR_ReaT1
VOOR_ReaT1 = -1
VOOR_ReaT = tk.DoubleVar()

global VOOR_RF1
VOOR_RF1 = -1
VOOR_RF = tk.DoubleVar()

global VOOR_RecT1
VOOR_RecT1 = -1
VOOR_RecT = tk.DoubleVar()

global VVIR_LRL1
VVIR_LRL1 = -1
VVIR_LRL = tk.DoubleVar()

global VVIR_URL1
VVIR_URL1 = -1
VVIR_URL = tk.DoubleVar()

global VVIR_MSR
VVIR_MSR1 = -1
VVIR_MSR = tk.DoubleVar()

global VVIR_VA1
VVIR_VA1 = -1
VVIR_VA = tk.DoubleVar()

global VVIR_VPW1
VVIR_VPW1 = -1
VVIR_VPW = tk.DoubleVar()

global VVIR_AT1
VVIR_AT1 = -1
VVIR_AT = tk.DoubleVar()

global VVIR_ReaT1
VVIR_ReaT1 = -1
VVIR_ReaT = tk.DoubleVar()

global VVIR_RF1
VVIR_RF1 = -1
VVIR_RF = tk.DoubleVar()

global VVIR_RecT1
VVIR_RecT1 = -1
VVIR_RecT = tk.DoubleVar()

global VVIR_VS1
VVIR_VS1 = -1
VVIR_VS = tk.DoubleVar()

global VVIR_VRP1
VVIR_VRP1 = -1
VVIR_VRP = tk.DoubleVar()

global DOOR_LRL1
DOOR_LRL1 = -1
DOOR_LRL = tk.DoubleVar()

global DOOR_URL1
DOOR_URL1 = -1
DOOR_URL = tk.DoubleVar()

global DOOR_MSR
DOOR_MSR1 = -1
DOOR_MSR = tk.DoubleVar()

global DOOR_VA1
DOOR_VA1 = -1
DOOR_VA = tk.DoubleVar()

global DOOR_VPW1
DOOR_VPW1 = -1
DOOR_VPW = tk.DoubleVar()

global DOOR_AT1
DOOR_AT1 = -1
DOOR_AT = tk.DoubleVar()

global DOOR_ReaT1
DOOR_ReaT1 = -1
DOOR_ReaT = tk.DoubleVar()

global DOOR_RF1
DOOR_RF1 = -1
DOOR_RF = tk.DoubleVar()

global DOOR_RecT1
DOOR_RecT1 = -1
DOOR_RecT = tk.DoubleVar()

global DOOR_FAVD1
DOOR_FAVD1 = -1
DOOR_FAVD = tk.DoubleVar()

global DOOR_AA1
DOOR_AA1 = -1
DOOR_AA = tk.DoubleVar()

global DOOR_APW1
DOOR_APW1 = -1
DOOR_APW = tk.DoubleVar()

def update_dict(string, value):
    string = string
    value = value
    with open('test_data.txt', 'r') as json_file:
        data_dict = json.load(json_file)
        print("updated\n")
        print(data_dict)
        data_dict[string] = value
        print(data_dict)
    with open('test_data.txt', 'w') as json_file:
        json.dump(data_dict, json_file)
        json_file.close()

def ini_file():
    data_dict = {'AOO_LRL':AOO_LRL1, 'AOO_URL': AOO_URL1, 'AOO_AA': AOO_AA1,'AOO_APW':AOO_APW1,'VOO_LRL':VOO_LRL1,'VOO_URL':VOO_URL1,'VOO_VA':VOO_VA1,'VOO_VPW':VOO_VPW1,'AAI_LRL':AAI_LRL1,'AAI_URL':AAI_URL1,'AAI_AA':AAI_AA1,'AAI_APW':AAI_APW1,'AAI_ARP':AAI_ARP1,'VVI_LRL':VVI_LRL1,'VVI_URL':VVI_URL1,'VVI_VA':VVI_VA1,'VVI_VPW':VVI_VPW1,'VVI_VRP':VVI_VRP1,'DOO_LRL':DOO_LRL1,'DOO_URL':DOO_URL1,'DOO_FAVD':DOO_FAVD1,'DOO_AA':DOO_AA1,'DOO_VA':DOO_VA1,'DOO_APW':DOO_APW1,'DOO_VPW':DOO_VPW1,'AOOR_LRL':AOOR_LRL1,'AOOR_URL':AOOR_URL1,'AOOR_MSR':AOOR_MSR1,'AOOR_AA':AOOR_AA1,'AOOR_APW':AOOR_APW1,'AOOR_AT':AOOR_AT1,'AOOR_ReaT':AOOR_ReaT1,'AOOR_RF':AOOR_RF1,'AOOR_RedT':AOOR_RecT1,'AAIR_LRL':AAIR_LRL1,'AAIR_URL':AAIR_URL1,'AAIR_MSR':AAIR_MSR1,'AAIR_AA':AAIR_AA1,'AAIR_APW':AAIR_APW1,'AAIR_AT':AAIR_AT1,'AAIR_ReaT':AAIR_ReaT1,'AAIR_RF':AAIR_RF1,'AAIR_RedT':AAIR_RecT1,'AAIR_AS':AAIR_AS1,'AAIR_ARP':AAIR_ARP1,'AAIR_PVARP':AAIR_PVARP1,'VOOR_LRL':VOOR_LRL1,'VOOR_URL':VOOR_URL1,'VOOR_MSR':VOOR_MSR1,'VOOR_VA':VOOR_VA1,'VOOR_VPW':VOOR_VPW1,'VOOR_AT':VOOR_AT1,'VOOR_ReaT':VOOR_ReaT1,'VOOR_RF':VOOR_RF1,'VOOR_RedT':VOOR_RecT1,'VVIR_LRL':VVIR_LRL1,'VVIR_URL':VVIR_URL1,'VVIR_MSR':VVIR_MSR1,'VVIR_VA':VVIR_VA1,'VVIR_VPW':VVIR_VPW1,'VVIR_AT':VVIR_AT1,'VVIR_ReaT':VVIR_ReaT1,'VVIR_RF':VVIR_RF1,'VVIR_RedT':VVIR_RecT1,'VVIR_VS':VVIR_VS1,'VVIR_VRP':VVIR_VRP1,'DOOR_LRL':DOOR_LRL1,'DOOR_URL':DOOR_URL1,'DOOR_MSR':DOOR_MSR1,'DOOR_VA':DOOR_VA1,'DOOR_VPW':DOOR_VPW1,'DOOR_AT':DOOR_AT1,'DOOR_ReaT':DOOR_ReaT1,'DOOR_RF':DOOR_RF1,'DOOR_RedT':DOOR_RecT1,'DOOR_FAVD':DOOR_FAVD1,'DOOR_AA':DOOR_AA1, 'DOOR_APW':DOOR_APW1}
    with open('test_data.txt','w') as json_file:
        json.dump(data_dict, json_file) #the data_dict is now converted to JSON string 


def Button(window,var_connect):
       
    window_mode_selection = tk.Toplevel(window)
    window_mode_selection.geometry('600x500')
    window_mode_selection.title('Mode Selection')

    print(var_connect[1])
    if var_connect[1] == 1:
        tk.Label(window_mode_selection, text='Device is connecting',font=('Arial',12)).place(x=200,y=100)
    else :
        tk.Label(window_mode_selection, text='Device is disconnecting',font=('Arial',12)).place(x=200,y=100)

    def M_VVI():
        window_mode_vvi = tk.Toplevel(window)
        window_mode_vvi.geometry('500x500')
        window_mode_vvi.title('VVI is selected!')

        VVI_LRL1 = VVI_LRL.get()
        LRL_value = tk.Entry(window_mode_vvi, textvariable = VVI_LRL, font=('Arial',12))
        LRL_value.place(x=280,y=175)
        tk.Label(window_mode_vvi, text='Lower Rate Limit(Int)(30ppm-175ppm): ').place(x=30,y=175)
        update_dict('VVI_LRL',VVI_LRL1)

        VVI_URL1 = VVI_URL.get()
        URL_value = tk.Entry(window_mode_vvi, textvariable = VVI_URL, font=('Arial',12))
        URL_value.place(x=280,y=205)
        tk.Label(window_mode_vvi, text='Upper Rate Limit(Int)(50ppm-175ppm): ').place(x=30,y=205)
        update_dict('VVI_URL',VVI_URL1)

        VVI_VA1 = VVI_VA.get()
        VA_value = tk.Entry(window_mode_vvi, textvariable = VVI_VA, font=('Arial',12))
        VA_value.place(x=280,y=235)
        tk.Label(window_mode_vvi, text='Ventricular Amplitude(Float)(3.5V-7.0V): ').place(x=30,y=235)
        update_dict('VVI_VA',VVI_VA1)

        VVI_VPW1 = VVI_VPW.get()
        VPW_value = tk.Entry(window_mode_vvi, textvariable = VVI_VPW, font=('Arial',12))
        VPW_value.place(x=280,y=265)
        tk.Label(window_mode_vvi, text='Ventricular Pulse Width(Float)(0.1ms-1.9ms): ').place(x=30,y=265)
        update_dict('VVI_VPW',VVI_VPW1)

        VVI_VRP1 = VVI_VRP.get()
        VRP_value = tk.Entry(window_mode_vvi, textvariable = VVI_VRP, font=('Arial',12))
        VRP_value.place(x=280,y=295)
        tk.Label(window_mode_vvi, text='Ventricular Refractory Period(Float): ').place(x=30,y=295)
        update_dict('VVI_VRP',VVI_VRP1)

        VVI_Com = tk.Button(window_mode_vvi, text='VVI_COMPARE', command=M_VVI)
        VVI_Com.place(x=50,y=350)
        if VVI_LRL1 == 0:
            print('1')
        else :
            if VVI_LRL1<30 or VVI_LRL1>175:
                tkinter.messagebox.showerror('Error','LRL out of range!')
            elif VVI_URL1<50 or VVI_URL1>175:
                tkinter.messagebox.showerror('Error','URL out of range!')
            elif VVI_VA1<3.5 or VVI_VA1>7:
                tkinter.messagebox.showerror('Error','VA out of range!')
            elif VVI_VPW1<1 or VVI_VPW1>10:
                tkinter.messagebox.showerror('Error','VPW out of range!')
            elif VVI_VRP1<150 or VVI_VRP1>500:
                tkinter.messagebox.showerror('Error','VRP out of range!')



    def M_AAI():
        window_mode_aai = tk.Toplevel(window)
        window_mode_aai.geometry('500x500')
        window_mode_aai.title('AAI is selected!')

        AAI_LRL1 = AAI_LRL.get()
        LRL_value = tk.Entry(window_mode_aai, textvariable = AAI_LRL, font=('Arial',12))
        LRL_value.place(x=280,y=175)
        tk.Label(window_mode_aai, text='Lower Rate Limit(Int)(30ppm-175ppm): ').place(x=30,y=175)
        update_dict('AAI_LRL',AAI_LRL1)

        AAI_URL1 = AAI_URL.get()
        URL_value = tk.Entry(window_mode_aai, textvariable = AAI_URL, font=('Arial',12))
        URL_value.place(x=280,y=205)
        tk.Label(window_mode_aai, text='Upper Rate Limit(Int)(50ppm-175ppm): ').place(x=30,y=205)
        update_dict('AAI_URL',AAI_URL1)

        AAI_AA1 = AAI_AA.get()
        AA_value = tk.Entry(window_mode_aai, textvariable = AAI_AA, font=('Arial',12))
        AA_value.place(x=280,y=235)
        tk.Label(window_mode_aai, text='Atrial Amplitude(Float)(3.5V-7.0V): ').place(x=30,y=235)
        update_dict('AAI_AA',AAI_AA1)

        AAI_APW1 = AAI_APW.get()
        APW_value = tk.Entry(window_mode_aai, textvariable = AAI_APW, font=('Arial',12))
        APW_value.place(x=280,y=265)
        tk.Label(window_mode_aai, text='Atrial Pulse Width(Float)(0.1ms-1.9ms): ').place(x=30,y=265)
        update_dict('AAI_APW',AAI_APW1)

        AAI_ARP1 = AAI_ARP.get()
        ARP_value = tk.Entry(window_mode_aai, textvariable = AAI_ARP, font=('Arial',12))
        ARP_value.place(x=280,y=295)
        tk.Label(window_mode_aai, text='Atrial Refractory Period(Float): ').place(x=30,y=295)
        update_dict('AAI_ARP',AAI_ARP1)

        AAI_Com = tk.Button(window_mode_aai, text='AAI_COMPARE', command=M_AAI)
        AAI_Com.place(x=50,y=350)
        if AAI_LRL1 == 0:
            print('1')
        else :
            if AAI_LRL1<30 or AAI_LRL1>175:
                tkinter.messagebox.showerror('Error','LRL out of range!')
            elif AAI_URL1<50 or AAI_URL1>175:
                tkinter.messagebox.showerror('Error','URL out of range!')
            elif AAI_AA1<3.5 or AAI_AA1>7:
                tkinter.messagebox.showerror('Error','AA out of range!')
            elif AAI_APW1<1 or AAI_APW1>10:
                tkinter.messagebox.showerror('Error','APW out of range!')
            elif AAI_ARP1<150 or AAI_ARP1>500:
                tkinter.messagebox.showerror('Error','ARP out of range!')


    def M_VOO():
        window_mode_voo = tk.Toplevel(window)
        window_mode_voo.geometry('500x500')
        window_mode_voo.title('VOO is selected!')

        VOO_LRL1 = VOO_LRL.get()
        LRL_value = tk.Entry(window_mode_voo, textvariable = VOO_LRL, font=('Arial',12))
        LRL_value.place(x=280,y=175)
        tk.Label(window_mode_voo, text='Lower Rate Limit(Int)(30ppm-175ppm): ').place(x=30,y=175)
        update_dict('VOO_LRL',VOO_LRL1)

        VOO_URL1 = VOO_URL.get()
        URL_value = tk.Entry(window_mode_voo, textvariable = VOO_URL, font=('Arial',12))
        URL_value.place(x=280,y=205)
        tk.Label(window_mode_voo, text='Upper Rate Limit(Int)(50ppm-175ppm): ').place(x=30,y=205)
        update_dict('VOO_URL',VOO_URL1)

        VOO_VA1 = VOO_VA.get()
        VA_value = tk.Entry(window_mode_voo, textvariable = VOO_VA, font=('Arial',12))
        VA_value.place(x=280,y=235)
        tk.Label(window_mode_voo, text='Ventricular Amplitude(Float)(3.5V-7.0V): ').place(x=30,y=235)
        update_dict('VOO_VA',VOO_VA1)

        VOO_VPW1 = VOO_VPW.get()
        VPW_value = tk.Entry(window_mode_voo, textvariable = VOO_VPW, font=('Arial',12))
        VPW_value.place(x=280,y=265)
        tk.Label(window_mode_voo, text='Ventricular Pulse Width(Float)(0.1ms-1.9ms): ').place(x=30,y=265)
        update_dict('VOO_VPW',VOO_VPW1)

        VOO_Com = tk.Button(window_mode_voo, text='VOO_COMPARE', command=M_VOO)
        VOO_Com.place(x=50,y=300)
        if VOO_LRL1 == 0:
            print('1')
        else :
            if VOO_LRL1<30 or VOO_LRL1>175:
                tkinter.messagebox.showerror('Error','LRL out of range!')
            elif VOO_URL1<50 or VOO_URL1>175:
                tkinter.messagebox.showerror('Error','URL out of range!')
            elif VOO_VA1<3.5 or VOO_VA1>7:
                tkinter.messagebox.showerror('Error','VA out of range!')
            elif VOO_VPW1<1 or VOO_VPW1>10:
                tkinter.messagebox.showerror('Error','VPW out of range!')


    def M_AOO():
        window_mode_aoo = tk.Toplevel(window)
        window_mode_aoo.geometry('500x500')
        window_mode_aoo.title('AOO is selected!')
        print('100')

        AOO_LRL1 = AOO_LRL.get()
        tk.Label(window_mode_aoo, text='Lower Rate Limit(Int)(30ppm-175ppm): ').place(x=30,y=175)
        LRL_value = tk.Entry(window_mode_aoo, textvariable = AOO_LRL, font=('Arial',12))
        LRL_value.place(x=280,y=175)
        update_dict('AOO_LRL',AOO_LRL1)

        
        AOO_URL1 = AOO_URL.get()
        tk.Label(window_mode_aoo, text='Upper Rate Limit(Int)(50ppm-175ppm): ').place(x=30,y=205)
        URL_value = tk.Entry(window_mode_aoo, textvariable = AOO_URL, font=('Arial',12))
        URL_value.place(x=280,y=205)
        update_dict('AOO_URL',AOO_URL1)
        
        AOO_AA1 = AOO_AA.get()
        tk.Label(window_mode_aoo, text='Atrial Amplitude(Float)(3.5V-7.0V): ').place(x=30,y=235)
        AA_value = tk.Entry(window_mode_aoo, textvariable = AOO_AA, font=('Arial',12))
        AA_value.place(x=280,y=235)
        update_dict('AOO_AA',AOO_AA1)

        AOO_APW1 = AOO_APW.get()
        tk.Label(window_mode_aoo, text='Atrial Pulse Width(Float)(0.1ms-1.9ms): ').place(x=30,y=265)
        APW_value = tk.Entry(window_mode_aoo, textvariable = AOO_APW, font=('Arial',12))
        APW_value.place(x=280,y=265)
        update_dict('AOO_APW',AOO_APW1)

        AOO_Com = tk.Button(window_mode_aoo, text='AOO_COMPARE', command=M_AOO)
        AOO_Com.place(x=50,y=300)
        if AOO_LRL1 == 0:
           print('1')
        else :
            if AOO_LRL1<30 or AOO_LRL1>175:
                tkinter.messagebox.showerror('Error','LRL out of range!')
            elif AOO_URL1<50 or AOO_URL1>175:
                tkinter.messagebox.showerror('Error','URL out of range!')
            elif AOO_AA1<3.5 or AOO_AA1>7:
                tkinter.messagebox.showerror('Error','AA out of range!')
            elif AOO_APW1<1 or AOO_APW1>10:
                tkinter.messagebox.showerror('Error','APW out of range!')
    

    def M_DOO():
        window_mode_doo = tk.Toplevel(window)
        window_mode_doo.geometry('500x500')
        window_mode_doo.title('DOO is selected!')
        print('100')

        DOO_LRL1 = DOO_LRL.get()
        tk.Label(window_mode_doo, text='Lower Rate Limit(Int)(30ppm-175ppm): ').place(x=30,y=175)
        LRL_value = tk.Entry(window_mode_doo, textvariable = DOO_LRL, font=('Arial',12))
        LRL_value.place(x=280,y=175)

        update_dict('DOD_LRL',DOO_LRL1)

    
        DOO_URL1 = DOO_URL.get()
        tk.Label(window_mode_doo, text='Upper Rate Limit(Int)(50ppm-175ppm): ').place(x=30,y=205)
        URL_value = tk.Entry(window_mode_doo, textvariable = DOO_URL, font=('Arial',12))
        URL_value.place(x=280,y=205)

        update_dict('DOO_URL',DOO_URL1)
        
        DOO_FAVD1 = DOO_FAVD.get()
        tk.Label(window_mode_doo, text='Fixed AV Delay(Int)(70ms-300ms): ').place(x=30,y=235)
        FAVD_value = tk.Entry(window_mode_doo, textvariable = DOO_FAVD, font=('Arial',12))
        FAVD_value.place(x=280,y=235)
        
        update_dict('DOO_FAVD',DOO_FAVD1)

        DOO_AA1 = DOO_AA.get()
        tk.Label(window_mode_doo, text='Atrial Amplitude(Float)(3.5V-7.0V): ').place(x=30,y=265)
        AA_value = tk.Entry(window_mode_doo, textvariable = DOO_AA, font=('Arial',12))
        AA_value.place(x=280,y=265)

        update_dict('DOO_AA',DOO_AA1)

        DOO_VA1 = DOO_VA.get()
        tk.Label(window_mode_doo, text='Ventricular Amplitude(Float)(3.5V-7.0V): ').place(x=30,y=295)
        AA_value = tk.Entry(window_mode_doo, textvariable = DOO_VA, font=('Arial',12))
        AA_value.place(x=280,y=295)

        update_dict('DOO_VA',DOO_VA1)

        DOO_APW1 = DOO_APW.get()
        tk.Label(window_mode_doo, text='Atrial Pulse Width(Float)(0.1ms-1.9ms): ').place(x=30,y=325)
        APW_value = tk.Entry(window_mode_doo, textvariable = DOO_APW, font=('Arial',12))
        APW_value.place(x=280,y=325)

        update_dict('DOO_APW',DOO_APW1) 

        DOO_VPW1 = DOO_VPW.get()
        tk.Label(window_mode_doo, text='Ventricular Pulse Width(Float)(0.1ms-1.9ms): ').place(x=30,y=355)
        VPW_value = tk.Entry(window_mode_doo, textvariable = DOO_VPW, font=('Arial',12))
        VPW_value.place(x=280,y=355)

        update_dict('DOO_VPW',DOO_VPW1)


    def M_AOOR():
        window_mode_aoor = tk.Toplevel(window)
        window_mode_aoor.geometry('500x500')
        window_mode_aoor.title('AOOR is selected!')

        AOOR_LRL1 = AOOR_LRL.get()
        LRL_value = tk.Entry(window_mode_aoor, textvariable = AOOR_LRL, font=('Arial',12))
        LRL_value.place(x=280,y=150)
        tk.Label(window_mode_aoor, text='Lower Rate Limit(Int)(30ppm-175ppm): ').place(x=30,y=150)
        update_dict('AOOR_LRL',AOOR_LRL1)

        AOOR_URL1 = AOOR_URL.get()
        URL_value = tk.Entry(window_mode_aoor, textvariable = AOOR_URL, font=('Arial',12))
        URL_value.place(x=280,y=180)
        tk.Label(window_mode_aoor, text='Upper Rate Limit(Int)(50ppm-175ppm): ').place(x=30,y=180)
        update_dict('AOOR_URL',AOOR_URL1)

        AOOR_MSR1 = AOOR_MSR.get()
        MSR_value = tk.Entry(window_mode_aoor, textvariable = AOOR_MSR, font=('Arial',12))
        MSR_value.place(x=280,y=210)
        tk.Label(window_mode_aoor, text='Maximum Sensor Rate(Int)(50ppm-175ppm):').place(x=30,y=210)
        update_dict('AOOR_MSR',AOOR_MSR1)

        AOOR_AA1 = AOOR_AA.get()
        AA_value = tk.Entry(window_mode_aoor, textvariable = AOOR_AA, font=('Arial',12))
        AA_value.place(x=280,y=240)
        tk.Label(window_mode_aoor, text='Atrial Amplitude(Float)(3.5V-7.0V): ').place(x=30,y=240)
        update_dict('AOOR_AA',AOOR_AA1)

        AOOR_APW1 = AOOR_APW.get()
        APW_value = tk.Entry(window_mode_aoor, textvariable = AOOR_APW, font=('Arial',12))
        APW_value.place(x=280,y=270)
        tk.Label(window_mode_aoor, text='Atrial Pulse Width(Float)(0.1ms-1.9ms): ').place(x=30,y=270)
        update_dict('AOOR_APW',AOOR_APW1)

        AOOR_AT1 = AOOR_AT.get()
        AT_value = tk.Entry(window_mode_aoor, textvariable = AOOR_AT, font=('Arial',12))
        AT_value.place(x=280,y=300)
        tk.Label(window_mode_aoor, text='Activity Threshold(Float): ').place(x=30,y=300)
        update_dict('AOOR_AT',AOOR_AT1)

        AOOR_ReaT1 = AOOR_ReaT.get()
        ReaT_value = tk.Entry(window_mode_aoor, textvariable = AOOR_ReaT, font=('Arial',12))
        ReaT_value.place(x=280,y=330)
        tk.Label(window_mode_aoor, text='Reaction Time(Float): ').place(x=30,y=330)
        update_dict('AOOR_ReaT',AOOR_ReaT1)

        AOOR_RF1 = AOOR_RF.get()
        RF_value = tk.Entry(window_mode_aoor, textvariable = AOOR_RF, font=('Arial',12))
        RF_value.place(x=280,y=360)
        tk.Label(window_mode_aoor, text='Response Factor(Float): ').place(x=30,y=360)
        update_dict('AOOR_RF',AOOR_RF1)

        AOOR_RecT1 = AOOR_RecT.get()
        RecT_value = tk.Entry(window_mode_aoor, textvariable = AOOR_RecT, font=('Arial',12))
        RecT_value.place(x=280,y=390)
        tk.Label(window_mode_aoor, text='Recovery Time(Float): ').place(x=30,y=390)
        update_dict('AOOR_RecT',AOOR_RecT1)



    def M_AAIR():
        window_mode_aair = tk.Toplevel(window)
        window_mode_aair.geometry('500x550')
        window_mode_aair.title('AAIR is selected!')

        AAIR_LRL1 = AAIR_LRL.get()
        LRL_value = tk.Entry(window_mode_aair, textvariable = AAIR_LRL, font=('Arial',12))
        LRL_value.place(x=280,y=150)
        tk.Label(window_mode_aair, text='Lower Rate Limit(Int)(30ppm-175ppm): ').place(x=30,y=150)
        update_dict('AAIR_LRL',AAIR_LRL1)

        AAIR_URL1 = AAIR_URL.get()
        URL_value = tk.Entry(window_mode_aair, textvariable = AAIR_URL, font=('Arial',12))
        URL_value.place(x=280,y=180)
        tk.Label(window_mode_aair, text='Upper Rate Limit(Int)(50ppm-175ppm): ').place(x=30,y=180)
        update_dict('AAUR_URL',AAIR_URL1)

        AAIR_MSR1 = AAIR_MSR.get()
        MSR_value = tk.Entry(window_mode_aair, textvariable = AAIR_MSR, font=('Arial',12))
        MSR_value.place(x=280,y=210)
        tk.Label(window_mode_aair, text='Maximum Sensor Rate(Int)(50ppm-175ppm):').place(x=30,y=210)
        update_dict('AAIR_MSR',AAIR_MSR1)

        AAIR_AA1 = AAIR_AA.get()
        AA_value = tk.Entry(window_mode_aair, textvariable = AAIR_AA, font=('Arial',12))
        AA_value.place(x=280,y=240)
        tk.Label(window_mode_aair, text='Atrial Amplitude(Float)(3.5V-7.0V): ').place(x=30,y=240)
        update_dict('AAIR_AA',AAIR_AA1)

        AAIR_APW1 = AAIR_APW.get()
        APW_value = tk.Entry(window_mode_aair, textvariable = AAIR_APW, font=('Arial',12))
        APW_value.place(x=280,y=270)
        tk.Label(window_mode_aair, text='Atrial Pulse Width(Float)(0.1ms-1.9ms): ').place(x=30,y=270)
        update_dict('AAIR_APW',AAIR_APW1)

        AAIR_AT1 = AAIR_AT.get()
        AT_value = tk.Entry(window_mode_aair, textvariable = AAIR_AT, font=('Arial',12))
        AT_value.place(x=280,y=300)
        tk.Label(window_mode_aair, text='Activity Threshold(Float): ').place(x=30,y=300)
        update_dict('AAIR_AT',AAIR_AT1)

        AAIR_ReaT1 = AAIR_ReaT.get()
        ReaT_value = tk.Entry(window_mode_aair, textvariable = AAIR_ReaT, font=('Arial',12))
        ReaT_value.place(x=280,y=330)
        tk.Label(window_mode_aair, text='Reaction Time(Float): ').place(x=30,y=330)
        update_dict('AAIR_ReaT',AAIR_ReaT1)

        AAIR_RF1 = AAIR_RF.get()
        RF_value = tk.Entry(window_mode_aair, textvariable = AAIR_RF, font=('Arial',12))
        RF_value.place(x=280,y=360)
        tk.Label(window_mode_aair, text='Response Factor(Float): ').place(x=30,y=360)
        update_dict('AAIR_RF',AAIR_RF1)

        AAIR_RecT1 = AAIR_RecT.get()
        RecT_value = tk.Entry(window_mode_aair, textvariable = AAIR_RecT, font=('Arial',12))
        RecT_value.place(x=280,y=390)
        tk.Label(window_mode_aair, text='Recovery Time(Float): ').place(x=30,y=390)
        update_dict('AAIR_RecT',AAIR_RecT1)


        #Add new variables

        AAIR_AS1 = AAIR_AS.get()
        AS_value = tk.Entry(window_mode_aair, textvariable = AAIR_AS, font=('Arial',12))
        AS_value.place(x=280,y=420)
        tk.Label(window_mode_aair, text='Atrial Sensitivity(Float): ').place(x=30,y=420)
        update_dict('AAIR_AS',AAIR_AS1)

        AAIR_ARP1 = AAIR_ARP.get()
        ARP_value = tk.Entry(window_mode_aair, textvariable = AAIR_ARP, font=('Arial',12))
        ARP_value.place(x=280,y=450)
        tk.Label(window_mode_aair, text='Atrial Refractory Period (integer): ').place(x=30,y=450)
        update_dict('AAIR_AT',AAIR_ARP1)

        AAIR_PVARP1 = AAIR_PVARP.get()
        PVARP_value = tk.Entry(window_mode_aair, textvariable = AAIR_PVARP, font=('Arial',12))
        PVARP_value.place(x=280,y=480)
        tk.Label(window_mode_aair, text='PVARP (Float): ').place(x=30,y=480)
        update_dict('AAIR_PVARP',AAIR_PVARP1)

        


        #VOOR

    def M_VOOR():
        window_mode_VOOR = tk.Toplevel(window)
        window_mode_VOOR.geometry('500x500')
        window_mode_VOOR.title('VOOR is selected!')

        VOOR_LRL1 = VOOR_LRL.get()
        LRL_value = tk.Entry(window_mode_VOOR, textvariable = VOOR_LRL, font=('Arial',12))
        LRL_value.place(x=280,y=150)
        tk.Label(window_mode_VOOR, text='Lower Rate Limit(Int)(30ppm-175ppm): ').place(x=30,y=150)
        update_dict('VOOR_LRL',VOOR_LRL1)

        VOOR_URL1 = VOOR_URL.get()
        URL_value = tk.Entry(window_mode_VOOR, textvariable = VOOR_URL, font=('Arial',12))
        URL_value.place(x=280,y=180)
        tk.Label(window_mode_VOOR, text='Upper Rate Limit(Int)(50ppm-175ppm): ').place(x=30,y=180)
        update_dict('VOOR_URL',VOOR_URL1)

        VOOR_MSR1 = VOOR_MSR.get()
        MSR_value = tk.Entry(window_mode_VOOR, textvariable = VOOR_MSR, font=('Arial',12))
        MSR_value.place(x=280,y=210)
        tk.Label(window_mode_VOOR, text='Maximum Sensor Rate(Int)(50ppm-175ppm):').place(x=30,y=210)
        update_dict('VOOR_MSR',VOOR_MSR1)

        VOOR_VA1 = VOOR_VA.get()
        VA_value = tk.Entry(window_mode_VOOR, textvariable = VOOR_VA, font=('Arial',12))
        VA_value.place(x=280,y=240)
        tk.Label(window_mode_VOOR, text='Ventricular Amplitude(Float)(3.5V-7.0V): ').place(x=30,y=240)
        update_dict('VOOR_VA',VOOR_VA1)

        VOOR_VPW1 = VOOR_VPW.get()
        VPW_value = tk.Entry(window_mode_VOOR, textvariable = VOOR_VPW, font=('Arial',12))
        VPW_value.place(x=280,y=270)
        tk.Label(window_mode_VOOR, text='Ventricular Pulse Width(Float)(0.1ms-1.9ms): ').place(x=30,y=270)
        update_dict('VOOR_VPW',VOOR_VPW1)

        VOOR_AT1 = VOOR_AT.get()
        AT_value = tk.Entry(window_mode_VOOR, textvariable = VOOR_AT, font=('Arial',12))
        AT_value.place(x=280,y=300)
        tk.Label(window_mode_VOOR, text='Activity Threshold(Float): ').place(x=30,y=300)
        update_dict('VOOR_AT',VOOR_AT1)

        VOOR_ReaT1 = VOOR_ReaT.get()
        ReaT_value = tk.Entry(window_mode_VOOR, textvariable = VOOR_ReaT, font=('Arial',12))
        ReaT_value.place(x=280,y=330)
        tk.Label(window_mode_VOOR, text='Reaction Time(Float): ').place(x=30,y=330)
        update_dict('VOOR_ReaT',VOOR_ReaT1)

        VOOR_RF1 = VOOR_RF.get()
        RF_value = tk.Entry(window_mode_VOOR, textvariable = VOOR_RF, font=('Arial',12))
        RF_value.place(x=280,y=360)
        tk.Label(window_mode_VOOR, text='Response Factor(Float): ').place(x=30,y=360)
        update_dict('VOOR_RF',VOOR_RF1)

        VOOR_RecT1 = VOOR_RecT.get()
        RecT_value = tk.Entry(window_mode_VOOR, textvariable = VOOR_RecT, font=('Arial',12))
        RecT_value.place(x=280,y=390)
        tk.Label(window_mode_VOOR, text='Recovery Time(Float): ').place(x=30,y=390)
        update_dict('VOOR_RecT',VOOR_RecT1)


    def M_VVIR():
        window_mode_VVIR = tk.Toplevel(window)
        window_mode_VVIR.geometry('500x500')
        window_mode_VVIR.title('VVIR is selected!')

        VVIR_LRL1 = VVIR_LRL.get()
        LRL_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_LRL, font=('Arial',12))
        LRL_value.place(x=280,y=150)
        tk.Label(window_mode_VVIR, text='Lower Rate Limit(Int)(30ppm-175ppm): ').place(x=30,y=150)
        update_dict('VVIR_LRL',VVIR_LRL1)

        VVIR_URL1 = VVIR_URL.get()
        URL_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_URL, font=('Arial',12))
        URL_value.place(x=280,y=180)
        tk.Label(window_mode_VVIR, text='Upper Rate Limit(Int)(50ppm-175ppm): ').place(x=30,y=180)
        update_dict('VVIR_URL',VVIR_URL1)

        VVIR_MSR1 = VVIR_MSR.get()
        MSR_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_MSR, font=('Arial',12))
        MSR_value.place(x=280,y=210)
        tk.Label(window_mode_VVIR, text='Maximum Sensor Rate(Int)(50ppm-175ppm):').place(x=30,y=210)
        update_dict('VVIR_MSR',VVIR_MSR1)

        VVIR_VA1 = VVIR_VA.get()
        VA_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_VA, font=('Arial',12))
        VA_value.place(x=280,y=240)
        tk.Label(window_mode_VVIR, text='Ventricular Amplitude(Float)(3.5V-7.0V): ').place(x=30,y=240)
        update_dict('VVIR_VA',VVIR_VA1)

        VVIR_VPW1 = VVIR_VPW.get()
        VPW_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_VPW, font=('Arial',12))
        VPW_value.place(x=280,y=270)
        tk.Label(window_mode_VVIR, text='Ventricular Pulse Width(Float)(0.1ms-1.9ms): ').place(x=30,y=270)
        update_dict('VVIR_VPW',VVIR_VPW1)

        VVIR_AT1 = VVIR_AT.get()
        AT_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_AT, font=('Arial',12))
        AT_value.place(x=280,y=300)
        tk.Label(window_mode_VVIR, text='Activity Threshold(Float): ').place(x=30,y=300)
        update_dict('VVIR_AT',VVIR_AT1)

        VVIR_ReaT1 = VVIR_ReaT.get()
        ReaT_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_ReaT, font=('Arial',12))
        ReaT_value.place(x=280,y=330)
        tk.Label(window_mode_VVIR, text='Reaction Time(Float): ').place(x=30,y=330)
        update_dict('VVIR_ReaT',VVIR_ReaT1)

        VVIR_RF1 = VVIR_RF.get()
        RF_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_RF, font=('Arial',12))
        RF_value.place(x=280,y=360)
        tk.Label(window_mode_VVIR, text='Response Factor(Float): ').place(x=30,y=360)
        update_dict('VVIR_RF',VVIR_RF1)

        VVIR_RecT1 = VVIR_RecT.get()
        RecT_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_RecT, font=('Arial',12))
        RecT_value.place(x=280,y=390)
        tk.Label(window_mode_VVIR, text='Recovery Time(Float): ').place(x=30,y=390)
        update_dict('VVIR_RecT',VVIR_RecT1)

        VVIR_VS1 = VVIR_VS.get()
        VS_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_VS, font=('Arial',12))
        VS_value.place(x=280,y=420)
        tk.Label(window_mode_VVIR, text='Ventricular Sensitivity(Float): ').place(x=30,y=420)
        update_dict('VVIR_VS',VVIR_VS1)

        VVIR_VRP1 = VVIR_VRP.get()
        VRP_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_VRP, font=('Arial',12))
        VRP_value.place(x=280,y=450)
        tk.Label(window_mode_VVIR, text='Ventricular Refractory Period(Float): ').place(x=30,y=450)
        update_dict('VVIR_VRP',VVIR_VRP1)
        
        

    def M_DOOR():
        window_mode_DOOR = tk.Toplevel(window)
        window_mode_DOOR.geometry('500x550')
        window_mode_DOOR.title('DOOR is selected!')

        DOOR_LRL1 = DOOR_LRL.get()
        LRL_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_LRL, font=('Arial',12))
        LRL_value.place(x=280,y=150)
        tk.Label(window_mode_DOOR, text='Lower Rate Limit(Int)(30ppm-175ppm): ').place(x=30,y=150)
        update_dict('DOOR_LRL',DOOR_LRL1)

        DOOR_URL1 = DOOR_URL.get()
        URL_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_URL, font=('Arial',12))
        URL_value.place(x=280,y=180)
        tk.Label(window_mode_DOOR, text='Upper Rate Limit(Int)(50ppm-175ppm): ').place(x=30,y=180)
        update_dict('DOOR_URL',DOOR_URL1)

        DOOR_MSR1 = DOOR_MSR.get()
        MSR_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_MSR, font=('Arial',12))
        MSR_value.place(x=280,y=210)
        tk.Label(window_mode_DOOR, text='Maximum Sensor Rate(Int)(50ppm-175ppm):').place(x=30,y=210)
        update_dict('DOOR_MSR',DOOR_MSR1)

        DOOR_VA1 = DOOR_VA.get()
        VA_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_VA, font=('Arial',12))
        VA_value.place(x=280,y=240)
        tk.Label(window_mode_DOOR, text='Ventricular Amplitude(Float)(3.5V-7.0V): ').place(x=30,y=240)
        update_dict('DOOR_VA',DOOR_VA1)

        DOOR_VPW1 = DOOR_VPW.get()
        VPW_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_VPW, font=('Arial',12))
        VPW_value.place(x=280,y=270)
        tk.Label(window_mode_DOOR, text='Ventricular Pulse Width(Float)(0.1ms-1.9ms): ').place(x=30,y=270)
        update_dict('DOOR_VPW',DOOR_VPW1)

        DOOR_AT1 = DOOR_AT.get()
        AT_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_AT, font=('Arial',12))
        AT_value.place(x=280,y=300)
        tk.Label(window_mode_DOOR, text='Activity Threshold(Float): ').place(x=30,y=300)
        update_dict('DOOR_AT',DOOR_AT1)

        DOOR_ReaT1 = DOOR_ReaT.get()
        ReaT_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_ReaT, font=('Arial',12))
        ReaT_value.place(x=280,y=330)
        tk.Label(window_mode_DOOR, text='Reaction Time(Float): ').place(x=30,y=330)
        update_dict('DOOR_ReaT',DOOR_ReaT1)

        DOOR_RF1 = DOOR_RF.get()
        RF_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_RF, font=('Arial',12))
        RF_value.place(x=280,y=360)
        tk.Label(window_mode_DOOR, text='Response Factor(Float): ').place(x=30,y=360)
        update_dict('DOOR_RF',DOOR_RF1)

        DOOR_RecT1 = DOOR_RecT.get()
        RecT_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_RecT, font=('Arial',12))
        RecT_value.place(x=280,y=390)
        tk.Label(window_mode_DOOR, text='Recovery Time(Float): ').place(x=30,y=390)
        update_dict('DOOR_RecT',DOOR_RecT1)

        DOOR_FAVD1 = DOOR_FAVD.get()
        FAVD_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_FAVD, font=('Arial',12))
        FAVD_value.place(x=280,y=420)
        tk.Label(window_mode_DOOR, text='Fixed AV Delay(Int)(70ms-300ms)').place(x=30,y=420)
        update_dict('DOOR_FAVD',DOOR_FAVD1)

        DOOR_AA1 = DOOR_AA.get()
        AA_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_AA, font=('Arial',12))
        AA_value.place(x=280,y=450)
        tk.Label(window_mode_DOOR, text='Atrial Amplitude(Float)(3.5V-7.0V): ').place(x=30,y=450)
        update_dict('DOOR_AA',DOOR_AA1)

        DOOR_APW1 = DOOR_APW.get()
        APW_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_APW, font=('Arial',12))
        APW_value.place(x=280,y=480)
        tk.Label(window_mode_DOOR, text='Atrial Pulse Width(Float)(0.1ms-1.9ms): ').place(x=30,y=480)
        update_dict('DOOR_APW',DOOR_APW1)




















    AOO_Bu = tk.Button(window_mode_selection, text='AOO_Bu', command= M_AOO )
    AOO_Bu.place(x=120,y=240)
    
    
    VOO_Bu = tk.Button(window_mode_selection, text='VOO_Bu',command= M_VOO )
    VOO_Bu.place(x=200,y=240)
    

    AAI_Bu = tk.Button(window_mode_selection, text='AAI_Bu', command= M_AAI )
    AAI_Bu.place(x=280,y=240)


    VVI_Bu = tk.Button(window_mode_selection, text='VVI_Bu',command= M_VVI )
    VVI_Bu.place(x=360,y=240)

    DOO_Bu = tk.Button(window_mode_selection, text='DOO_Bu',command= M_DOO )
    DOO_Bu.place(x=440,y=240)

    AOOR_Bu = tk.Button(window_mode_selection, text='AOOR_Bu',command= M_AOOR )
    AOOR_Bu.place(x=120,y=280)

    AAIR_Bu = tk.Button(window_mode_selection, text='AAIR_Bu',command= M_AAIR )
    AAIR_Bu.place(x=200,y=280)
        
    VOOR_Bu = tk.Button(window_mode_selection, text='VOOR_Bu',command= M_VOOR )
    VOOR_Bu.place(x=280,y=280)
            
    VVIR_Bu = tk.Button(window_mode_selection, text='VVIR_Bu',command= M_VVIR )
    VVIR_Bu.place(x=360,y=280)

    DOOR_Bu = tk.Button(window_mode_selection, text='DOOR_Bu',command= M_DOOR )
    DOOR_Bu.place(x=440,y=280)


