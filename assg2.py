import tkinter as tk
import tkinter.messagebox
import pickle
import json


global window 
window = tk.Tk()
status = window 
window.title('Welcome to 3K04!')
window.geometry('400x300')


# welcome page
canvas = tk.Canvas(window, width=400, height=135, bg='green')
image_file = tk.PhotoImage(file='3K04.gif')
image = canvas.create_image(200,0, anchor='n',image=image_file)
canvas.pack(side='top')
tk.Label(window, text='Welcome',font=('Arial',16)).pack()

#User information
tk.Label(window, text='ID:',font=('Arial',12)).place(x=10,y=170)
tk.Label(window, text='Password:',font=('Arial',12)).place(x=10,y=210)

# User login entry
#usr name
var_usr_name = tk.StringVar()
var_usr_name.set('example@mcmaster.ca')
entry_usr_name = tk.Entry(window, textvariable = var_usr_name, font=('Arial',14))
entry_usr_name.place(x=120,y=175)
#usr password
var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, font=('Arial',14), show='*')
entry_usr_pwd.place(x=120,y=215)
var_connect = [5]


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

global VVI_VS1
VVI_VS1 = -1
VVI_VS = tk.DoubleVar()

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

global AAI_AS1
AAI_AS1 = -1
AAI_AS = tk.DoubleVar()

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

global data_dict
global listbox

global usrLimit

class Dictionary:

    def update_dict(self,string,value):
        self.string = string
        self.value = value
        with open('test_data.txt', 'r') as json_file:
            self.data_dict = json.load(json_file)
            print("updated\n")
            print(self.data_dict)
            self.data_dict[string] = value
            print(self.data_dict)
        with open('test_data.txt', 'w') as json_file:   
            json.dump(self.data_dict, json_file)
            json_file.close()

    def ini_file(self):
        
        self.data_dict = {'AOO_LRL':AOO_LRL1, 'AOO_URL': AOO_URL1, 'AOO_AA': AOO_AA1,'AOO_APW':AOO_APW1,'VOO_LRL':VOO_LRL1,'VOO_URL':VOO_URL1,'VOO_VA':VOO_VA1,'VOO_VPW':VOO_VPW1,'AAI_LRL':AAI_LRL1,'AAI_URL':AAI_URL1,'AAI_AA':AAI_AA1,'AAI_APW':AAI_APW1,'AAI_ARP':AAI_ARP1,'AAI_AS':AAI_AS1,'VVI_LRL':VVI_LRL1,'VVI_URL':VVI_URL1,'VVI_VA':VVI_VA1,'VVI_VPW':VVI_VPW1,'VVI_VRP':VVI_VRP1, 'VVI_VS':VVI_VS1,'DOO_LRL':DOO_LRL1,'DOO_URL':DOO_URL1,'DOO_FAVD':DOO_FAVD1,'DOO_AA':DOO_AA1,'DOO_VA':DOO_VA1,'DOO_APW':DOO_APW1,'DOO_VPW':DOO_VPW1,'AOOR_LRL':AOOR_LRL1,'AOOR_URL':AOOR_URL1,'AOOR_MSR':AOOR_MSR1,'AOOR_AA':AOOR_AA1,'AOOR_APW':AOOR_APW1,'AOOR_AT':AOOR_AT1,'AOOR_ReaT':AOOR_ReaT1,'AOOR_RF':AOOR_RF1,'AOOR_RedT':AOOR_RecT1,'AAIR_LRL':AAIR_LRL1,'AAIR_URL':AAIR_URL1,'AAIR_MSR':AAIR_MSR1,'AAIR_AA':AAIR_AA1,'AAIR_APW':AAIR_APW1,'AAIR_AT':AAIR_AT1,'AAIR_ReaT':AAIR_ReaT1,'AAIR_RF':AAIR_RF1,'AAIR_RedT':AAIR_RecT1,'AAIR_AS':AAIR_AS1,'AAIR_ARP':AAIR_ARP1,'AAIR_PVARP':AAIR_PVARP1,'VOOR_LRL':VOOR_LRL1,'VOOR_URL':VOOR_URL1,'VOOR_MSR':VOOR_MSR1,'VOOR_VA':VOOR_VA1,'VOOR_VPW':VOOR_VPW1,'VOOR_AT':VOOR_AT1,'VOOR_ReaT':VOOR_ReaT1,'VOOR_RF':VOOR_RF1,'VOOR_RedT':VOOR_RecT1,'VVIR_LRL':VVIR_LRL1,'VVIR_URL':VVIR_URL1,'VVIR_MSR':VVIR_MSR1,'VVIR_VA':VVIR_VA1,'VVIR_VPW':VVIR_VPW1,'VVIR_AT':VVIR_AT1,'VVIR_ReaT':VVIR_ReaT1,'VVIR_RF':VVIR_RF1,'VVIR_RedT':VVIR_RecT1,'VVIR_VS':VVIR_VS1,'VVIR_VRP':VVIR_VRP1,'DOOR_LRL':DOOR_LRL1,'DOOR_URL':DOOR_URL1,'DOOR_MSR':DOOR_MSR1,'DOOR_VA':DOOR_VA1,'DOOR_VPW':DOOR_VPW1,'DOOR_AT':DOOR_AT1,'DOOR_ReaT':DOOR_ReaT1,'DOOR_RF':DOOR_RF1,'DOOR_RedT':DOOR_RecT1,'DOOR_FAVD':DOOR_FAVD1,'DOOR_AA':DOOR_AA1, 'DOOR_APW':DOOR_APW1}
        
        with open('test_data.txt','w') as json_file:
            json.dump(self.data_dict, json_file) #the data_dict is now converted to JSON string 
d=Dictionary()
d.ini_file()
#Initializing the data_dict (IMPORTANT) AND USER LIMITS

