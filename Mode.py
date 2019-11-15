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


global data_dict

global usrLimit

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
    data_dict = {'AOO_LRL':AOO_LRL1, 'AOO_URL': AOO_URL1, 'AOO_AA': AOO_AA1,'AOO_APW':AOO_APW1,'VOO_LRL':VOO_LRL1,'VOO_URL':VOO_URL1,'VOO_VA':VOO_VA1,'VOO_VPW':VOO_VPW1,'AAI_LRL':AAI_LRL1,'AAI_URL':AAI_URL1,'AAI_AA':AAI_AA1,'AAI_APW':AAI_APW1,'AAI_ARP':AAI_ARP1,'VVI_LRL':VVI_LRL1,'VVI_URL':VVI_URL1,'VVI_VA':VVI_VA1,'VVI_VPW':VVI_VPW1,'VVI_VRP':VVI_VRP1,'AOOR_LRL':AOOR_LRL1,'AOOR_URL':AOOR_URL1}
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
        LRL_value.place(x=230,y=175)
        tk.Label(window_mode_vvi, text='Lower Rate Limit(Int): ').place(x=30,y=175)
        update_dict('VVI_LRL',VVI_LRL1)

        VVI_URL1 = VVI_URL.get()
        URL_value = tk.Entry(window_mode_vvi, textvariable = VVI_URL, font=('Arial',12))
        URL_value.place(x=230,y=205)
        tk.Label(window_mode_vvi, text='Upper Rate Limit(Int): ').place(x=30,y=205)
        update_dict('VVI_URL',VVI_URL1)

        VVI_VA1 = VVI_VA.get()
        VA_value = tk.Entry(window_mode_vvi, textvariable = VVI_VA, font=('Arial',12))
        VA_value.place(x=230,y=235)
        tk.Label(window_mode_vvi, text='Ventricular Amplitude(Float): ').place(x=30,y=235)
        update_dict('VVI_VA',VVI_VA1)

        VVI_VPW1 = VVI_VPW.get()
        VPW_value = tk.Entry(window_mode_vvi, textvariable = VVI_VPW, font=('Arial',12))
        VPW_value.place(x=230,y=265)
        tk.Label(window_mode_vvi, text='Ventricular Pulse Width(Float): ').place(x=30,y=265)
        update_dict('VVI_VPW',VVI_VPW1)

        VVI_VRP1 = VVI_VRP.get()
        VRP_value = tk.Entry(window_mode_vvi, textvariable = VVI_VRP, font=('Arial',12))
        VRP_value.place(x=230,y=295)
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
        LRL_value.place(x=230,y=175)
        tk.Label(window_mode_aai, text='Lower Rate Limit(Int): ').place(x=30,y=175)
        update_dict('AAI_LRL',AAI_LRL1)

        AAI_URL1 = AAI_URL.get()
        URL_value = tk.Entry(window_mode_aai, textvariable = AAI_URL, font=('Arial',12))
        URL_value.place(x=230,y=205)
        tk.Label(window_mode_aai, text='Upper Rate Limit(Int): ').place(x=30,y=205)
        update_dict('AAI_URL',AAI_URL1)

        AAI_AA1 = AAI_AA.get()
        AA_value = tk.Entry(window_mode_aai, textvariable = AAI_AA, font=('Arial',12))
        AA_value.place(x=230,y=235)
        tk.Label(window_mode_aai, text='Atrial Amplitude(Float): ').place(x=30,y=235)
        update_dict('AAI_AA',AAI_AA1)

        AAI_APW1 = AAI_APW.get()
        APW_value = tk.Entry(window_mode_aai, textvariable = AAI_APW, font=('Arial',12))
        APW_value.place(x=230,y=265)
        tk.Label(window_mode_aai, text='Atrial Pulse Width(Float): ').place(x=30,y=265)
        update_dict('AAI_APW',AAI_APW1)

        AAI_ARP1 = AAI_ARP.get()
        ARP_value = tk.Entry(window_mode_aai, textvariable = AAI_ARP, font=('Arial',12))
        ARP_value.place(x=230,y=295)
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
        LRL_value.place(x=230,y=175)
        tk.Label(window_mode_voo, text='Lower Rate Limit(Int): ').place(x=30,y=175)
        update_dict('VOO_LRL',VOO_LRL1)

        VOO_URL1 = VOO_URL.get()
        URL_value = tk.Entry(window_mode_voo, textvariable = VOO_URL, font=('Arial',12))
        URL_value.place(x=230,y=205)
        tk.Label(window_mode_voo, text='Upper Rate Limit(Int): ').place(x=30,y=205)
        update_dict('VOO_URL',VOO_URL1)

        VOO_VA1 = VOO_VA.get()
        VA_value = tk.Entry(window_mode_voo, textvariable = VOO_VA, font=('Arial',12))
        VA_value.place(x=230,y=235)
        tk.Label(window_mode_voo, text='Ventricular Amplitude(Float): ').place(x=30,y=235)
        update_dict('VOO_VA',VOO_VA1)

        VOO_VPW1 = VOO_VPW.get()
        VPW_value = tk.Entry(window_mode_voo, textvariable = VOO_VPW, font=('Arial',12))
        VPW_value.place(x=230,y=265)
        tk.Label(window_mode_voo, text='Ventricular Pulse Width(Float): ').place(x=30,y=265)
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
        tk.Label(window_mode_aoo, text='Lower Rate Limit(Int): ').place(x=30,y=175)
        LRL_value = tk.Entry(window_mode_aoo, textvariable = AOO_LRL, font=('Arial',12))
        LRL_value.place(x=230,y=175)
        update_dict('AOO_LRL',AOO_LRL1)

        
        AOO_URL1 = AOO_URL.get()
        tk.Label(window_mode_aoo, text='Upper Rate Limit(Int): ').place(x=30,y=205)
        URL_value = tk.Entry(window_mode_aoo, textvariable = AOO_URL, font=('Arial',12))
        URL_value.place(x=230,y=205)
        update_dict('AOO_URL',AOO_URL1)
        
        AOO_AA1 = AOO_AA.get()
        tk.Label(window_mode_aoo, text='Atrial Amplitude(Float): ').place(x=30,y=235)
        AA_value = tk.Entry(window_mode_aoo, textvariable = AOO_AA, font=('Arial',12))
        AA_value.place(x=230,y=235)
        update_dict('AOO_AA',AOO_AA1)

        AOO_APW1 = AOO_APW.get()
        tk.Label(window_mode_aoo, text='Atrial Pulse Width(Float): ').place(x=30,y=265)
        APW_value = tk.Entry(window_mode_aoo, textvariable = AOO_APW, font=('Arial',12))
        APW_value.place(x=230,y=265)
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
    

    def M_AOOR():
        window_mode_aoor = tk.Toplevel(window)
        window_mode_aoor.geometry('500x500')
        window_mode_aoor.title('AOOR is selected!')

        AOOR_LRL1 = AOOR_LRL.get()
        LRL_value = tk.Entry(window_mode_aoor, textvariable = AOOR_LRL, font=('Arial',12))
        LRL_value.place(x=230,y=150)
        tk.Label(window_mode_aoor, text='Lower Rate Limit(Float): ').place(x=30,y=150)
        update_dict('AOOR_LRL',AOOR_LRL1)

        AOOR_URL1 = AOOR_URL.get()
        URL_value = tk.Entry(window_mode_aoor, textvariable = AOOR_URL, font=('Arial',12))
        URL_value.place(x=230,y=180)
        tk.Label(window_mode_aoor, text='Upper Rate Limit(Float): ').place(x=30,y=180)
        update_dict('AOOR_URL',AOOR_URL1)

        AOOR_MSR1 = AOOR_MSR.get()
        MSR_value = tk.Entry(window_mode_aoor, textvariable = AOOR_MSR, font=('Arial',12))
        MSR_value.place(x=230,y=210)
        tk.Label(window_mode_aoor, text='Maximum Sensor Rate(Float): ').place(x=30,y=210)
        update_dict('AOOR_MSR',AOOR_MSR1)

        AOOR_AA1 = AOOR_AA.get()
        AA_value = tk.Entry(window_mode_aoor, textvariable = AOOR_AA, font=('Arial',12))
        AA_value.place(x=230,y=240)
        tk.Label(window_mode_aoor, text='Atrial Amplitude(Float): ').place(x=30,y=240)
        update_dict('AOOR_AA',AOOR_AA1)

        AOOR_APW1 = AOOR_APW.get()
        APW_value = tk.Entry(window_mode_aoor, textvariable = AOOR_APW, font=('Arial',12))
        APW_value.place(x=230,y=270)
        tk.Label(window_mode_aoor, text='Atrial Pulse Width (Float): ').place(x=30,y=270)
        update_dict('AOOR_APW',AOOR_APW1)

        AOOR_AT1 = AOOR_AT.get()
        AT_value = tk.Entry(window_mode_aoor, textvariable = AOOR_AT, font=('Arial',12))
        AT_value.place(x=230,y=300)
        tk.Label(window_mode_aoor, text='Activity Threshold(Float): ').place(x=30,y=300)
        update_dict('AOOR_AT',AOOR_AT1)

        AOOR_ReaT1 = AOOR_ReaT.get()
        ReaT_value = tk.Entry(window_mode_aoor, textvariable = AOOR_ReaT, font=('Arial',12))
        ReaT_value.place(x=230,y=330)
        tk.Label(window_mode_aoor, text='Reaction Time(Float): ').place(x=30,y=330)
        update_dict('AOOR_ReaT',AOOR_ReaT1)

        AOOR_RF1 = AOOR_RF.get()
        RF_value = tk.Entry(window_mode_aoor, textvariable = AOOR_RF, font=('Arial',12))
        RF_value.place(x=230,y=360)
        tk.Label(window_mode_aoor, text='Response Factor(Float): ').place(x=30,y=360)
        update_dict('AOOR_RF',AOOR_RF1)

        AOOR_RecT1 = AOOR_RecT.get()
        RecT_value = tk.Entry(window_mode_aoor, textvariable = AOOR_RecT, font=('Arial',12))
        RecT_value.place(x=230,y=390)
        tk.Label(window_mode_aoor, text='Recovery Time(Float): ').place(x=30,y=390)
        update_dict('AOOR_RecT',AOOR_RecT1)


































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



    def M_DOO():
        window_mode_doo = tk.Toplevel(window)
        window_mode_doo.geometry('500x500')
        window_mode_doo.title('ODD is selected!')
        print('100')

        DOO_LRL1 = DOO_LRL.get()
        tk.Label(window_mode_doo, text='Lower Rate Limit(Int): ').place(x=30,y=175)
        LRL_value = tk.Entry(window_mode_doo, textvariable = DOO_LRL, font=('Arial',12))
        LRL_value.place(x=230,y=175)

        update_dict('ODD_LRL',ODD_LRL1)

    
        DOO_URL1 = DOO_URL.get()
        tk.Label(window_mode_doo, text='Upper Rate Limit(Int): ').place(x=30,y=205)
        URL_value = tk.Entry(window_mode_doo, textvariable = DOO_URL, font=('Arial',12))
        URL_value.place(x=230,y=205)

        update_dict('DOO_URL',DOO_URL1)
        
        DOO_FAVD1 = DOO_FAVD.get()
        tk.Label(window_mode_doo, text='Fixed AV Delay(Float): ').place(x=30,y=235)
        FAVD_value = tk.Entry(window_mode_doo, textvariable = DOO_FAVD, font=('Arial',12))
        FAVD_value.place(x=230,y=235)
        
        update_dict('DOO_FAVD',DOO_FAVD1)

        DOO_AA1 = DOO_AA.get()
        tk.Label(window_mode_doo, text='Atrial Amplitude(Float): ').place(x=30,y=265)
        AA_value = tk.Entry(window_mode_doo, textvariable = DOO_AA, font=('Arial',12))
        AA_value.place(x=230,y=265)

        update_dict('DOO_AA',DOO_AA1)

        DOO_VA1 = DOO_VA.get()
        tk.Label(window_mode_doo, text='Ventricular Amplitude(Float): ').place(x=30,y=265)
        AA_value = tk.Entry(window_mode_doo, textvariable = DOO_VA, font=('Arial',12))
        AA_value.place(x=230,y=295)

        update_dict('DOO_VA',DOO_VA1)

        DOO_APW1 = DOO_APW.get()
        tk.Label(window_mode_doo, text='Atrial Pulse Width(Float): ').place(x=30,y=265)
        APW_value = tk.Entry(window_mode_doo, textvariable = DOO_APW, font=('Arial',12))
        APW_value.place(x=230,y=325)

        update_dict('DOO_APW',DOO_APW1)

        DOO_VPW1 = DOO_VPW.get()
        tk.Label(window_mode_doo, text='Ventricular Pulse Width(Float): ').place(x=30,y=265)
        VPW_value = tk.Entry(window_mode_doo, textvariable = DOO_VPW, font=('Arial',12))
        VPW_value.place(x=230,y=355)

        update_dict('DOO_VPW',DOO_VPW1)


        
        





























    AOO_Bu = tk.Button(window_mode_selection, text='AOO_Bu', command= M_AOO )
    AOO_Bu.place(x=120,y=240)
    
    
    VOO_Bu = tk.Button(window_mode_selection, text='VOO_Bu',command= M_VOO )
    VOO_Bu.place(x=200,y=240)
    

    AAI_Bu = tk.Button(window_mode_selection, text='AAI_Bu', command= M_AAI )
    AAI_Bu.place(x=280,y=240)


    VVI_Bu = tk.Button(window_mode_selection, text='VVI_Bu',command= M_VVI )
    VVI_Bu.place(x=360,y=240)

        
            

