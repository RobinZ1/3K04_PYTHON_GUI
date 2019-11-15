#Tutorial

#initialize a window
'''
import tkinter as tk

window = tk.Tk()

window.title('My Window')

window.geometry('500x300')

l = tk.Label(window, text='Banzai!',bg = 'green',font=('Arial',12),width=30,height=2)

l.pack()

window.mainloop()

'''


'''
# register a button with command--------------

import tkinter as tk

window = tk.Tk()

window.title('My Window')

window.geometry('500x300')

var = tk.StringVar()

l = tk.Label(window, textvariable = var, bg = 'green', fg = 'white', font = ('Arial',12), width = 30, height = 2)

l.pack()

on_hit = False

def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('You hit me!')
    else:
        on_hit = False;
        var.set('');

b = tk.Button(window, text='hit me', font = ('Arial',12), width = 10, height = 1, command=hit_me)

b.pack() #place the button

window.mainloop()
'''

# Entry 是 tkinter类中提供的一个单行文本输入域，用来输入显示一行文本，收集键盘输入
'''
import tkinter as tk

window = tk.Tk()

window.title('My Window')

window.geometry('500x300')

e1 = tk.Entry(window, show='*', font=('Arial',14))
e2 = tk.Entry(window, show='h',font=('Arial',14))
e1.pack()
e2.pack()

window.mainloop()
'''

# Text-----------
'''
import tkinter as tk

window = tk.Tk()
window.title('My Window') 
window.geometry('500x300')
e = tk.Entry(window, show=None)
e.pack()

def insert_point():
    var = e.get()
    t.insert('insert',var)

def insert_end():
    var = e.get()
    t.insert('end',var)

b1 = tk.Button(window, text='insert point', width = 10, height = 2, command=insert_point)
b1.pack()
b2 = tk.Button(window, text='insert back',width = 10, height = 2, command=insert_end)
b2.pack()

t = tk.Text(window, height = 3)
t.pack()

window.mainloop()
'''

# Listbox
'''
import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

var1 = tk.StringVar()
l = tk.Label(window, bg='green',fg='white',font=('Arial',12),width=10, textvariable = var1)
l.pack()

def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)

b1 = tk.Button(window, text='print selection',width=15, height=2, command=print_selection)
b1.pack()


var2 = tk.StringVar()
var2.set((1,2,3,4))

lb = tk.Listbox(window, listvariable=var2)
list_items = [11,22,33,44]
for item in list_items:
    lb.insert('end',item)

lb.insert(1,'first')
lb.insert(2,'second')
lb.delete(2)
lb.pack()
 
window.mainloop()
'''


# Radiobutton 代表一个变量， 它可以有多个值中的一个， 点击它将为这个变量设置值，并且清除与这同一变量相关的其他radiobutton
'''
import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')
var = tk.StringVar()
l = tk.Label(window, bg='yellow',width=20,text='empty')
l.pack()
def print_selection():
    l.config(text='you have selected '+var.get())

r1 = tk.Radiobutton(window, text='Option A',variable = var, value='A', command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='Option B',variable = var, value='B',command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='Option C',variable =var, value='C',command=print_selection)
r3.pack()

window.mainloop()
'''

#Checkbutton  代表一个变量，有个不同的值，点击这个按钮将会在这两这个值间切换，选择和取消选择
'''
import tkinter as tk
window = tk.Tk()
window.title('My Window')
window.geometry('500x300')
l = tk.Label(window, bg='yellow',width=20,text='empty')
l.pack()

def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love only Python')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love only C++')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='I do not love either')
    else:
        l.config(text='I love both!')

var1 = tk.IntVar()
var2 = tk.IntVar()

c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue = 1, offvalue = 0, command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window, text='C++', variable = var2, onvalue = 1, offvalue = 0, command = print_selection)
c2.pack()

window.mainloop()
'''


# Scale
'''
import tkinter as tk

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')
l = tk.Label(window, bg = 'green', fg='white', width=20, text='empty')
l.pack()

def print_selection(v):
    l.config(text='You have selected'+v)
    
s = tk.Scale(window, label='try me', from_ =0, to= 10, orient=tk.HORIZONTAL, length=200, showvalue=0, tickinterval=2, resolution=0.01, command=print_selection)
s.pack()

window.mainloop()
'''

