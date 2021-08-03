import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title="DRINK A GLASS OF WATER",
            message="Regular drinking of water is good for health and keeps body hydrated.",
            # downloaded from https://icon-icons.com/
            app_icon="E:\projects\water-notification-proj\water glass.ico",
            timeout=5
        )
        time.sleep(3600)
# Run using command - pythonw .\main.py
# Runs in background
