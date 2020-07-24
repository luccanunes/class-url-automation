import os
from get_pdf import get_pdf
from download_pdf import download_pdf
from get_url import get_url
from time import sleep


def main():
    from selenium import webdriver
    pdf = get_pdf()
    download_pdf(pdf['URL'])
    url = get_url(pdf['file_name'])
    zoom = url['zoom']
    id = url['id']
    password = url['password']
    pdf = pdf['URL']
    # open zoom for mi self
    driver = webdriver.Chrome(executable_path=r'E:\coding\python\chromedriver.exe')
    driver.get(zoom)
    # Run JavaScript code to send msg
    os.system(
        f"node E:\coding\other\class-url-automation\src\send_text_wpp {zoom} {pdf} {id} {password}"
    )


main()
sleep(15)
