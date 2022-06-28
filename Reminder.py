
from email import message
from socket import timeout
import time
from plyer import notification


if __name__=="__main__":
    while True:
        a=input("Enter a task--->")
        b=input("Enter Task description--->")
        ti=int(input("Enter the duration of the task in in minutes--->"))
        notification.notify(
            title="Reminder to do-{}".format(a),
            message="{}".format(b),
            timeout=20)
        time.sleep(ti*60)