# Canvas
'''
import tkinter as tk
window = tk.Tk()
window.title('My Window')
window.geometry('500x300')
canvas = tk.Canvas(window, bg='green',height=200, width=500)
image_file = tk.PhotoImage(file='pic.gif') #must be in the same folder
image = canvas.create_image(250, 0, anchor='n', image=image_file)

x0, y0, x1, y1 = 100,100,150,150
line = canvas.create_line(x0-50, y0-50, x1-50, y1-50)
oval = canvas.create_oval(x0+120, y0+50, x1+120, y1+50, fill='yellow')
arc = canvas.create_arc(x0, y0+50, x1, y1+50, start=0, extent = 180)
rect = canvas.create_rectangle(330, 30, 330+20, 30+20)
canvas.pack()

def moveit():
    canvas.move(rect, 2, 2)

b = tk.Button(window, text='move item', command=moveit).pack()

window.mainloop()
'''




# Menu
'''
import tkinter as tk
window = tk.Tk()
window.title()
window.geometry('500x300')
l = tk.Label(window, text=' ', bg='green')
l.pack()

counter = 0
def do_job():
    global counter
    l.config(text='do '+str(counter))
    counter += 1

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu = filemenu)

filemenu.add_command(label='New',command=do_job)
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=window.quit)

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit',menu=editmenu)

editmenu.add_command(label='Cut',command=do_job)
editmenu.add_command(label='Copy',command=do_job)
editmenu.add_command(label='Paste',command=do_job)

submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='Import',menu=submenu, underline=0)

submenu.add_command(label='Submenu_1', command=do_job)


window.config(menu = menubar)
window.mainloop()
'''


#Frame 
'''
import tkinter as tk
window = tk.Tk()
window.title('My Window')
window.geometry('500x300')
tk.Label(window, text = 'On the window', bg='red', font=('Arial',16)).pack()

frame = tk.Frame(window)
frame.pack()
frame_l = tk.Frame(frame)
frame_r = tk.Frame(frame)
frame_l.pack(side='left')
frame_r.pack(side='right')

tk.Label(frame_l, text='on the frame_l1', bg='green').pack()
tk.Label(frame_l, text='on the frame_l2', bg='green').pack()
tk.Label(frame_l, text='on the frame_l3', bg='green').pack()
tk.Label(frame_r, text='on the frame_r1', bg='yellow').pack()
tk.Label(frame_r, text='on the frame_r2', bg='yellow').pack()
tk.Label(frame_r, text='on the frame_r3', bg='yellow').pack()

window.mainloop()

'''

# messageBox
'''
import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')

def hit_me():
    #tkinter.messagebox.showinfo(title='Hi',message='你好！')
    #tkinter.messagebox.showwarning(title='Hi',messange='警告')
    #tkinter.messagebox.showerror(title='Hi',messange='错误')
    print(tkinter.messagebox.askquestion(title='Hi',message='你好'))
    #print(tkinter.messagebox.askyesno(title='Hi', message='你好'))

tk.Button(window, text='hit me', bg='green',font=('Arial',14), command=hit_me).pack()

window.mainloop()
'''

# The Grid/Pack/Place geometry Manager

# Real Practice, Dynamic Login page

'''编写一个用户登录界面， 用户可以登录账户信息，如果账户已经存在，
可以直接登录， 登录名或者登录密码输入错误会提示， 如果账户不存在，
提示用户注册，点击注册进去注册页面， 输入注册信息，确定后便可以返回
登录界面进行登录
'''

import tkinter as tk
import tkinter.messagebox
import pickle
import json

window = tk.Tk()

window.title('Welcome to 3K04!')

window.geometry('400x300')

# welcome page
canvas = tk.Canvas(window, width=400, height=135, bg='green')
image_file = tk.PhotoImage(file='3k04.gif')
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

global AAI_VPW1
AAI_VPW1 = -1
AAI_VPW = tk.DoubleVar()

global AAI_VRP1
AAI_VRP1 = -1
AAI_VRP = tk.DoubleVar()

global data_dict

global usrLimit



def update_dict(string, value):
    with open('test_data.txt', 'r') as json_file:
        data_dict = json.load(json_file)
        print("updated\n")
        print(data_dict)
        data_dict[string] = value
        print(data_dict)
    with open('test_data.txt', 'w') as json_file:
        json.dump(data_dict, json_file)
        json_file.close()

# def update_usr():
#     with open('test_data.txt','r') as json_file:
#         data_dict = json.load(json_file)
#         return False

#         if data_dict['UsrNumbers'] > 2:
#             json_file.close()
#             return False
#         else:
#             with open('test_data.txt','w') as json_file:
#                 data_dict['UsrNumbers'] += 1
#                 json.dump(data_dict, json_file)
#                 json_file.close()
#             return True




