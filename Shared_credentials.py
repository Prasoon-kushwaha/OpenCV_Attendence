from queue import Queue
import tkinter as tk

username = "root"
password = 'root'
global first
first = True
Connected = True
MessageQueue = Queue()
update = False
global rw
rw = None


# Initialize Tkinter window later in the code
def initialize_window():
    global rw
    rw = tk.Tk()
    rw.title("IIIT Una Attendance System")
    rw.configure(bg="#fbffd7", height="1080", width="1920")


# Call initialize_window() only if the module is run directly
if __name__ == "__main__":
    initialize_window()

# Rest of the code...
initialize_window()