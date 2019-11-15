def M_DOOR():
        window_mode_DOOR = tk.Toplevel(window)
        window_mode_DOOR.geometry('500x500')
        window_mode_DOOR.title('DOOR is selected!')

        DOOR_LRL1 = DOOR_LRL.get()
        LRL_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_LRL, font=('Arial',12))
        LRL_value.place(x=230,y=150)
        tk.Label(window_mode_DOOR, text='Lower Rate Limit(Float): ').place(x=30,y=150)
        update_dict('DOOR_LRL',DOOR_LRL1)

        DOOR_URL1 = DOOR_URL.get()
        URL_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_URL, font=('Arial',12))
        URL_value.place(x=230,y=180)
        tk.Label(window_mode_DOOR, text='Upper Rate Limit(Float): ').place(x=30,y=180)
        update_dict('DOOR_URL',DOOR_URL1)

        DOOR_MSR1 = DOOR_MSR.get()
        MSR_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_MSR, font=('Arial',12))
        MSR_value.place(x=230,y=210)
        tk.Label(window_mode_DOOR, text='Maximum Sensor Rate(Float): ').place(x=30,y=210)
        update_dict('DOOR_MSR',DOOR_MSR1)

        DOOR_VA1 = DOOR_VA.get()
        VA_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_VA, font=('Arial',12))
        VA_value.place(x=230,y=240)
        tk.Label(window_mode_DOOR, text='Ventricular Amplitude(Float): ').place(x=30,y=240)
        update_dict('DOOR_VA',DOOR_VA1)

        DOOR_VPW1 = DOOR_VPW.get()
        VPW_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_VPW, font=('Arial',12))
        VPW_value.place(x=230,y=270)
        tk.Label(window_mode_DOOR, text='Ventricular Pulse Width (Float): ').place(x=30,y=270)
        update_dict('DOOR_VPW',DOOR_VPW1)

        DOOR_AT1 = DOOR_AT.get()
        AT_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_AT, font=('Arial',12))
        AT_value.place(x=230,y=300)
        tk.Label(window_mode_DOOR, text='Activity Threshold(Float): ').place(x=30,y=300)
        update_dict('DOOR_AT',DOOR_AT1)

        DOOR_ReaT1 = DOOR_ReaT.get()
        ReaT_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_ReaT, font=('Arial',12))
        ReaT_value.place(x=230,y=330)
        tk.Label(window_mode_DOOR, text='Reaction Time(Float): ').place(x=30,y=330)
        update_dict('DOOR_ReaT',DOOR_ReaT1)

        DOOR_RF1 = DOOR_RF.get()
        RF_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_RF, font=('Arial',12))
        RF_value.place(x=230,y=360)
        tk.Label(window_mode_DOOR, text='Response Factor(Float): ').place(x=30,y=360)
        update_dict('DOOR_RF',DOOR_RF1)

        DOOR_RecT1 = DOOR_RecT.get()
        RecT_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_RecT, font=('Arial',12))
        RecT_value.place(x=230,y=390)
        tk.Label(window_mode_DOOR, text='Recovery Time(Float): ').place(x=30,y=390)
        update_dict('DOOR_RecT',DOOR_RecT1)

        DOOR_FAVD1 = DOOR_FAVD.get()
        FAVD_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_FAVD, font=('Arial',12))
        FAVD_value.place(x=230,y=420)
        tk.Label(window_mode_DOOR, text='Fixed AV Delay (Float): ').place(x=30,y=420)
        update_dict('DOOR_FAVD',DOOR_FAVD1)

        DOOR_AA1 = DOOR_AA.get()
        AA_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_AA, font=('Arial',12))
        AA_value.place(x=230,y=450)
        tk.Label(window_mode_DOOR, text='Atrial Amplitude(Float): ').place(x=30,y=450)
        update_dict('DOOR_AA',DOOR_AA1)

        DOOR_APW1 = DOOR_APW.get()
        APW_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_APW, font=('Arial',12))
        APW_value.place(x=230,y=480)
        tk.Label(window_mode_DOOR, text='Atrial Pulse Width(Float): ').place(x=30,y=480)
        update_dict('DOOR_APW',DOOR_APW1)
























        'DOOR_LRL':DOOR_LRL1,'DOOR_URL':DOOR_URL1,'DOOR_MSR':DOOR_MSR1,'DOOR_VA':DOOR_VA1,'DOOR_VPW':DOOR_VPW1,'DOOR_AT':DOOR_AT1,'DOOR_ReaT':DOOR_ReaT1,'DOOR_RF':DOOR_RF1,'DOOR_RedT':DOOR_RecT1,'DOOR_FAVD':DOOR_FAVD1,'DOOR_AA':DOOR_AA1, 'DOOR_APW':DOOR_APW1




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

