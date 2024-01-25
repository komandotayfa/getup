import time
import tkinter as tk
from plyer import notification

def create_gui():
    # Create the Tkinter window
    root = tk.Tk()
    root.title("KAPAT")

    # Create a label
    label = tk.Label(root, text="KAPAT ŞUNU!")

    # Pack the label and button into the window
    label.pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()

def remind_to_get_up():
    notification.notify(
        title='KALK!',
        message='KALK LAN!',
        timeout=20  # The notification will disappear after 10 seconds
    )

if __name__ == "__main__":
    # Set the interval to 1 hour (3600 seconds)
    interval_seconds = 3600
    while True:
            time.sleep(interval_seconds)  # Sleep for the specified interval
            remind_to_get_up()
            create_gui()