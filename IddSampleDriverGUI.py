import customtkinter as ctk
import subprocess as sb
from customtkinter import END
from CTkMessagebox import CTkMessagebox as msgbox
import ctypes
import os

app = ctk.CTk()  
app.geometry("280x620")
app.title('IddSampleDriverGUI')
app.resizable(False, False)

options_file = 'C:\\IddSampleDriver\\option.txt'

if not os.path.exists(options_file):
    with open(options_file, 'w'):
        pass

def invalid_entries(column):
    msgbox(title='Invalid Entry', message=f"The entries in column {column} were invalid, and thus this line was skipped from being saved.")

def devcon_error(e):
    msgbox(title='Devcon Error', message=f"An error has occured when restarting the driver: {e}", icon='cancel')

def devcon_no_devices(deviceid):
    msgbox(title='Invalid Device ID', message=f"Invalid Device ID: {deviceid}", icon='cancel')

def devcon_failure():
    msgbox(title='Devcon Failure', message=f"Driver restart failed", icon='cancel')

def devcon_success():
    msgbox(title='Success', message='Successfully saved the settings and restarted the driver', icon='check')


def restart_driver():
    device_id = dvc_id_entry.get()
    try:
        driver_restart = sb.run(['./devcon', 'restart', device_id], capture_output=True, text=True)
        output = driver_restart.stdout
        error = driver_restart.stderr

        print(output)
        print(error)

        if not output or error == 'No matching devices found.':
            if driver_restart.returncode == 0:
                devcon_success()
            elif driver_restart.returncode == 2:
                devcon_failure()
            else:
                ctypes.windll.user32.MessageBoxW(0, "Invalid syntax or reboot required (or something went very wrong cuz u shouldn't be seeing this)", "Error", 0x10)
        else:
            devcon_no_devices(dvc_id_entry.get())
          
    except Exception as e:
        devcon_error(e)

def save_settings():
    with open(options_file, 'w') as f:
        f.write(num_monitor_entry.get())
        f.write(f"\n#{dvc_id_entry.get()}\n")
        column = 1

        for w, h, hz in widget_list:
            if w.get() and h.get() and hz.get():
                f.write(w.get())
                f.write(f", {h.get()}")
                f.write(f", {hz.get()}\n")
            elif not w.get() and not h.get() and not hz.get():
                pass
            else:
                invalid_entries(column)
            column = column+1


def save_and_reload():
    save_settings()
    restart_driver()

if ctypes.windll.shell32.IsUserAnAdmin() == 0:
    ctypes.windll.user32.MessageBoxW(0, "You must run this as admin!", "Error", 0x10)
    exit()            

save_btn = ctk.CTkButton(app, text='Save & Reload', width=120, command=save_and_reload)
find_btn = ctk.CTkButton(app, text='Find Driver', width=80)
num_monitor_entry = ctk.CTkEntry(app, placeholder_text='No. Monitors', width=80)
dvc_id_entry = ctk.CTkEntry(app, placeholder_text='Device ID', width=200)

w1 = ctk.CTkEntry(app, placeholder_text='Width', width=80)
h1 = ctk.CTkEntry(app, placeholder_text='Height', width=80)
hz1 = ctk.CTkEntry(app, placeholder_text='Hz', width=40)

w2 = ctk.CTkEntry(app, placeholder_text='Width', width=80)
h2 = ctk.CTkEntry(app, placeholder_text='Height', width=80)
hz2 = ctk.CTkEntry(app, placeholder_text='Hz', width=40)

w3 = ctk.CTkEntry(app, placeholder_text='Width', width=80)
h3 = ctk.CTkEntry(app, placeholder_text='Height', width=80)
hz3 = ctk.CTkEntry(app, placeholder_text='Hz', width=40)

w4 = ctk.CTkEntry(app, placeholder_text='Width', width=80)
h4 = ctk.CTkEntry(app, placeholder_text='Height', width=80)
hz4 = ctk.CTkEntry(app, placeholder_text='Hz', width=40)

