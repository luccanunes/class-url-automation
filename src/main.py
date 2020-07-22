import os
from get_pdf import get_pdf
from download_pdf import download_pdf
from get_url import get_url
from time import sleep


def main():
    pdf = get_pdf()
    download_pdf(pdf['URL'])
    url = get_url(pdf['file_name'])
    zoom = url['zoom']
    id = url['id']
    password = url['password']
    pdf = pdf['URL']
    # Run JavaScript code to send msg
    os.system(
        f"node E:\coding\other\class-url-automation\src\send_text_wpp {zoom} {pdf} {id} {password}"
    )


main()
sleep(15)
