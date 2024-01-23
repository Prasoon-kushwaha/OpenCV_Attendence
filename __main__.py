import threading
import tkinter as tk
import subprocess
from tkinter import font
from datetime import date
import tkinter.font as tkFont
import MySql
from Shared_credentials import rw, initialize_window
import Shared_credentials
from tkinter import messagebox
from PIL import Image, ImageTk

if rw == None:
    initialize_window()


def update_connection():
    connection()
    rw.after(2500, update_connection)


# Loading database
def Load():
    global password
    global pwindow
    global User
    global connected

    # Create the main window
    r = tk.Tk()
    r.title("Connection Window")
    r.configure(bg="#fbffd7", height=300, width=600)  # Increased width

    # Set fonts
    title_font = font.Font(family="Helvetica", size=18, weight="bold")
    label_font = font.Font(family="Helvetica", size=12)
    entry_font = font.Font(family="Helvetica", size=12)

    # Title
    title_label = tk.Label(r, text="Connect to Database", background="#fbffd7", font=title_font)
    title_label.pack(pady=10)

    # User Name
    label_user = tk.Label(r, text="User Name:", background="#fbffd7", font=label_font)
    label_user.pack(pady=5)
    entry_user = tk.Entry(r, font=entry_font, textvariable=User)
    entry_user.pack(pady=5)

    # Password
    label_password = tk.Label(r, text="Password:", background="#fbffd7", font=label_font)
    label_password.pack(pady=5)
    entry_password = tk.Entry(r, font=entry_font, show="*")
    entry_password.pack(pady=5)

    # Connect Button
    connect_button = tk.Button(r, text="Connect", height=1, font=entry_font, command=lambda: connection())
    connect_button.pack(pady=20)

    # Initialize variables
    password = entry_password
    User = entry_user
    pwindow = r
    connected = False


def connection():
    global data
    global pwindow
    global password
    global User
    global studentrcd
    global connected
    global rw
    M = 0
    if not connected:
        print(password.get(), User.get())
        password_val = password.get()
        User_val = User.get()
        password = password_val
        User = User_val
        Shared_credentials.username = User_val
        Shared_credentials.password = password_val
        try:
            MySql.addnewdate(password=password_val, user=User_val)
            pwindow.destroy()
        except:
            print("Wrong Password or Username")  # ERROR
            connected = False
            password.delete(0, tk.END)  # Clear the Entry widget
            User.delete(0, tk.END)  # Clear the Entry widget
            pwindow.destroy()  # DESTROYNG CURRENT WINDOW AS WRONG CREDENTIALS
            messagebox.showerror("ERROR OCCURRED", "Wrong username or password")
            Load()
        M = 1  # preventing Data to be called stopping auto refresh on pressing button
    data = MySql.exc("select roll,Name," + MySql.today + " from attendence ", password=password, user=User,
                     get=None)
    tbl = ""
    print(data)
    roll = ""
    name = ""
    status = ""
    for a in range(len(data)):
        roll += str(data[a][0]) + "\n"
        name += str(data[a][1]) + "\n"
        status += str(data[a][2]) + "\n"
    studentrcd = [roll, name, status]
    connected = True
    Shared_credentials.Connected = connected
    if M == 1:
        pass
        # DATA()
    view()
    print(studentrcd)


def DNA():  # don't know anything--DNA
    r = tk.Tk()

    # Configure window
    r.title("How to use ?")
    r.configure(bg="#fbffd7", height=500, width=900)

    # Set a custom font
    fontStyle = font.Font(family="Helvetica", size=14)

    s = "This is a general message for the use case of this project.\n\n" \
        "1. Connect to the Database.\n" \
        "2. Enter the credentials.\n" \
        "3. Launch the webcam. \n  \n" \
        "You can also access data from MySQL command Line as well as \n " \
        "in csv file containing Name, Roll and Time of entries \n\n" \
        "Once the attendance is marks a e-mail will be send to your institute mail address"

    # Create a label with formatted text
    label = tk.Label(r, text=s, background="#fbffd7", font=fontStyle, justify="left", padx=20, pady=20)
    label.pack()


