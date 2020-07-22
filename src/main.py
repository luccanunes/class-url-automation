from send_text_wpp import send_same_textURL as send_wpp
from get_pdf import get_pdf
from download_pdf import download_pdf
from get_url import get_url
import schedule
from time import sleep


def main():
    pdf = get_pdf()
    download_pdf(pdf[0])
    link = get_url(pdf[1])
    send_wpp(
        ['5571999930704', '5571999124404', '5571986991043',
         '5571997377176', '5571999440042'], link
    )


# schedule.every().day.at("7:20").do(main)
schedule.every().day.at("08:24").do(main)

while True:
    if schedule.run_pending():
        break
    sleep(30)
print('cabou')
