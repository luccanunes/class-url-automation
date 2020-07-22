def download_pdf():
    from get_pdf import get_pdf
    from selenium import webdriver
    from time import sleep

    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {
        # Change default directory for downloads
        "download.default_directory": r"E:\coding\python\class-url-automation\src\pdfs",
        "download.prompt_for_download": False,  # To auto download the file
        "download.directory_upgrade": True,
        # It will not show PDF directly in chrome
        "plugins.always_open_pdf_externally": True
    })
    driver = webdriver.Chrome(
        executable_path=r'E:\coding\python\chromedriver.exe', chrome_options=options
    )

    driver.get(
        'https://colegiooficina.com.br/arquivos/restrito/2serie/agenda_sas/07_julho/AGEN_15_SAS_21-07_2serie.pdf')
    sleep(3)


download_pdf()
