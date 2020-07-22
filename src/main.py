from send_text_wpp import send_same_textURL as send_wpp
from get_pdf import get_pdf
from download_pdf import download_pdf
from get_url import get_url
import schedule
from time import sleep


def main():
    pdf = get_pdf()
    download_pdf(pdf[0])
    print(get_url(pdf[1]))


# schedule.every().day.at("7:20").do(main)
schedule.every().day.at("23:20").do(main)

while True:
    if schedule.run_pending():
        schedule.run_pending()
        break
    sleep(10)
