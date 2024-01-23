import time
from plyer import notification  # You may need to install the plyer library using: pip install plyer

def remind_to_get_up():
    notification.notify(
        title='Time to Take a Break!',
        message='It\'s been an hour. Take a break, stretch, and relax for a while.',
        app_icon=None,  # You can provide an icon path if you have one
        timeout=20  # The notification will disappear after 10 seconds
    )

if __name__ == "__main__":
    # Set the interval to 1 hour (3600 seconds)
    interval_seconds = 3600

    while True:
        time.sleep(interval_seconds)  # Sleep for the specified interval
        remind_to_get_up()
