import tkinter as tk
import tkinter.messagebox
import pickle
import json


global window 
window = tk.Tk()
status = window 
window.title('Welcome to 3K04!')
window.geometry('400x300')
from Mode import Button
from Mode import ini_file
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
var_connect = [5,6]

data = ini_file();
#Mode Selection Function
#AOO
global AOO_LRL1
AOO_LRL1 = -1
AOO_LRL = tk.IntVar();

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
VOO_LRL = tk.IntVar();

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
VVI_LRL = tk.IntVar();

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
AAI_LRL = tk.IntVar();

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

global data_dict

global usrLimit


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
                
                var_connect[1]=0
                print(var_connect[1])
            else:
        
                device_info['DeviceID'] = idd
                with open('devices_info.txt','w') as device_file:
                    json.dump(device_info, device_file)
                    
                tkinter.messagebox.showinfo('Welcome','You have successfully saved your device!')
                
                var_connect[1] = 1
                print(var_connect)
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
                start = Button(status,var_connect)
                
                
                

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
btn_sign_up = tk.Button(window, text='Register Device',command=myButton.register_deviceID)
btn_sign_up.place(x=280,y=240)

window.mainloop()





fuckpu