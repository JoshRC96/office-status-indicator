import serial # importing the serial module from the pyserial library to enable communication with the Arduino board.
import tkinter as tk

ser = serial.Serial('COM3', 9600) # setting the serial communication

def set_status(status):
    if status in ('B','N','O'):
        ser.write(status.encode()) # sending the status to the Arduino sketch
        if status == 'B':
            current_status_label.config(text='Current status: Busy')
            color_square.config(bg='red')
        elif status == 'N':
            current_status_label.config(text='Current status: Not Busy')
            color_square.config(bg='white')
        else:
            current_status_label.config(text='Current status: Off')
            color_square.config(bg='black')

def on_closing():
    '''This function ensure the LED turns off before closing the Python program'''
    set_status('O')
    app.destroy()

# Creating the main app window
app = tk.Tk()
app.title('Office Status Control')

# Bind the window closing event to the on_closing function
app.protocol("WM_DELETE_WINDOW", on_closing)

# Main banner
main_banner = tk.Label(app,text='Office Status Control', font=('Arial',16))
main_banner.grid(row=0, column=0, columnspan=3, sticky='nsew')

# Status idicator
current_status_label = tk.Label(app, text='Current Status:', font=('Arial', 12))
current_status_label.grid(row=1, column=0, columnspan=3, pady=10)

# Color square (to visually indicate current status)
color_square = tk.Label(app, width=4, height=2)
color_square.grid(row=2, column=1, pady=10)

# Buttons
busy_button = tk.Button(app, text='Busy', command=lambda: set_status('B'))
not_busy_button = tk.Button(app, text='Not busy', command=lambda: set_status('N'))
off_button = tk.Button(app, text='Off', command=lambda: set_status('O'))

# Position the buttons
busy_button.grid(row=3, column=0, padx=10, sticky='nsew')
not_busy_button.grid(row=3, column=1, padx=10, sticky='nsew')
off_button.grid(row=3, column=2, padx=10, sticky='nsew')

# Use column weights to keep buttons centered
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)

# Use row weight to expand the banner and status indicator
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)

# Run the Tkinter main loop
app.mainloop()