from weather import main_func
from send_message import send_message
import datetime

if __name__ == "__main__":

    weekno = datetime.datetime.today().weekday()

    TODAY_CHECK = datetime.date.today()

    start = datetime.datetime.strptime('16 Sep, 2021', "%d %b, %Y").date()
    end = datetime.datetime.strptime('23 Oct, 2021', "%d %b, %Y").date()

    if weekno < 5 and start <= TODAY_CHECK <= end:
        string = main_func()

        if string != '':
            send_message(string)