w5 = ctk.CTkEntry(app, placeholder_text='Width', width=80)
h5 = ctk.CTkEntry(app, placeholder_text='Height', width=80)
hz5 = ctk.CTkEntry(app, placeholder_text='Hz', width=40)

w6 = ctk.CTkEntry(app, placeholder_text='Width', width=80)
h6 = ctk.CTkEntry(app, placeholder_text='Height', width=80)
hz6 = ctk.CTkEntry(app, placeholder_text='Hz', width=40)

w7 = ctk.CTkEntry(app, placeholder_text='Width', width=80)
h7 = ctk.CTkEntry(app, placeholder_text='Height', width=80)
hz7 = ctk.CTkEntry(app, placeholder_text='Hz', width=40)

w8 = ctk.CTkEntry(app, placeholder_text='Width', width=80)
h8 = ctk.CTkEntry(app, placeholder_text='Height', width=80)
hz8 = ctk.CTkEntry(app, placeholder_text='Hz', width=40)

w9 = ctk.CTkEntry(app, placeholder_text='Width', width=80)
h9 = ctk.CTkEntry(app, placeholder_text='Height', width=80)
hz9 = ctk.CTkEntry(app, placeholder_text='Hz', width=40)

w10 = ctk.CTkEntry(app, placeholder_text='Width', width=80)
h10 = ctk.CTkEntry(app, placeholder_text='Height', width=80)
hz10 = ctk.CTkEntry(app, placeholder_text='Hz', width=40)

widget_list = [(w1, h1, hz1), (w2, h2, hz2), (w3, h3, hz3), (w4, h4, hz4),
               (w5, h5, hz5), (w6, h6, hz6), (w7, h7, hz7), (w8, h8, hz8),
               (w9, h9, hz9), (w10, h10, hz10)]

save_btn.place(relx=0.04, rely=0.94)
dvc_id_entry.place(relx=0.04, rely=0.88)
#find_btn.place(relx=0.5, rely=0.94)

num_monitor_entry.grid(row=0, column=0, padx=10, pady=10)

w1.grid(row=1, column=0)
h1.grid(row=1, column=1)
hz1.grid(row=1, column=2, padx=10, pady=10)

w2.grid(row=2, column=0)
h2.grid(row=2, column=1)
hz2.grid(row=2, column=2, padx=10, pady=10)

w3.grid(row=3, column=0)
h3.grid(row=3, column=1)
hz3.grid(row=3, column=2, padx=10, pady=10)

w4.grid(row=4, column=0)
h4.grid(row=4, column=1)
hz4.grid(row=4, column=2, padx=10, pady=10)

w5.grid(row=5, column=0)
h5.grid(row=5, column=1)
hz5.grid(row=5, column=2, padx=10, pady=10)

w6.grid(row=6, column=0)
h6.grid(row=6, column=1)
hz6.grid(row=6, column=2, padx=10, pady=10)

w7.grid(row=7, column=0)
h7.grid(row=7, column=1)
hz7.grid(row=7, column=2, padx=10, pady=10)

w8.grid(row=8, column=0)
h8.grid(row=8, column=1)
hz8.grid(row=8, column=2, padx=10, pady=10)

w9.grid(row=9, column=0)
h9.grid(row=9, column=1)
hz9.grid(row=9, column=2, padx=10, pady=10)

w10.grid(row=10, column=0)
h10.grid(row=10, column=1)
hz10.grid(row=10, column=2, padx=10, pady=10)


with open(options_file, 'r') as f:
    content = f.read()
    line = content.splitlines()
    print(content)

    try:
        num_monitor_entry.insert(ctk.END, line[0])
        dvc_id_entry.insert(ctk.END, line[1].strip('#'))
    except:
        pass

    for i in range(2, 12):
        try:
            vars = line[i].split(', ')
            w = globals()[f'w{i-1}']
            h = globals()[f'h{i-1}']
            hz = globals()[f'hz{i-1}']
            w.insert(END, vars[0])
            h.insert(END, vars[1])
            hz.insert(END, vars[2])
        except IndexError:
            pass

app.mainloop()