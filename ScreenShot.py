from tkinter import *
import pyautogui
from tkinter.messagebox import showinfo
import win32gui , win32con
import time
from tkinter.filedialog import askdirectory
import datetime
import pytz

root = Tk()
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide,win32con.SW_HIDE)
root.geometry("600x500")
root.maxsize(600,500)
root.minsize(600,500)
root.iconbitmap("C:\\Users\\prince\\Desktop\\GUI\\Required files\\screen.ico") 
root.title("SnapClick")  

def help_func():
    showinfo("Help",f"SnapClick we capture a screecshot\nof the screen")

Label(root,text="SnapClick",font="Magneto 40 underline",fg="red").pack()
help = Menu(root)
help.add_command(label="Help",command=help_func)
root.config(menu=help)

name = Entry(root,width=15)
name.place(x=400,y=255)

directory = 0

def select():
    global directory
    directory = askdirectory()

def capture():
    global directory
    if directory==0:
        if name.get()=="":
            root.wm_state("iconic")
            time.sleep(2)
            screen = pyautogui.screenshot()
            year = time.strftime("%Y")
            month = time.strftime("%m")
            datee = time.strftime("%d")
            hour = time.strftime("%H")
            min =time.strftime("%M")
            sec = time.strftime("%S")
            to_save = f"SNAP_{year}{month}{datee}-{hour}-{min}-{sec}_Pro"
        
            screen.save(f"C:\\Users\\prince\\Desktop\\GUI\\{str(to_save)}.png")
            root.state('zoomed')
            showinfo("Svaed",f"Screen shot have been saved\nwith name {to_save}.png\nat current location.")
        
        else:
            root.wm_state("iconic")
            time.sleep(2)
            screen = pyautogui.screenshot()
        
            screen.save(f"C:\\Users\\prince\\Desktop\\GUI\\{name.get()}.png")
            root.state('zoomed')
            showinfo("Svaed",f"Screen shot have been saved\nwith name {name.get()}.png\nat current location.")

    elif directory!=0:
        if name.get()=="":
            root.wm_state("iconic")
            time.sleep(2)
            screen = pyautogui.screenshot()
            year = time.strftime("%Y")
            month = time.strftime("%m")
            datee = time.strftime("%d")
            hour = time.strftime("%H")
            min =time.strftime("%M")
            sec = time.strftime("%S")
            to_save = f"SNAP_{year}{month}{datee}-{hour}-{min}-{sec}_Pro"
        
            screen.save(f"{directory}\{to_save}.png")
            root.state('zoomed')
            showinfo("Saved",f"Screen shot have been saved\nwith name {to_save}.png\nat specified location.")
        else:
            root.wm_state("iconic")
            time.sleep(2)
            screen = pyautogui.screenshot()
        
            screen.save(f"{directory}\{name.get()}.png")
            root.state('zoomed')
            showinfo("Saved",f"Screen shot have been saved\nwith name {name.get()}.png\nat specified location.")

select_loc = Button(root,text="Location",font="Magneto 15",fg="blue",command=select)
select_loc.place(x=20,y=150)

name_lbl = Label(root,text="Enter the file name : ",font="Magneto 15")
name_lbl.place(x=20,y=250)

btn = Button(root,text="Capture",font="Magneto 15",fg="blue",command=capture)
btn.place(x=20,y=350)

root.mainloop()
