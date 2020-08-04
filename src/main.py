import os
from get_pdf import get_pdf
from download_pdf import download_pdf
from get_url import get_url
from time import sleep


def main():
    from selenium import webdriver
    pdf = get_pdf()
    print(pdf['URL'])
    download_pdf(pdf['URL'])
    url = get_url(pdf['file_name'])
    # url = get_url('AGEN_23_SAS_31-07_2serie.pdf')
    zoom = url['zoom']
    id = url['id']
    password = url['password']
    # open zoom for mi self
    driver = webdriver.Chrome(executable_path=r'E:\coding\python\chromedriver.exe')
    driver.get(zoom)
    # * Run JavaScript code to send msg
    os.system(
        f"node E:\coding\other\class-url-automation\src\send_text_wpp\index.js {zoom} {pdf['URL']} {id} {password}"
    )


main()
sleep(15)
