import os
from get_pdf import get_pdf
from get_url import get_url, spanish
from time import sleep


def main():
    from selenium import webdriver
    pdf = get_pdf()
    url = spanish(pdf['file_name'])
    # url = get_url('AGEN_23_SAS_31-07_2serie.pdf')
    pdf = pdf['URL']
    zoom = url['zoom']
    id = url['id']
    password = url['password']
    # open zoom for mi self
    driver = webdriver.Chrome(executable_path=r'E:\coding\python\chromedriver.exe')
    driver.get(zoom)
    # * Run JavaScript code to send msg
    os.system(
        f"node E:\coding\other\class-url-automation\src\send_text_wpp\spanish.js {zoom} {pdf} {id} {password}"
    )


main()
sleep(15)
