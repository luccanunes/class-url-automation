import os
import schedule
from get_pdf import get_pdf
from download_pdf import download_pdf
from get_url import get_url
from time import sleep


def main():
    pdf = get_pdf()
    download_pdf(pdf[0])
    zoom = get_url(pdf[1])
    pdf = pdf[0]
    os.system(
        f"node E:\coding\other\class-url-automation\src\send_text_wpp {zoom} {pdf}"
    )


# schedule.every().day.at("7:20").do(main)
schedule.every().day.at("12:30").do(main)

while True:
    if schedule.run_pending():
        break
    sleep(30)
print('cabou')
