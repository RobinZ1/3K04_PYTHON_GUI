def M_VVIR():
        window_mode_VVIR = tk.Toplevel(window)
        window_mode_VVIR.geometry('500x500')
        window_mode_VVIR.title('VVIR is selected!')

        VVIR_LRL1 = VVIR_LRL.get()
        LRL_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_LRL, font=('Arial',12))
        LRL_value.place(x=230,y=150)
        tk.Label(window_mode_VVIR, text='Lower Rate Limit(Float): ').place(x=30,y=150)
        update_dict('VVIR_LRL',VVIR_LRL1)

        VVIR_URL1 = VVIR_URL.get()
        URL_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_URL, font=('Arial',12))
        URL_value.place(x=230,y=180)
        tk.Label(window_mode_VVIR, text='Upper Rate Limit(Float): ').place(x=30,y=180)
        update_dict('VVIR_URL',VVIR_URL1)

        VVIR_MSR1 = VVIR_MSR.get()
        MSR_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_MSR, font=('Arial',12))
        MSR_value.place(x=230,y=210)
        tk.Label(window_mode_VVIR, text='Maximum Sensor Rate(Float): ').place(x=30,y=210)
        update_dict('VVIR_MSR',VVIR_MSR1)

        VVIR_VA1 = VVIR_VA.get()
        VA_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_VA, font=('Arial',12))
        VA_value.place(x=230,y=240)
        tk.Label(window_mode_VVIR, text='Ventricular Amplitude(Float): ').place(x=30,y=240)
        update_dict('VVIR_VA',VVIR_VA1)

        VVIR_VPW1 = VVIR_VPW.get()
        VPW_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_VPW, font=('Arial',12))
        VPW_value.place(x=230,y=270)
        tk.Label(window_mode_VVIR, text='Ventricular Pulse Width (Float): ').place(x=30,y=270)
        update_dict('VVIR_VPW',VVIR_VPW1)

        VVIR_AT1 = VVIR_AT.get()
        AT_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_AT, font=('Arial',12))
        AT_value.place(x=230,y=300)
        tk.Label(window_mode_VVIR, text='Activity Threshold(Float): ').place(x=30,y=300)
        update_dict('VVIR_AT',VVIR_AT1)

        VVIR_ReaT1 = VVIR_ReaT.get()
        ReaT_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_ReaT, font=('Arial',12))
        ReaT_value.place(x=230,y=330)
        tk.Label(window_mode_VVIR, text='Reaction Time(Float): ').place(x=30,y=330)
        update_dict('VVIR_ReaT',VVIR_ReaT1)

        VVIR_RF1 = VVIR_RF.get()
        RF_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_RF, font=('Arial',12))
        RF_value.place(x=230,y=360)
        tk.Label(window_mode_VVIR, text='Response Factor(Float): ').place(x=30,y=360)
        update_dict('VVIR_RF',VVIR_RF1)

        VVIR_RecT1 = VVIR_RecT.get()
        RecT_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_RecT, font=('Arial',12))
        RecT_value.place(x=230,y=390)
        tk.Label(window_mode_VVIR, text='Recovery Time(Float): ').place(x=30,y=390)
        update_dict('VVIR_RecT',VVIR_RecT1)

        VVIR_VS1 = VVIR_VS.get()
        VS_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_VS, font=('Arial',12))
        VS_value.place(x=230,y=420)
        tk.Label(window_mode_VVIR, text='Ventricular Sensitivity(Float): ').place(x=30,y=420)
        update_dict('VVIR_VS',VVIR_VS1)

        VVIR_VRP1 = VVIR_VRP.get()
        VRP_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_VRP, font=('Arial',12))
        VRP_value.place(x=230,y=450)
        tk.Label(window_mode_VVIR, text='Ventricular Refractory Period(Float): ').place(x=30,y=450)
        update_dict('VVIR_VRP',VVIR_VRP1)
























        'VVIR_LRL':VVIR_LRL1,'VVIR_URL':VVIR_URL1,'VVIR_MSR':VVIR_MSR1,'VVIR_VA':VVIR_VA1,'VVIR_VPW':VVIR_VPW1,'VVIR_AT':VVIR_AT1,'VVIR_ReaT':VVIR_ReaT1,'VVIR_RF':VVIR_RF1,'VVIR_RedT':VVIR_RecT1,'VVIR_VS':VVIR_VS1,'VVIR_VRP':VVIR_VRP1




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