def Launch():
    def run_subprocess():
        global connected #add name here
        other_file_path = r'C:\Users\praso\PycharmProjects\Open-CV-Attendence-Project\Attendance_System.py'
        python_executable_path = r'C:\Users\praso\PycharmProjects\Open-CV-Attendence-Project\venv\Scripts\python.exe'
        if connected == True:
            subprocess.run([python_executable_path, other_file_path])
        else:
            messagebox.showerror("ERROR OCCURRED", "Database Not Connected")

    # Create a new thread and run the subprocess call in that thread
    thread = threading.Thread(target=run_subprocess)
    thread2 = threading.Thread(target=update_connection)
    thread.start()
    thread2.start()


# def tables():

def view():
    Roll = tk.Label(rw, text=studentrcd[0], background="#8B8C6D", font=fontStyle, fg="#fbffd7")
    Roll.place(relx=0.54, rely=0.2, anchor='ne')
    name = tk.Label(rw, text=studentrcd[1], background="#8B8C6D", font=fontStyle, justify="left", fg="#fbffd7")
    name.place(relx=0.72, rely=0.2, anchor='ne')
    P_ab = tk.Label(rw, text="" + studentrcd[2] + " ", background="#8B8C6D", font=fontStyle, fg="#fbffd7")
    P_ab.place(relx=0.9, rely=0.2, anchor='ne')


def add_refresh(Name, data, user, pswd):
    global awindow
    MySql.exc(
        "INSERT INTO attendence (roll,Name) VALUES(" + str(len(data) + 1) + ',' + '"' + Name + '"' + ");",
        user=user, password=pswd, get="update")
    # MySQL command
    awindow.destroy()


def newdata(data, user, pswd):
    global awindow
    global connected
    if connected == True:
        r = tk.Tk()
        r.geometry()
        label = tk.Label(r, text="ENTER NAME", background="#fbffd7", font=fontStyle)
        label.pack()
        name = tk.Entry(r, font=fontStyle1, textvariable=User)
        name.pack()
        Enter = tk.Button(r, text="Add Name", height=1, font=fontStyle1,
                          command=lambda: add_refresh(Name=str(name.get()), data=data, user=user, pswd=pswd))
        Enter.pack()
        awindow = r


    else:
        messagebox.showerror(title="ERROR", message="AUTHORISATION REQUIRED")
        Load()


# ================DEFAULT===============
password = None
User = None
studentrcd = " NONE "
connected = False
data = None
pwindow = None
awindow = None
cur = 1  # current roll no of student
# =======================================================================================
today = date.today()

fontStyle = tkFont.Font(family="Lucida Grande", size=26, weight="bold")
fontStyle1 = tkFont.Font(family="Lucida Grande", size=15)
fontStyle2 = tkFont.Font(family="Lucida Grande", size=25)
fontStyle3 = tkFont.Font(family="Lucida Grande", size=30)

# ===============IMAGES==================
iFAQ = ImageTk.PhotoImage(file="question.png")
iviewport = ImageTk.PhotoImage(file="ViewPort.png")
iiiitu = ImageTk.PhotoImage(file="IIITU.png")
iconn = ImageTk.PhotoImage(file="connect.png")
iconnected = ImageTk.PhotoImage(file="connect.png")
irefresh = ImageTk.PhotoImage(file="start.png")

view()

IIITUlog = tk.Button(image=iiiitu, border=0, bg='#fbffd7', activebackground='#fbffd7')
IIITUlog.place(relx=0.44, rely=0.03, anchor='ne')
FAQ = tk.Button(image=iFAQ, border=0, bg='#fbffd7', activebackground='#fbffd7', command=lambda: DNA())
FAQ.place(relx=0.09, rely=0.85, anchor='ne')

Date = tk.Label(rw, text=str(today), background="#fbffd7",
                font=tkFont.Font(family="Lucida Grande", size=40, weight='bold'), fg='#8B8C6D')
Date.place(relx=0.15, rely=0.115, anchor='nw')

refresh = tk.Button(image=irefresh, border=0, bg='#fbffd7', activebackground='#fbffd7', command=lambda: Launch())
refresh.place(relx=0.33, rely=0.4, anchor='ne')

LOAD = tk.Button(image=iconn, border=0, bg='#fbffd7', activebackground='#fbffd7', command=lambda: Load())
LOAD.place(relx=0.35, rely=0.6, anchor='ne')
#

View_Port = tk.Button(image=iviewport, border=0, bg='#fbffd7', activebackground='#fbffd7', command=lambda: connection())
View_Port.place(relx=0.95, rely=0.1, anchor='ne')
if rw != None:
    rw.mainloop()