def ini_file():
    
    data_dict = {'AOO_LRL':AOO_LRL1, 'AOO_URL': AOO_URL1, 'AOO_AA': AOO_AA1,'AOO_APW':AOO_APW1,'VOO_LRL':VOO_LRL1,'VOO_URL':VOO_URL1,'VOO_VA':VOO_VA1,'VOO_VPW':VOO_VPW1,'AAI_LRL':AAI_LRL1,'AAI_URL':AAI_URL1,'AAI_AA':AAI_AA1,'AAI_VPW':AAI_VPW1,'AAI_VRP':AAI_VRP1,'VVI_LRL':VVI_LRL1,'VVI_URL':VVI_URL1,'VVI_VA':VVI_VA1,'VVI_VPW':VVI_VPW1,'VVI_VRP':VVI_VRP1}
    with open('test_data.txt','w') as json_file:
        json.dump(data_dict, json_file) #the data_dict is now converted to JSON string 

ini_file()

def Mode_selection():

    
    
 #Parameters Interface
    
    window_mode_selection = tk.Toplevel(window)
    window_mode_selection.geometry('600x500')
    window_mode_selection.title('Mode Selection')

#Device connection

    var_device_name = tk.StringVar()
    entry_device_name = tk.Entry(window_mode_selection, textvariable=var_device_name, font=('Arial',14))
    entry_device_name.place(x=200,y=175)
    tk.Label(window_mode_selection, text='Device is connecting',font=('Arial',12)).place(x=200,y=100)
    tk.Label(window_mode_selection, text='Device',font=('Arial',12)).place(x=140,y=175)
  
    def Mode_AOO():

        window_mode_aoo = tk.Toplevel(window)
        window_mode_aoo.geometry('500x500')
        window_mode_aoo.title('AOO is selected!')

        
        
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
        
        # btn_return = tk.Button(window_mode_aoo, text='saved', command=saved_and_return)
        # btn_return.place(x=230,y=300)

    '''VOO'''
    def Mode_VOO():
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
       
    '''AAI'''
    def Mode_AAI():
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

    '''VVI'''
    def Mode_VVI():
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

    AOO_Bu = tk.Button(window_mode_selection, text='AOO_Bu', command=Mode_AOO)
    AOO_Bu.place(x=120,y=240)
    
    VOO_Bu = tk.Button(window_mode_selection, text='VOO_Bu',command=Mode_VOO)
    VOO_Bu.place(x=200,y=240)

    AAI_Bu = tk.Button(window_mode_selection, text='AAI_Bu', command=Mode_AAI)
    AAI_Bu.place(x=280,y=240)

    VVI_Bu = tk.Button(window_mode_selection, text='VVI_Bu',command=Mode_VVI)
    VVI_Bu.place(x=360,y=240)

    









#define user login function:
def usr_login():
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
            tkinter.messagebox.showinfo(title='Welcome',message='You have signed into the pacemaker monitor center!'+usr_name)
            Mode_selection()


        else:
            tkinter.messagebox.showerror(message='Error, your password is wrong, try again!')

    else:
        is_sign_up = tkinter.messagebox.askyesno('Welcome! ','You have not registered yet. Sign up now?')

        if is_sign_up:
            usr_sign_up()






''''''

def register_deviceID():

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

        else:
            # print('time to select')
            # if update_usr():
            #     tkinter.messagebox.showinfo(title='Sign Up Failed!',message='You have reached the maximum number of users')
            #     with open('test_data.txt','r'):
            #         print(data_dict['UsrNumbers'])
            #     btn_return = tk.Button(window, text='back to main page', command = window_sign_up.destroy())
            #     btn_return.place(x=130,y=200)

            # else:
    
            device_info['DeviceID'] = idd
            with open('devices_info.txt','w') as device_file:
                json.dump(device_info, device_file)
                
            tkinter.messagebox.showinfo('Welcome','You have successfully saved your device!')

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

''''''




# define usr registration function
def usr_sign_up():
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
            # print('time to select')
            # if update_usr():
            #     tkinter.messagebox.showinfo(title='Sign Up Failed!',message='You have reached the maximum number of users')
            #     with open('test_data.txt','r'):
            #         print(data_dict['UsrNumbers'])
            #     btn_return = tk.Button(window, text='back to main page', command = window_sign_up.destroy())
            #     btn_return.place(x=130,y=200)

            # else:
    
            exist_usr_info[nn] = np
            with open('usrs_info.pickle','wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
                
            tkinter.messagebox.showinfo('Welcome','You have successfully signed up!')

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

btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=120,y=240)
btn_sign_up = tk.Button(window, text='Sign up',command=usr_sign_up)
btn_sign_up.place(x=200,y=240)
btn_sign_up = tk.Button(window, text='Register Device',command=register_deviceID)
btn_sign_up.place(x=280,y=240)

window.mainloop()


        
        