class Mode:

        #def __init__(self, window_mode_selection):
            #window_mode_selection = tk.Toplevel()
           # window_mode_selection.geometry('600x300')
         #   window_mode_selection.title('Mode Selection')
          #  self.window_mode_selection = window_mode_selection; 
            
    

        
        

        def Button(self):
            window_mode_selection = tk.Toplevel()
            window_mode_selection.geometry('600x300')
            window_mode_selection.title('Mode Selection')
            #if var_connect[0] == 1:
              #  tk.Label(window_mode_selection, text='Device is connected',font=('Arial',12)).place(x=200,y=260)
            #else :
              #  tk.Label(window_mode_selection, text='Device is disconnected',font=('Arial',12)).place(x=200,y=260)
         #Scrollbar
        
            def data_scroll():
            
                scrollbar = tk.Scrollbar(window_mode_selection)
                scrollbar.pack(side=tk.RIGHT, fill= tk.BOTH)

                listbox = tk.Listbox(window_mode_selection, width = 60)
                listbox.pack()
                
                with open('test_data.txt','r') as json_file:
                    data_dict = json.load(json_file)
                    
                for key, value in data_dict.items():
                    listbox.insert(tk.END, (key, value))

                with open('test_data.txt','w') as json_file:
                    json.dump(data_dict, json_file)

                listbox.config(yscrollcommand=scrollbar.set)
                scrollbar.config(command=listbox.yview)
            


            
            
                
            def M_VVI():
                window_mode_vvi = tk.Toplevel(window)
                window_mode_vvi.geometry('500x600')
                window_mode_vvi.title('VVI is selected!')

                VVI_LRL1 = VVI_LRL.get()
                LRL_value = tk.Entry(window_mode_vvi, textvariable = VVI_LRL, font=('Arial',12))
                LRL_value.place(x=280,y=175)
                tk.Label(window_mode_vvi, text='Lower Rate Limit(Int)(30ppm-175ppm): ').place(x=30,y=175)
                d.update_dict('VVI_LRL',VVI_LRL1)

                VVI_URL1 = VVI_URL.get()
                URL_value = tk.Entry(window_mode_vvi, textvariable = VVI_URL, font=('Arial',12))
                URL_value.place(x=280,y=205)
                tk.Label(window_mode_vvi, text='Upper Rate Limit(Int)(50ppm-175ppm): ').place(x=30,y=205)
                d.update_dict('VVI_URL',VVI_URL1)

                VVI_VA1 = VVI_VA.get()
                VA_value = tk.Entry(window_mode_vvi, textvariable = VVI_VA, font=('Arial',12))
                VA_value.place(x=280,y=235)
                tk.Label(window_mode_vvi, text='Ventricular Amplitude(Float)(3.5V-7.0V): ').place(x=30,y=235)
                d.update_dict('VVI_VA',VVI_VA1)

                VVI_VPW1 = VVI_VPW.get()
                VPW_value = tk.Entry(window_mode_vvi, textvariable = VVI_VPW, font=('Arial',12))
                VPW_value.place(x=280,y=265)
                tk.Label(window_mode_vvi, text='Ventricular Pulse Width(Float)(0.1ms-1.9ms): ').place(x=30,y=265)
                d.update_dict('VVI_VPW',VVI_VPW1)

                VVI_VRP1 = VVI_VRP.get()
                VRP_value = tk.Entry(window_mode_vvi, textvariable = VVI_VRP, font=('Arial',12))
                VRP_value.place(x=280,y=295)
                tk.Label(window_mode_vvi, text='Ventricular Refractory Period(Int)(150-500ms): ').place(x=30,y=295)
                d.update_dict('VVI_VRP',VVI_VRP1)

                VVI_VS1 = VVI_VS.get()
                VS_value = tk.Entry(window_mode_vvi, textvariable = VVI_VS, font=('Arial',12))
                VS_value.place(x=280,y=325)
                tk.Label(window_mode_vvi, text='Ventricular Sensitivity(FLoat)(1.0mV-10mV): ').place(x=30,y=325)
                d.update_dict('VVI_VS',VVI_VS1)

                VVI_Com = tk.Button(window_mode_vvi, text='VVI_COMPARE', command=lambda:[M_VVI(),window_mode_vvi.destroy(),window_mode_selection.destroy(),self.Button()])
                VVI_Com.place(x=50,y=365)
                if VVI_LRL1 == 0:
                    print('1')
                else :
                    if VVI_LRL1<30 or VVI_LRL1>175:
                        tkinter.messagebox.showerror('Error','LRL out of range!',parent=window_mode_vvi)
                    elif VVI_URL1<50 or VVI_URL1>175:
                        tkinter.messagebox.showerror('Error','URL out of range!',parent=window_mode_vvi)
                    elif VVI_VA1<3.5 or VVI_VA1>7:
                        tkinter.messagebox.showerror('Error','VA out of range!',parent=window_mode_vvi)
                    elif VVI_VPW1<0.1 or VVI_VPW1>1.9:
                        tkinter.messagebox.showerror('Error','VPW out of range!',parent=window_mode_vvi)
                    elif VVI_VRP1<150 or VVI_VRP1>500:
                        tkinter.messagebox.showerror('Error','VRP out of range!',parent=window_mode_vvi)
                    elif VVI_VS1<1.0 or VVI_VS1>10:
                        tkinter.messagebox.showerror('Error','VS out of range!',parent=window_mode_vvi)
                    else:
                        tkinter.messagebox.showinfo('Passed','Values Saved!',parent=window_mode_vvi)
                    
                    


            def M_AAI():
                window_mode_aai = tk.Toplevel(window)
                window_mode_aai.geometry('500x500')
                window_mode_aai.title('AAI is selected!')

                AAI_LRL1 = AAI_LRL.get()
                LRL_value = tk.Entry(window_mode_aai, textvariable = AAI_LRL, font=('Arial',12))
                LRL_value.place(x=280,y=175)
                tk.Label(window_mode_aai, text='Lower Rate Limit(Int)(30ppm-175ppm): ').place(x=30,y=175)
                d.update_dict('AAI_LRL',AAI_LRL1)

                
                AAI_URL1 = AAI_URL.get()
                URL_value = tk.Entry(window_mode_aai, textvariable = AAI_URL, font=('Arial',12))
                URL_value.place(x=280,y=205)
                tk.Label(window_mode_aai, text='Upper Rate Limit(Int)(50ppm-175ppm): ').place(x=30,y=205)
                d.update_dict('AAI_URL',AAI_URL1)

                AAI_AA1 = AAI_AA.get()
                AA_value = tk.Entry(window_mode_aai, textvariable = AAI_AA, font=('Arial',12))
                AA_value.place(x=280,y=235)
                tk.Label(window_mode_aai, text='Atrial Amplitude(Float)(3.5V-7.0V): ').place(x=30,y=235)
                d.update_dict('AAI_AA',AAI_AA1)

                AAI_APW1 = AAI_APW.get()
                APW_value = tk.Entry(window_mode_aai, textvariable = AAI_APW, font=('Arial',12))
                APW_value.place(x=280,y=265)
                tk.Label(window_mode_aai, text='Atrial Pulse Width(Float)(0.1ms-1.9ms): ').place(x=30,y=265)
                d.update_dict('AAI_APW',AAI_APW1)

                AAI_ARP1 = AAI_ARP.get()
                ARP_value = tk.Entry(window_mode_aai, textvariable = AAI_ARP, font=('Arial',12))
                ARP_value.place(x=280,y=295)
                tk.Label(window_mode_aai, text='Atrial Refractory Period(Int)(150ms-500ms): ').place(x=30,y=295)
                d.update_dict('AAI_ARP',AAI_ARP1)

                AAI_AS1 = AAI_AS.get()
                AS_value = tk.Entry(window_mode_aai, textvariable = AAI_AS, font=('Arial',12))
                AS_value.place(x=280,y=325)
                tk.Label(window_mode_aai, text='Atrial Sensitivity(Float)(1.0mV-10mV): ').place(x=30,y=325)
                d.update_dict('AAI_AS',AAI_AS1)

                AAI_Com = tk.Button(window_mode_aai, text='AAI_COMPARE', command=lambda:[M_AAI(),window_mode_aai.destroy(),window_mode_selection.destroy(),self.Button()])
                AAI_Com.place(x=50,y=365)
                if AAI_LRL1 == 0:
                    print('1')
                else :
                    
                    if AAI_LRL1<30 or AAI_LRL1>175:
                        tkinter.messagebox.showerror('Error','LRL out of range!',parent=window_mode_aai)
                    elif AAI_URL1<50 or AAI_URL1>175:
                        tkinter.messagebox.showerror('Error','URL out of range!',parent=window_mode_aai)
                    elif AAI_AA1<3.5 or AAI_AA1>7:
                        tkinter.messagebox.showerror('Error','AA out of range!',parent=window_mode_aai)
                    elif AAI_APW1<0.1 or AAI_APW1>1.9:
                        tkinter.messagebox.showerror('Error','APW out of range!',parent=window_mode_aai)
                    elif AAI_ARP1<150 or AAI_ARP1>500:
                        tkinter.messagebox.showerror('Error','ARP out of range!',parent=window_mode_aai)
                    elif AAI_AS1<1.0 or AAI_AS1>10:
                        tkinter.messagebox.showerror('Error','AS out of range!',parent=window_mode_aai)
                    else:
                        tkinter.messagebox.showinfo('Passed','Values Saved!',parent=window_mode_aai)
                

                    
                    

            def M_VOO():
                window_mode_voo = tk.Toplevel(window)
                window_mode_voo.geometry('500x500')
                window_mode_voo.title('VOO is selected!')

                VOO_LRL1 = VOO_LRL.get()
                LRL_value = tk.Entry(window_mode_voo, textvariable = VOO_LRL, font=('Arial',12))
                LRL_value.place(x=280,y=175)
                tk.Label(window_mode_voo, text='Lower Rate Limit(Int)(30ppm-175ppm): ').place(x=30,y=175)
                d.update_dict('VOO_LRL',VOO_LRL1)
                

                VOO_URL1 = VOO_URL.get()
                URL_value = tk.Entry(window_mode_voo, textvariable = VOO_URL, font=('Arial',12))
                URL_value.place(x=280,y=205)
                tk.Label(window_mode_voo, text='Upper Rate Limit(Int)(50ppm-175ppm): ').place(x=30,y=205)
                d.update_dict('VOO_URL',VOO_URL1)
                
                VOO_VA1 = VOO_VA.get()
                VA_value = tk.Entry(window_mode_voo, textvariable = VOO_VA, font=('Arial',12))
                VA_value.place(x=280,y=235)
                tk.Label(window_mode_voo, text='Ventricular Amplitude(Float)(3.5V-7.0V): ').place(x=30,y=235)
                d.update_dict('VOO_VA',VOO_VA1)

                VOO_VPW1 = VOO_VPW.get()
                VPW_value = tk.Entry(window_mode_voo, textvariable = VOO_VPW, font=('Arial',12))
                VPW_value.place(x=280,y=265)
                tk.Label(window_mode_voo, text='Ventricular Pulse Width(Float)(0.1ms-1.9ms): ').place(x=30,y=265)
                d.update_dict('VOO_VPW',VOO_VPW1)
                VOO_Com = tk.Button(window_mode_voo, text='VOO_COMPARE', command=lambda:[M_VOO(),window_mode_voo.destroy(),window_mode_selection.destroy(),self.Button()])
                VOO_Com.place(x=50,y=300)
                
                

                if VOO_LRL1 == 0:
                    pass
                else:

                    if VOO_LRL1<30 or VOO_LRL1>175:
                        tkinter.messagebox.showerror('Error','LRL out of range!',parent=window_mode_voo)
                        
                    elif VOO_URL1<50 or VOO_URL1>175:
                        tkinter.messagebox.showerror('Error','URL out of range!',parent=window_mode_voo)
                        
                    elif VOO_VA1<3.5 or VOO_VA1>7:
                        tkinter.messagebox.showerror('Error','VA out of range!',parent=window_mode_voo)
                        
                    elif VOO_VPW1<0.1 or VOO_VPW1>1.9:
                        tkinter.messagebox.showerror('Error','VPW out of range!',parent=window_mode_voo)
                    else:
                        tkinter.messagebox.showinfo('Passed','Values Saved!',parent=window_mode_voo)
                    
                    
                    
                    
                    
                        
                    
            

            

            

            
    
        




    


            def M_AOO():
                window_mode_aoo = tk.Toplevel(window)
                window_mode_aoo.geometry('500x500')
                window_mode_aoo.title('AOO is selected!')
                print('100')

                AOO_LRL1 = AOO_LRL.get()
                tk.Label(window_mode_aoo, text='Lower Rate Limit(Int)(30ppm-175ppm): ').place(x=30,y=175)
                LRL_value = tk.Entry(window_mode_aoo, textvariable = AOO_LRL, font=('Arial',12))
                LRL_value.place(x=280,y=175)
                d.update_dict('AOO_LRL',AOO_LRL1)

                
                AOO_URL1 = AOO_URL.get()
                tk.Label(window_mode_aoo, text='Upper Rate Limit(Int)(50ppm-175ppm): ').place(x=30,y=205)
                URL_value = tk.Entry(window_mode_aoo, textvariable = AOO_URL, font=('Arial',12))
                URL_value.place(x=280,y=205)
                d.update_dict('AOO_URL',AOO_URL1)
                
                AOO_AA1 = AOO_AA.get()
                tk.Label(window_mode_aoo, text='Atrial Amplitude(Float)(3.5V-7.0V): ').place(x=30,y=235)
                AA_value = tk.Entry(window_mode_aoo, textvariable = AOO_AA, font=('Arial',12))
                AA_value.place(x=280,y=235)
                d.update_dict('AOO_AA',AOO_AA1)

                AOO_APW1 = AOO_APW.get()
                tk.Label(window_mode_aoo, text='Atrial Pulse Width(Float)(0.1ms-1.9ms): ').place(x=30,y=265)
                APW_value = tk.Entry(window_mode_aoo, textvariable = AOO_APW, font=('Arial',12))
                APW_value.place(x=280,y=265)
                d.update_dict('AOO_APW',AOO_APW1)

                AOO_Com = tk.Button(window_mode_aoo, text='AOO_COMPARE', command=lambda:[M_AOO(),window_mode_aoo.destroy(),window_mode_selection.destroy(),self.Button()])
                AOO_Com.place(x=50,y=300)
                if AOO_LRL1 == 0:
                    print('1')
                else :
                    if AOO_LRL1<30 or AOO_LRL1>175:
                        tkinter.messagebox.showerror('Error','LRL out of range!',parent=window_mode_aoo)
                    elif AOO_URL1<50 or AOO_URL1>175:
                        tkinter.messagebox.showerror('Error','URL out of range!',parent=window_mode_aoo)
                    elif AOO_AA1<3.5 or AOO_AA1>7:
                        tkinter.messagebox.showerror('Error','AA out of range!',parent=window_mode_aoo)
                    elif AOO_APW1<0.1 or AOO_APW1>1.9:
                        tkinter.messagebox.showerror('Error','APW out of range!',parent=window_mode_aoo)
                    else:
                        tkinter.messagebox.showinfo('Passed','Values Saved!',parent=window_mode_aoo)
                    
                    
                    




            def M_DOO():
                window_mode_doo = tk.Toplevel(window)
                window_mode_doo.geometry('500x500')
                window_mode_doo.title('DOO is selected!')
                print('100')

                DOO_LRL1 = DOO_LRL.get()
                tk.Label(window_mode_doo, text='Lower Rate Limit(Int)(30ppm-175ppm): ').place(x=30,y=175)
                LRL_value = tk.Entry(window_mode_doo, textvariable = DOO_LRL, font=('Arial',12))
                LRL_value.place(x=280,y=175)

                d.update_dict('DOD_LRL',DOO_LRL1)


            
                DOO_URL1 = DOO_URL.get()
                tk.Label(window_mode_doo, text='Upper Rate Limit(Int)(50ppm-175ppm): ').place(x=30,y=205)
                URL_value = tk.Entry(window_mode_doo, textvariable = DOO_URL, font=('Arial',12))
                URL_value.place(x=280,y=205)
                d.update_dict('DOO_URL',DOO_URL1)
                
                DOO_FAVD1 = DOO_FAVD.get()
                tk.Label(window_mode_doo, text='Fixed AV Delay(Int)(70ms-300ms): ').place(x=30,y=235)
                FAVD_value = tk.Entry(window_mode_doo, textvariable = DOO_FAVD, font=('Arial',12))
                FAVD_value.place(x=280,y=235)

                d.update_dict('DOO_FAVD',DOO_FAVD1)

                DOO_AA1 = DOO_AA.get()
                tk.Label(window_mode_doo, text='Atrial Amplitude(Float)(3.5V-7.0V): ').place(x=30,y=265)
                AA_value = tk.Entry(window_mode_doo, textvariable = DOO_AA, font=('Arial',12))
                AA_value.place(x=280,y=265)

                d.update_dict('DOO_AA',DOO_AA1)

                DOO_VA1 = DOO_VA.get()
                tk.Label(window_mode_doo, text='Ventricular Amplitude(Float)(3.5V-7.0V): ').place(x=30,y=295)
                AA_value = tk.Entry(window_mode_doo, textvariable = DOO_VA, font=('Arial',12))
                AA_value.place(x=280,y=295)

                d.update_dict('DOO_VA',DOO_VA1)

                DOO_APW1 = DOO_APW.get()
                tk.Label(window_mode_doo, text='Atrial Pulse Width(Float)(0.1ms-1.9ms): ').place(x=30,y=325)
                APW_value = tk.Entry(window_mode_doo, textvariable = DOO_APW, font=('Arial',12))
                APW_value.place(x=280,y=325)

                d.update_dict('DOO_APW',DOO_APW1) 

                DOO_VPW1 = DOO_VPW.get()
                tk.Label(window_mode_doo, text='Ventricular Pulse Width(Float)(0.1ms-1.9ms): ').place(x=30,y=355)
                VPW_value = tk.Entry(window_mode_doo, textvariable = DOO_VPW, font=('Arial',12))
                VPW_value.place(x=280,y=355)
                d.update_dict('DOO_VPW',DOO_VPW1)

                DOO_Com = tk.Button(window_mode_doo, text='DOO_COMPARE', command=lambda:[M_DOO(),window_mode_doo.destroy(),window_mode_selection.destroy(),self.Button()])
                DOO_Com.place(x=50,y=390)
                if DOO_LRL1 == 0:
                    print('1')
                else :
                    if DOO_LRL1<30 or DOO_LRL1>175:
                        tkinter.messagebox.showerror('Error','LRL is out of range!',parent=window_mode_doo)
                    elif DOO_URL1<50 or DOO_URL1>175:
                        tkinter.messagebox.showerror('Error','URL is out of range!',parent=window_mode_doo)
                    elif DOO_FAVD1<70 or DOO_FAVD1>300:
                        tkinter.messagebox.showerror('Error', 'FAVD is out of range',parent=window_mode_doo)
                    elif DOO_AA1<3.5 or DOO_AA1>7.0:
                        tkinter.messagebox.showerror('Error', 'AA is out of range',parent=window_mode_doo)
                    elif DOO_VA1<3.5 or DOO_VA1>7.0:
                        tkinter.messagebox.showerror('Error','VA is out of range!',parent=window_mode_doo)
                    elif DOO_APW1<0.1 or DOO_APW1>1.9:
                        tkinter.messagebox.showerror('Error', 'APW is out of range',parent=window_mode_doo)
                    elif DOO_VPW1<0.1 or DOO_VPW1>1.9:
                        tkinter.messagebox.showerror('Error','VPW is out of range!',parent=window_mode_doo)
                    else:
                        tkinter.messagebox.showinfo('Passed','Values Saved!',parent=window_mode_doo)
                    
                
            def M_AOOR():
                window_mode_aoor = tk.Toplevel(window)
                window_mode_aoor.geometry('500x500')
                window_mode_aoor.title('AOOR is selected!')

                AOOR_LRL1 = AOOR_LRL.get()
                LRL_value = tk.Entry(window_mode_aoor, textvariable = AOOR_LRL, font=('Arial',12))
                LRL_value.place(x=280,y=150)
                tk.Label(window_mode_aoor, text='Lower Rate Limit(Int)(30ppm-175ppm): ').place(x=30,y=150)
                d.update_dict('AOOR_LRL',AOOR_LRL1)

                AOOR_URL1 = AOOR_URL.get()
                URL_value = tk.Entry(window_mode_aoor, textvariable = AOOR_URL, font=('Arial',12))
                URL_value.place(x=280,y=180)
                tk.Label(window_mode_aoor, text='Upper Rate Limit(Int)(50ppm-175ppm): ').place(x=30,y=180)
                d.update_dict('AOOR_URL',AOOR_URL1)

                AOOR_MSR1 = AOOR_MSR.get()
                MSR_value = tk.Entry(window_mode_aoor, textvariable = AOOR_MSR, font=('Arial',12))
                MSR_value.place(x=280,y=210)
                tk.Label(window_mode_aoor, text='Maximum Sensor Rate(Int)(50ppm-175ppm):').place(x=30,y=210)
                d.update_dict('AOOR_MSR',AOOR_MSR1)

                AOOR_AA1 = AOOR_AA.get()
                AA_value = tk.Entry(window_mode_aoor, textvariable = AOOR_AA, font=('Arial',12))
                AA_value.place(x=280,y=240)
                tk.Label(window_mode_aoor, text='Atrial Amplitude(Float)(3.5V-7.0V): ').place(x=30,y=240)
                d.update_dict('AOOR_AA',AOOR_AA1)

                AOOR_APW1 = AOOR_APW.get()
                APW_value = tk.Entry(window_mode_aoor, textvariable = AOOR_APW, font=('Arial',12))
                APW_value.place(x=280,y=270)
                tk.Label(window_mode_aoor, text='Atrial Pulse Width(Float)(0.1ms-1.9ms): ').place(x=30,y=270)
                d.update_dict('AOOR_APW',AOOR_APW1)

                AOOR_AT1 = AOOR_AT.get()
                AT_value = tk.Entry(window_mode_aoor, textvariable = AOOR_AT, font=('Arial',12))
                AT_value.place(x=280,y=300)
                tk.Label(window_mode_aoor, text='Activity Threshold(Int)(1-5000): ').place(x=30,y=300)
                d.update_dict('AOOR_AT',AOOR_AT1)

                AOOR_ReaT1 = AOOR_ReaT.get()
                ReaT_value = tk.Entry(window_mode_aoor, textvariable = AOOR_ReaT, font=('Arial',12))
                ReaT_value.place(x=280,y=330)
                tk.Label(window_mode_aoor, text='Reaction Time(Int)(10sec-50sec): ').place(x=30,y=330)
                d.update_dict('AOOR_ReaT',AOOR_ReaT1)

                AOOR_RF1 = AOOR_RF.get()
                RF_value = tk.Entry(window_mode_aoor, textvariable = AOOR_RF, font=('Arial',12))
                RF_value.place(x=280,y=360)
                tk.Label(window_mode_aoor, text='Response Factor(Int)(1-16): ').place(x=30,y=360)
                d.update_dict('AOOR_RF',AOOR_RF1)

                AOOR_RecT1 = AOOR_RecT.get()
                RecT_value = tk.Entry(window_mode_aoor, textvariable = AOOR_RecT, font=('Arial',12))
                RecT_value.place(x=280,y=390)
                tk.Label(window_mode_aoor, text='Recovery Time(Int)(2min-16min): ').place(x=30,y=390)
                d.update_dict('AOOR_RecT',AOOR_RecT1)

                AOOR_Com = tk.Button(window_mode_aoor, text='AOOR_COMPARE', command=lambda:[M_AOOR(),window_mode_aoor.destroy(),window_mode_selection.destroy(),self.Button()])
                AOOR_Com.place(x=50,y=420)
                if AOOR_LRL1 == 0:
                    print('1')
                else :
                    if AOOR_LRL1<30 or AOOR_LRL1>175:
                        tkinter.messagebox.showerror('Error','LRL is out of range!',parent=window_mode_aoor)
                    elif AOOR_URL1<50 or AOOR_URL1>175:
                        tkinter.messagebox.showerror('Error','URL is out of range!',parent=window_mode_aoor)
                    elif AOOR_MSR1<50 or AOOR_MSR1>175:
                        tkinter.messagebox.showerror('Error','MSR is out of range!',parent=window_mode_aoor)
                    elif AOOR_AA1<3.5 or AOOR_AA1>7.0:
                        tkinter.messagebox.showerror('Error', 'AA is out of range!',parent=window_mode_aoor)
                    elif AOOR_APW1<0.1 or AOOR_APW1>1.9:
                        tkinter.messagebox.showerror('Error', 'APW is out of range!',parent=window_mode_aoor)
                    elif AOOR_AT1<1 or AOOR_AT1>5000:
                        tkinter.messagebox.showerror('Error','AT is out of range!',parent=window_mode_aoor)
                    elif AOOR_ReaT1<10 or AOOR_ReaT1>50:
                        tkinter.messagebox.showerror('Error','ReaT is out of range!',parent=window_mode_aoor)
                    elif AOOR_RF1<1 or AOOR_RF1>16:
                        tkinter.messagebox.showerror('Error', 'RF is out of range!',parent=window_mode_aoor)
                    elif AOOR_RecT1<2 or AOOR_RecT1>16:
                        tkinter.messagebox.showerror('Error', 'RecT is out of range!',parent=window_mode_aoor)
                    else:
                        tkinter.messagebox.showinfo('Passed','Values Saved!',parent=window_mode_aoor)
                    
                   

            def M_AAIR():
                window_mode_aair = tk.Toplevel(window)
                window_mode_aair.geometry('500x600')
                window_mode_aair.title('AAIR is selected!')

                AAIR_LRL1 = AAIR_LRL.get()
                LRL_value = tk.Entry(window_mode_aair, textvariable = AAIR_LRL, font=('Arial',12))
                LRL_value.place(x=280,y=150)
                tk.Label(window_mode_aair, text='Lower Rate Limit(Int)(30ppm-175ppm): ').place(x=30,y=150)
                d.update_dict('AAIR_LRL',AAIR_LRL1)

                AAIR_URL1 = AAIR_URL.get()
                URL_value = tk.Entry(window_mode_aair, textvariable = AAIR_URL, font=('Arial',12))
                URL_value.place(x=280,y=180)
                tk.Label(window_mode_aair, text='Upper Rate Limit(Int)(50ppm-175ppm): ').place(x=30,y=180)
                d.update_dict('AAUR_URL',AAIR_URL1)

                AAIR_MSR1 = AAIR_MSR.get()
                MSR_value = tk.Entry(window_mode_aair, textvariable = AAIR_MSR, font=('Arial',12))
                MSR_value.place(x=280,y=210)
                tk.Label(window_mode_aair, text='Maximum Sensor Rate(Int)(50ppm-175ppm):').place(x=30,y=210)
                d.update_dict('AAIR_MSR',AAIR_MSR1)

                AAIR_AA1 = AAIR_AA.get()
                AA_value = tk.Entry(window_mode_aair, textvariable = AAIR_AA, font=('Arial',12))
                AA_value.place(x=280,y=240)
                tk.Label(window_mode_aair, text='Atrial Amplitude(Float)(3.5V-7.0V): ').place(x=30,y=240)
                d.update_dict('AAIR_AA',AAIR_AA1)

                AAIR_APW1 = AAIR_APW.get()
                APW_value = tk.Entry(window_mode_aair, textvariable = AAIR_APW, font=('Arial',12))
                APW_value.place(x=280,y=270)
                tk.Label(window_mode_aair, text='Atrial Pulse Width(Float)(0.1ms-1.9ms): ').place(x=30,y=270)
                d.update_dict('AAIR_APW',AAIR_APW1)

                AAIR_AT1 = AAIR_AT.get()
                AT_value = tk.Entry(window_mode_aair, textvariable = AAIR_AT, font=('Arial',12))
                AT_value.place(x=280,y=300)
                tk.Label(window_mode_aair, text='Activity Threshold(Int)(1-5000): ').place(x=30,y=300)
                d.update_dict('AAIR_AT',AAIR_AT1)

                AAIR_ReaT1 = AAIR_ReaT.get()
                ReaT_value = tk.Entry(window_mode_aair, textvariable = AAIR_ReaT, font=('Arial',12))
                ReaT_value.place(x=280,y=330)
                tk.Label(window_mode_aair, text='Reaction Time(Int)(10sec-50sec): ').place(x=30,y=330)
                d.update_dict('AAIR_ReaT',AAIR_ReaT1)

                AAIR_RF1 = AAIR_RF.get()
                RF_value = tk.Entry(window_mode_aair, textvariable = AAIR_RF, font=('Arial',12))
                RF_value.place(x=280,y=360)
                tk.Label(window_mode_aair, text='Response Factor(Int)(1-16): ').place(x=30,y=360)
                d.update_dict('AAIR_RF',AAIR_RF1)

                AAIR_RecT1 = AAIR_RecT.get()
                RecT_value = tk.Entry(window_mode_aair, textvariable = AAIR_RecT, font=('Arial',12))
                RecT_value.place(x=280,y=390)
                tk.Label(window_mode_aair, text='Recovery Time(Int)(2min-16min): ').place(x=30,y=390)
                d.update_dict('AAIR_RecT',AAIR_RecT1)


                #Add new variables

                AAIR_AS1 = AAIR_AS.get()
                AS_value = tk.Entry(window_mode_aair, textvariable = AAIR_AS, font=('Arial',12))
                AS_value.place(x=280,y=420)
                tk.Label(window_mode_aair, text='Atrial Sensitivity(Float)(1.0mV-10mV): ').place(x=30,y=420)
                d.update_dict('AAIR_AS',AAIR_AS1)

                AAIR_ARP1 = AAIR_ARP.get()
                ARP_value = tk.Entry(window_mode_aair, textvariable = AAIR_ARP, font=('Arial',12))
                ARP_value.place(x=280,y=450)
                tk.Label(window_mode_aair, text='Atrial Refractory Period(Int)(150ms-500ms): ').place(x=30,y=450)
                d.update_dict('AAIR_AT',AAIR_ARP1)

                AAIR_PVARP1 = AAIR_PVARP.get()
                PVARP_value = tk.Entry(window_mode_aair, textvariable = AAIR_PVARP, font=('Arial',12))
                PVARP_value.place(x=280,y=480)
                tk.Label(window_mode_aair, text='PVARP(Int)(150ms-500ms): ').place(x=30,y=480)
                d.update_dict('AAIR_PVARP',AAIR_PVARP1)

                AAIR_Com = tk.Button(window_mode_aair, text='AAIR_COMPARE', command=lambda:[M_AAIR(),window_mode_aair.destroy(),window_mode_selection.destroy(),self.Button()])
                AAIR_Com.place(x=50,y=510)
                if AAIR_LRL1 == 0:
                    print('1')
                else :
                    if AAIR_LRL1<30 or AAIR_LRL1>175:
                        tkinter.messagebox.showerror('Error','LRL is out of range!',parent=window_mode_aair)
                    elif AAIR_URL1<50 or AAIR_URL1>175:
                        tkinter.messagebox.showerror('Error','URL is out of range!',parent=window_mode_aair)
                    elif AAIR_MSR1<50 or AAIR_MSR1>175:
                        tkinter.messagebox.showerror('Error','MSR is out of range!',parent=window_mode_aair)
                    elif AAIR_AA1<3.5 or AAIR_AA1>7.0:
                        tkinter.messagebox.showerror('Error', 'AA is out of range',parent=window_mode_aair)
                    elif AAIR_APW1<0.1 or AAIR_APW1>1.9:
                        tkinter.messagebox.showerror('Error', 'APW is out of range',parent=window_mode_aair)
                    elif AAIR_AT1<1 or AAIR_AT1>5000:
                        tkinter.messagebox.showerror('Error','AT is out of range!',parent=window_mode_aair)
                    elif AAIR_ReaT1<10 or AAIR_ReaT1>50:
                        tkinter.messagebox.showerror('Error','ReaT is out of range!',parent=window_mode_aair)
                    elif AAIR_RF1<1 or AAIR_RF1>16:
                        tkinter.messagebox.showerror('Error', 'RF is out of range',parent=window_mode_aair)
                    elif AAIR_RecT1<2 or AAIR_RecT1>16:
                        tkinter.messagebox.showerror('Error', 'RecT is out of range',parent=window_mode_aair)
                    elif AAIR_AS1<1 or AAIR_AS1>10:
                        tkinter.messagebox.showerror('Error', 'AS is out of range',parent=window_mode_aair)
                    elif AAIR_ARP1<150 or AAIR_ARP1>500:
                        tkinter.messagebox.showerror('Error', 'ARP is out of range',parent=window_mode_aair)
                    elif AAIR_PVARP1<150 or AAIR_PVARP1>500:
                        tkinter.messagebox.showerror('Error', 'PVARP is out of range',parent=window_mode_aair)
                    else:
                        tkinter.messagebox.showinfo('Passed','Values Saved!',parent=window_mode_aair)
                    
            


                #VOOR

            def M_VOOR():
                window_mode_VOOR = tk.Toplevel(window)
                window_mode_VOOR.geometry('500x500')
                window_mode_VOOR.title('VOOR is selected!')

                VOOR_LRL1 = VOOR_LRL.get()
                LRL_value = tk.Entry(window_mode_VOOR, textvariable = VOOR_LRL, font=('Arial',12))
                LRL_value.place(x=280,y=150)
                tk.Label(window_mode_VOOR, text='Lower Rate Limit(Int)(30ppm-175ppm): ').place(x=30,y=150)
                d.update_dict('VOOR_LRL',VOOR_LRL1)

                VOOR_URL1 = VOOR_URL.get()
                URL_value = tk.Entry(window_mode_VOOR, textvariable = VOOR_URL, font=('Arial',12))
                URL_value.place(x=280,y=180)
                tk.Label(window_mode_VOOR, text='Upper Rate Limit(Int)(50ppm-175ppm): ').place(x=30,y=180)
                d.update_dict('VOOR_URL',VOOR_URL1)

                VOOR_MSR1 = VOOR_MSR.get()
                MSR_value = tk.Entry(window_mode_VOOR, textvariable = VOOR_MSR, font=('Arial',12))
                MSR_value.place(x=280,y=210)
                tk.Label(window_mode_VOOR, text='Maximum Sensor Rate(Int)(50ppm-175ppm):').place(x=30,y=210)
                d.update_dict('VOOR_MSR',VOOR_MSR1)

                VOOR_VA1 = VOOR_VA.get()
                VA_value = tk.Entry(window_mode_VOOR, textvariable = VOOR_VA, font=('Arial',12))
                VA_value.place(x=280,y=240)
                tk.Label(window_mode_VOOR, text='Ventricular Amplitude(Float)(3.5V-7.0V): ').place(x=30,y=240)
                d.update_dict('VOOR_VA',VOOR_VA1)

                VOOR_VPW1 = VOOR_VPW.get()
                VPW_value = tk.Entry(window_mode_VOOR, textvariable = VOOR_VPW, font=('Arial',12))
                VPW_value.place(x=280,y=270)
                tk.Label(window_mode_VOOR, text='Ventricular Pulse Width(Float)(0.1ms-1.9ms): ').place(x=30,y=270)
                d.update_dict('VOOR_VPW',VOOR_VPW1)

                VOOR_AT1 = VOOR_AT.get()
                AT_value = tk.Entry(window_mode_VOOR, textvariable = VOOR_AT, font=('Arial',12))
                AT_value.place(x=280,y=300)
                tk.Label(window_mode_VOOR, text='Activity Threshold(Int)(1-5000): ').place(x=30,y=300)
                d.update_dict('VOOR_AT',VOOR_AT1)

                VOOR_ReaT1 = VOOR_ReaT.get()
                ReaT_value = tk.Entry(window_mode_VOOR, textvariable = VOOR_ReaT, font=('Arial',12))
                ReaT_value.place(x=280,y=330)
                tk.Label(window_mode_VOOR, text='Reaction Time(Int)(10sec-50sec): ').place(x=30,y=330)
                d.update_dict('VOOR_ReaT',VOOR_ReaT1)

                VOOR_RF1 = VOOR_RF.get()
                RF_value = tk.Entry(window_mode_VOOR, textvariable = VOOR_RF, font=('Arial',12))
                RF_value.place(x=280,y=360)
                tk.Label(window_mode_VOOR, text='Response Factor(Int)(1-16): ').place(x=30,y=360)
                d.update_dict('VOOR_RF',VOOR_RF1)

                VOOR_RecT1 = VOOR_RecT.get()
                RecT_value = tk.Entry(window_mode_VOOR, textvariable = VOOR_RecT, font=('Arial',12))
                RecT_value.place(x=280,y=390)
                tk.Label(window_mode_VOOR, text='Recovery Time(Int)(2min-16min): ').place(x=30,y=390)
                d.update_dict('VOOR_RecT',VOOR_RecT1)

                VOOR_Com = tk.Button(window_mode_VOOR, text='VOOR_COMPARE', command=lambda:[M_VOOR(),window_mode_VOOR.destroy(),window_mode_selection.destroy(),self.Button()])
                VOOR_Com.place(x=50,y=420)
                if VOOR_LRL1 == 0:
                    print('1')
                else :
                    if VOOR_LRL1<30 or VOOR_LRL1>175:
                        tkinter.messagebox.showerror('Error','LRL is out of range!',parent=window_mode_VOOR)
                    elif VOOR_URL1<50 or VOOR_URL1>175:
                        tkinter.messagebox.showerror('Error','URL is out of range!',parent=window_mode_VOOR)
                    elif VOOR_MSR1<50 or VOOR_MSR1>175:
                        tkinter.messagebox.showerror('Error','MSR is out of range!',parent=window_mode_VOOR)
                    elif VOOR_VA1<3.5 or VOOR_VA1>7.0:
                        tkinter.messagebox.showerror('Error', 'VA is out of range',parent=window_mode_VOOR)
                    elif VOOR_VPW1<0.1 or VOOR_VPW1>1.9:
                        tkinter.messagebox.showerror('Error', 'VPW is out of range',parent=window_mode_VOOR)
                    elif VOOR_AT1<1 or VOOR_AT1>5000:
                        tkinter.messagebox.showerror('Error','AT is out of range!',parent=window_mode_VOOR)
                    elif VOOR_ReaT1<10 or VOOR_ReaT1>50:
                        tkinter.messagebox.showerror('Error','ReaT is out of range!',parent=window_mode_VOOR)
                    elif VOOR_RF1<1 or VOOR_RF1>16:
                        tkinter.messagebox.showerror('Error', 'RF is out of range',parent=window_mode_VOOR)
                    elif VOOR_RecT1<2 or VOOR_RecT1>16:
                        tkinter.messagebox.showerror('Error', 'RecT is out of range',parent=window_mode_VOOR)
                    else:
                        tkinter.messagebox.showinfo('Passed','Values Saved!',parent=window_mode_VOOR)
                    
                    
            



            def M_VVIR():
                window_mode_VVIR = tk.Toplevel(window)
                window_mode_VVIR.geometry('500x550')
                window_mode_VVIR.title('VVIR is selected!')

                VVIR_LRL1 = VVIR_LRL.get()
                LRL_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_LRL, font=('Arial',12))
                LRL_value.place(x=280,y=150)
                tk.Label(window_mode_VVIR, text='Lower Rate Limit(Int)(30ppm-175ppm): ').place(x=30,y=150)
                d.update_dict('VVIR_LRL',VVIR_LRL1)

                VVIR_URL1 = VVIR_URL.get()
                URL_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_URL, font=('Arial',12))
                URL_value.place(x=280,y=180)
                tk.Label(window_mode_VVIR, text='Upper Rate Limit(Int)(50ppm-175ppm): ').place(x=30,y=180)
                d.update_dict('VVIR_URL',VVIR_URL1)

                VVIR_MSR1 = VVIR_MSR.get()
                MSR_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_MSR, font=('Arial',12))
                MSR_value.place(x=280,y=210)
                tk.Label(window_mode_VVIR, text='Maximum Sensor Rate(Int)(50ppm-175ppm):').place(x=30,y=210)
                d.update_dict('VVIR_MSR',VVIR_MSR1)

                VVIR_VA1 = VVIR_VA.get()
                VA_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_VA, font=('Arial',12))
                VA_value.place(x=280,y=240)
                tk.Label(window_mode_VVIR, text='Ventricular Amplitude(Float)(3.5V-7.0V): ').place(x=30,y=240)
                d.update_dict('VVIR_VA',VVIR_VA1)

                VVIR_VPW1 = VVIR_VPW.get()
                VPW_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_VPW, font=('Arial',12))
                VPW_value.place(x=280,y=270)
                tk.Label(window_mode_VVIR, text='Ventricular Pulse Width(Float)(0.1ms-1.9ms): ').place(x=30,y=270)
                d.update_dict('VVIR_VPW',VVIR_VPW1)

                VVIR_AT1 = VVIR_AT.get()
                AT_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_AT, font=('Arial',12))
                AT_value.place(x=280,y=300)
                tk.Label(window_mode_VVIR, text='Activity Threshold(Int)(1-5000): ').place(x=30,y=300)
                
                d.update_dict('VVIR_AT',VVIR_AT1)

                VVIR_ReaT1 = VVIR_ReaT.get()
                ReaT_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_ReaT, font=('Arial',12))
                ReaT_value.place(x=280,y=330)
                tk.Label(window_mode_VVIR, text='Reaction Time(Int)(10sec-50sec): ').place(x=30,y=330)
                d.update_dict('VVIR_ReaT',VVIR_ReaT1)

                VVIR_RF1 = VVIR_RF.get()
                RF_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_RF, font=('Arial',12))
                RF_value.place(x=280,y=360)
                tk.Label(window_mode_VVIR, text='Response Factor(Int)(1-16): ').place(x=30,y=360)
                d.update_dict('VVIR_RF',VVIR_RF1)

                VVIR_RecT1 = VVIR_RecT.get()
                RecT_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_RecT, font=('Arial',12))
                RecT_value.place(x=280,y=390)
                tk.Label(window_mode_VVIR, text='Recovery Time(Int)(2min-16min): ').place(x=30,y=390)
                d.update_dict('VVIR_RecT',VVIR_RecT1)

                VVIR_VS1 = VVIR_VS.get()
                VS_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_VS, font=('Arial',12))
                VS_value.place(x=280,y=420)
                tk.Label(window_mode_VVIR, text='Ventricular Sensitivity(Float)(0.1mV-10mV): ').place(x=30,y=420)
                d.update_dict('VVIR_VS',VVIR_VS1)

                VVIR_VRP1 = VVIR_VRP.get()
                VRP_value = tk.Entry(window_mode_VVIR, textvariable = VVIR_VRP, font=('Arial',12))
                VRP_value.place(x=280,y=450)
                tk.Label(window_mode_VVIR, text='Ventricular Refractory Period(Int)(150-500ms): ').place(x=30,y=450)
                d.update_dict('VVIR_VRP',VVIR_VRP1)

                VVIR_Com = tk.Button(window_mode_VVIR, text='VVIR_COMPARE', command=lambda:[M_VVIR(),window_mode_VVIR.destroy(),window_mode_selection.destroy(),self.Button()])
                VVIR_Com.place(x=50,y=480)
                if VVIR_LRL1 == 0:
                    print('1')
                else :
                    if VVIR_LRL1<30 or VVIR_LRL1>175:
                        tkinter.messagebox.showerror('Error','LRL is out of range!',parent=window_mode_VVIR)
                    elif VVIR_URL1<50 or VVIR_URL1>175:
                        tkinter.messagebox.showerror('Error','URL is out of range!',parent=window_mode_VVIR)
                    elif VVIR_MSR1<50 or VVIR_MSR1>175:
                        tkinter.messagebox.showerror('Error','MSR is out of range!',parent=window_mode_VVIR)
                    elif VVIR_VA1<3.5 or VVIR_VA1>7.0:
                        tkinter.messagebox.showerror('Error', 'VA is out of range',parent=window_mode_VVIR)
                    elif VVIR_VPW1<0.1 or VVIR_VPW1>1.9:
                        tkinter.messagebox.showerror('Error', 'VPW is out of range',parent=window_mode_VVIR)
                    elif VVIR_AT1<1 or VVIR_AT1>5000:
                        tkinter.messagebox.showerror('Error','AT is out of range!',parent=window_mode_VVIR)
                    elif VVIR_ReaT1<10 or VVIR_ReaT1>50:
                        tkinter.messagebox.showerror('Error','ReaT is out of range!',parent=window_mode_VVIR)
                    elif VVIR_RF1<1 or VVIR_RF1>16:
                        tkinter.messagebox.showerror('Error', 'RF is out of range',parent=window_mode_VVIR)
                    elif VVIR_RecT1<2 or VVIR_RecT1>16:
                        tkinter.messagebox.showerror('Error', 'RecT is out of range',parent=window_mode_VVIR)
                    elif VVIR_VS1<1 or VVIR_VS1>10:
                        tkinter.messagebox.showerror('Error', 'VS is out of range',parent=window_mode_VVIR)
                    elif VVIR_VRP1<150 or VVIR_VRP1>500:
                        tkinter.messagebox.showerror('Error', 'VRP is out of range',parent=window_mode_VVIR)
                    else:
                        tkinter.messagebox.showinfo('Passed','Values Saved!',parent=window_mode_VVIR)
                
                

            def M_DOOR():
                window_mode_DOOR = tk.Toplevel(window)
                window_mode_DOOR.geometry('500x600')
                window_mode_DOOR.title('DOOR is selected!')

                DOOR_LRL1 = DOOR_LRL.get()
                LRL_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_LRL, font=('Arial',12))
                LRL_value.place(x=280,y=150)
                tk.Label(window_mode_DOOR, text='Lower Rate Limit(Int)(30ppm-175ppm): ').place(x=30,y=150)
                d.update_dict('DOOR_LRL',DOOR_LRL1)

                DOOR_URL1 = DOOR_URL.get()
                URL_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_URL, font=('Arial',12))
                URL_value.place(x=280,y=180)
                tk.Label(window_mode_DOOR, text='Upper Rate Limit(Int)(50ppm-175ppm): ').place(x=30,y=180)
                d.update_dict('DOOR_URL',DOOR_URL1)

                DOOR_MSR1 = DOOR_MSR.get()
                MSR_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_MSR, font=('Arial',12))
                MSR_value.place(x=280,y=210)
                tk.Label(window_mode_DOOR, text='Maximum Sensor Rate(Int)(50ppm-175ppm):').place(x=30,y=210)
                d.update_dict('DOOR_MSR',DOOR_MSR1)

                DOOR_VA1 = DOOR_VA.get()
                VA_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_VA, font=('Arial',12))
                VA_value.place(x=280,y=240)
                tk.Label(window_mode_DOOR, text='Ventricular Amplitude(Float)(3.5V-7.0V): ').place(x=30,y=240)
                d.update_dict('DOOR_VA',DOOR_VA1)

                DOOR_VPW1 = DOOR_VPW.get()
                VPW_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_VPW, font=('Arial',12))
                VPW_value.place(x=280,y=270)
                tk.Label(window_mode_DOOR, text='Ventricular Pulse Width(Float)(0.1ms-1.9ms): ').place(x=30,y=270)
                d.update_dict('DOOR_VPW',DOOR_VPW1)

                DOOR_AT1 = DOOR_AT.get()
                AT_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_AT, font=('Arial',12))
                AT_value.place(x=280,y=300)
                tk.Label(window_mode_DOOR, text='Activity Threshold(Int)(1-5000): ').place(x=30,y=300)
                d.update_dict('DOOR_AT',DOOR_AT1)

                DOOR_ReaT1 = DOOR_ReaT.get()
                ReaT_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_ReaT, font=('Arial',12))
                ReaT_value.place(x=280,y=330)
                tk.Label(window_mode_DOOR, text='Reaction Time(Int)(10sec-50sec): ').place(x=30,y=330)
                d.update_dict('DOOR_ReaT',DOOR_ReaT1)

                DOOR_RF1 = DOOR_RF.get()
                RF_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_RF, font=('Arial',12))
                RF_value.place(x=280,y=360)
                tk.Label(window_mode_DOOR, text='Response Factor(Int)(1-16): ').place(x=30,y=360)
                d.update_dict('DOOR_RF',DOOR_RF1)

                DOOR_RecT1 = DOOR_RecT.get()
                RecT_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_RecT, font=('Arial',12))
                RecT_value.place(x=280,y=390)
                tk.Label(window_mode_DOOR, text='Recovery Time(Int)(2min-16min): ').place(x=30,y=390)
                d.update_dict('DOOR_RecT',DOOR_RecT1)

                DOOR_FAVD1 = DOOR_FAVD.get()
                FAVD_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_FAVD, font=('Arial',12))
                FAVD_value.place(x=280,y=420)
                tk.Label(window_mode_DOOR, text='Fixed AV Delay(Int)(70ms-300ms)').place(x=30,y=420)
                d.update_dict('DOOR_FAVD',DOOR_FAVD1)

                DOOR_AA1 = DOOR_AA.get()
                AA_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_AA, font=('Arial',12))
                AA_value.place(x=280,y=450)
                tk.Label(window_mode_DOOR, text='Atrial Amplitude(Float)(3.5V-7.0V): ').place(x=30,y=450)
                d.update_dict('DOOR_AA',DOOR_AA1)

                DOOR_APW1 = DOOR_APW.get()
                APW_value = tk.Entry(window_mode_DOOR, textvariable = DOOR_APW, font=('Arial',12))
                APW_value.place(x=280,y=480)
                tk.Label(window_mode_DOOR, text='Atrial Pulse Width(Float)(0.1ms-1.9ms): ').place(x=30,y=480)
                d.update_dict('DOOR_APW',DOOR_APW1)

                DOOR_Com = tk.Button(window_mode_DOOR, text='DOOR_COMPARE', command=lambda:[M_DOOR(),window_mode_DOOR.destroy(),window_mode_selection.destroy(),self.Button()])
                DOOR_Com.place(x=50,y=510)
                if DOOR_LRL1 == 0:
                    print('1')
                else :
                    if DOOR_LRL1<30 or DOOR_LRL1>175:
                        tkinter.messagebox.showerror('Error','LRL is out of range!',parent=window_mode_DOOR)
                    elif DOOR_URL1<50 or DOOR_URL1>175:
                        tkinter.messagebox.showerror('Error','URL is out of range!',parent=window_mode_DOOR)
                    elif DOOR_MSR1<50 or DOOR_MSR1>175:
                        tkinter.messagebox.showerror('Error','MSR is out of range!',parent=window_mode_DOOR)
                    elif DOOR_VA1<3.5 or DOOR_VA1>7.0:
                        tkinter.messagebox.showerror('Error', 'VA is out of range',parent=window_mode_DOOR)
                    elif DOOR_VPW1<0.1 or DOOR_VPW1>1.9:
                        tkinter.messagebox.showerror('Error', 'VPW is out of range',parent=window_mode_DOOR)
                    elif DOOR_AT1<1 or DOOR_AT1>5000:
                        tkinter.messagebox.showerror('Error','AT is out of range!',parent=window_mode_DOOR)
                    elif DOOR_ReaT1<10 or DOOR_ReaT1>50:
                        tkinter.messagebox.showerror('Error','ReaT is out of range!',parent=window_mode_DOOR)
                    elif DOOR_RF1<1 or DOOR_RF1>16:
                        tkinter.messagebox.showerror('Error', 'RF is out of range',parent=window_mode_DOOR)
                    elif DOOR_RecT1<2 or DOOR_RecT1>16:
                        tkinter.messagebox.showerror('Error', 'RecT is out of range',parent=window_mode_DOOR)
                    elif DOOR_FAVD1<70 or DOOR_FAVD1>300:
                        tkinter.messagebox.showerror('Error', 'FAVD is out of range',parent=window_mode_DOOR)
                    elif DOOR_AA1<3.5 or DOOR_AA1>7.0:
                        tkinter.messagebox.showerror('Error', 'AA is out of range',parent=window_mode_DOOR)
                    elif DOOR_APW1<0.1 or DOOR_APW1>1.9:
                        tkinter.messagebox.showerror('Error', 'APW is out of range',parent=window_mode_DOOR)
                    else:
                        tkinter.messagebox.showinfo('Passed','Values Saved!',parent=window_mode_DOOR)
                    
                   






            


            AOO_Bu = tk.Button(window_mode_selection, text='AOO_Bu', command= M_AOO)
            AOO_Bu.place(x=120,y=180)
            
            VOO_Bu = tk.Button(window_mode_selection, text='VOO_Bu',command= M_VOO)
            VOO_Bu.place(x=200,y=180)
            
            AAI_Bu = tk.Button(window_mode_selection, text='AAI_Bu', command= M_AAI)
            AAI_Bu.place(x=280,y=180)


            VVI_Bu = tk.Button(window_mode_selection, text='VVI_Bu',command= M_VVI)
            VVI_Bu.place(x=360,y=180)

            DOO_Bu = tk.Button(window_mode_selection, text='DOO_Bu',command= M_DOO)
            DOO_Bu.place(x=440,y=180)

            AOOR_Bu = tk.Button(window_mode_selection, text='AOOR_Bu',command= M_AOOR)
            AOOR_Bu.place(x=120,y=220)

            AAIR_Bu = tk.Button(window_mode_selection, text='AAIR_Bu',command= M_AAIR)
            AAIR_Bu.place(x=200,y=220)
                
            VOOR_Bu = tk.Button(window_mode_selection, text='VOOR_Bu',command= M_VOOR)
            VOOR_Bu.place(x=280,y=220)
                    
            VVIR_Bu = tk.Button(window_mode_selection, text='VVIR_Bu',command= M_VVIR)
            VVIR_Bu.place(x=360,y=220)

            DOOR_Bu = tk.Button(window_mode_selection, text='DOOR_Bu',command= M_DOOR)
            DOOR_Bu.place(x=440,y=220)

            data_scroll()
        
        

    

    



