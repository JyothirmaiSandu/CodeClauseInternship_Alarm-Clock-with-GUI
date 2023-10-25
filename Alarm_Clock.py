import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def set_alarm():
    try:
        hour = int(entry_hour.get())
        minute = int(entry_minute.get())
        am_pm = am_pm_var.get()
        day = int(day_var.get())
        month = int(month_var.get())
        year = int(year_var.get())

        if am_pm == 'PM':
            hour += 12

        alarm_time = datetime(year, month, day, hour, minute)

        now = datetime.now()
        if alarm_time < now:
            messagebox.showerror("Error", "Please enter a future time.")
            return

        time_difference = alarm_time - now
        seconds_difference = time_difference.total_seconds()

        root.after(int(seconds_difference * 1000), trigger_alarm)

        messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time.strftime('%Y-%m-%d %I:%M %p')}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for hour and minute.")

def trigger_alarm():
    messagebox.showinfo("Alarm", "Time to wake up!")

def update_clock():
    current_time = datetime.now().strftime('%d - %m - %y') + '\n' + datetime.now().strftime('%I:%M:%S %p')
    clock_label.config(text=current_time)
    root.after(1000, update_clock)

root = tk.Tk()
root.geometry("225x325")
root.title("Alarm Clock")
root.configure(bg="#F0E68C") 

clock_label = tk.Label(root, font=('Arial', 12), bg="#F0E68C") 
clock_label.grid(row=0, columnspan=2, pady=(10, 20))

label_hour = tk.Label(root, text="Hour (0-12):", bg="#F0E68C") 
label_hour.grid(row=1, column=0, pady=(0, 5))
entry_hour = tk.Entry(root, bg="#FFDAB9") 
entry_hour.grid(row=1, column=1, pady=(0, 5))

label_minute = tk.Label(root, text="Minute (0-59):", bg="#F0E68C")
label_minute.grid(row=2, column=0, pady=(0, 5))
entry_minute = tk.Entry(root, bg="#FFDAB9") 
entry_minute.grid(row=2, column=1, pady=(0, 5))

label_am_pm = tk.Label(root, text="AM/PM:", bg="#F0E68C") 
label_am_pm.grid(row=3, column=0, pady=(0, 5))
am_pm_options = ['AM', 'PM']
am_pm_var = tk.StringVar(root)
am_pm_var.set(am_pm_options[0]) 
am_pm_menu = tk.OptionMenu(root, am_pm_var, *am_pm_options)
am_pm_menu.configure(bg="#FFDAB9") 
am_pm_menu.grid(row=3, column=1, pady=(0, 5))

label_day = tk.Label(root, text="Day (1-31):", bg="#F0E68C") 
label_day.grid(row=4, column=0, pady=(0, 5))
day_var = tk.StringVar(root)
day_var.set('1') 
day_menu = tk.OptionMenu(root, day_var, *[str(i) for i in range(1, 32)])
day_menu.configure(bg="#FFDAB9") 
day_menu.grid(row=4, column=1, pady=(0, 5))

label_month = tk.Label(root, text="Month (1-12):", bg="#F0E68C") 
label_month.grid(row=5, column=0, pady=(0, 5))
month_var = tk.StringVar(root)
month_var.set('1') 
month_menu = tk.OptionMenu(root, month_var, *[str(i) for i in range(1, 13)])
month_menu.configure(bg="#FFDAB9") 
month_menu.grid(row=5, column=1, pady=(0, 5))

label_year = tk.Label(root, text="Year:", bg="#F0E68C")
label_year.grid(row=6, column=0, pady=(0, 5))
year_var = tk.StringVar(root)
year_var.set(str(datetime.now().year)) 
year_menu = tk.OptionMenu(root, year_var, *[str(i) for i in range(datetime.now().year, datetime.now().year + 10)])
year_menu.configure(bg="#FFDAB9") 
year_menu.grid(row=6, column=1, pady=(0, 5))

set_button = tk.Button(root, text="Set Alarm", command=set_alarm, bg="#87CEFA") 
set_button.grid(row=7, columnspan=2, pady=(10, 20))

update_clock()

root.mainloop()
