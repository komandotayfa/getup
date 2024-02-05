import time
import tkinter as tk
from plyer import notification

def gui():
    root = tk.Tk()
    root.title("KAPAT")
    label = tk.Label(root, text="KAPAT ŞUNU!")
    label.pack(pady=10)
    root.mainloop()

def getup():
    notification.notify(
        title='KALK!',
        message='KALK LAN!',
        timeout=20  # Saniye/Seconds
    )

if __name__ == "__main__":
    waitsec = 3600  # Saniye/Seconds
    while True:
            time.sleep(waitsec)
            getup()
            gui()