class LoginPage:
    
    def register_deviceID(self):
        
        def save_deviceID():

            try:
                with open('devices_info.txt','r') as device_file:
                    device_info = json.load(device_file)

            except FileNotFoundError:
                with open('devices_info.txt','w') as device_file:
                    device_info = {'DeviceID':'anyid'}
                    json.dump(device_info, device_file)
                    device_file.close()

            idd = banzai.get()

            with open('devices_info.txt','r')as device_file:
                device_info = json.load(device_file)

            if idd in device_info.values():
                tkinter.messagebox.showerror('Error','The device has already registered!')
                
                var_connect[0]=0
            else:
        
                device_info['DeviceID'] = idd
                with open('devices_info.txt','w') as device_file:
                    json.dump(device_info, device_file)
                    
                tkinter.messagebox.showinfo('Welcome','You have successfully saved your device!')
                
                var_connect[0] = 1
                
                window_save_device.destroy()


        window_save_device = tk.Toplevel(window)
        window_save_device.geometry('300x150')
        window_save_device.title('Register your device')
        
        btn_save_device = tk.Button(window_save_device, text='Save Device',command=save_deviceID)
        btn_save_device.place(x=10,y=100)

        banzai = tk.StringVar()
        tk.Label(window_save_device, text='enter the ID in string form').place(x=10,y=30)
        banzai_entry = tk.Entry(window_save_device, textvariable=banzai)
        banzai_entry.place(x=10, y = 60)
        
        #define user login function:
    def usr_login(self):
        usr_name = var_usr_name.get()
        usr_pwd = var_usr_pwd.get()
        

        try:
            with open('usrs_info.pickle','rb') as usr_file:
                usrs_info = pickle.load(usr_file)

        except FileNotFoundError:  

            with open('usrs_info.pickle','wb') as usr_file:
                usrs_info = {'admin':'admin'}
                pickle.dump(usrs_info, usr_file)
                usr_file.close()

        #if user name and password match the record in the file, login success
        if usr_name in usrs_info:
            if usr_pwd == usrs_info[usr_name]:
                tkinter.messagebox.showinfo(title='Welcome',message='You have logged into the pacemaker monitor center!'+usr_name)
                m = Mode()
                m.Button()

            else:
                tkinter.messagebox.showerror(message='Error, your password is wrong, try again!')

        else:
            is_sign_up = tkinter.messagebox.askyesno('Welcome! ','You have not registered yet. Sign up now?')

            if is_sign_up:
                LoginPage.usr_sign_up(self)



    # define usr registration function
    def usr_sign_up(self):
        def sign_to_pacemaker_MonitorCenter():
            np = new_pwd.get()
            npf = new_pwd_confirm.get()
            nn = new_name.get()

            with open('usrs_info.pickle','rb')as usr_file:
                exist_usr_info = pickle.load(usr_file)

            if np != npf:
                tkinter.messagebox.showerror('Error','Password and confirm password must be the same!')
            
            elif nn in exist_usr_info:
                tkinter.messagebox.showerror('Error','The user has already signed up!')

            else:

                try:
                    with open('usr_number.txt','r') as number_file:
                        usr_number = json.load(number_file)

                    
                except FileNotFoundError:  

                    with open('usr_number.txt','w') as number_file:
                        usr_number = {'userNumbers':0}
                        json.dump(usr_number, number_file)
                        number_file.close()


                with open('usr_number.txt','r') as number_file:
                    usr_number = json.load(number_file)
                    
                if usr_number['userNumbers'] < 1:
                    usr_number['userNumbers'] += 1
                    with open('usr_number.txt','w') as number_file:
                        json.dump(usr_number, number_file)
                        number_file.close()

                    exist_usr_info[nn] = np
                    with open('usrs_info.pickle','wb') as usr_file:
                        pickle.dump(exist_usr_info, usr_file)
                    
                    tkinter.messagebox.showinfo('Welcome','You have successfully signed up!')

                else:
                    tkinter.messagebox.showinfo('Error','Maximum Users of 10 has reached! Sign in failed!')
                    number_file.close()


                window_sign_up.destroy()


        window_sign_up = tk.Toplevel(window)
        window_sign_up.geometry('300x200')
        window_sign_up.title('Sign up window')

        new_name = tk.StringVar()
        new_name.set('example@mcmaster.ca')
        tk.Label(window_sign_up, text='User name: ').place(x=10,y=10)
        entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
        entry_new_name.place(x=130, y=10)

        new_pwd = tk.StringVar()
        tk.Label(window_sign_up, text='Password: ').place(x=10,y=50)
        entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
        entry_usr_pwd.place(x=130,y=50)

        new_pwd_confirm = tk.StringVar()
        tk.Label(window_sign_up, text='Confirm Password: ').place(x=10,y=90)
        entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
        entry_usr_pwd_confirm.place(x=130,y=90)

        btn_confirm_sign_up = tk.Button(window_sign_up, text='Sign up', command=sign_to_pacemaker_MonitorCenter)
        btn_confirm_sign_up.place(x=180,y=130)
myButton = LoginPage()
btn_login = tk.Button(window, text='Login', command=myButton.usr_login)
btn_login.place(x=120,y=240)
btn_sign_up = tk.Button(window, text='Sign up',command=myButton.usr_sign_up)
btn_sign_up.place(x=200,y=240)
#btn_sign_up = tk.Button(window, text='Register Device',command=myButton.register_deviceID)
#btn_sign_up.place(x=280,y=240)

window.mainloop()

