def get_url():
    from selenium import webdriver
    from consoleLog import clog, log_sleep
    from datetime import datetime

    options = webdriver.ChromeOptions()
    options.add_argument('lang=pt-br')
    driver = webdriver.Chrome(
        executable_path=r'E:\coding\python\chromedriver.exe', chrome_options=options
    )

    # URL pattern: 'https://colegiooficina.com.br/arquivos/restrito/2serie/agenda_sas/{mnum}_{mn}/AGEN_{ag}_SAS_{date}_2serie.pdf'
    # eg: https://colegiooficina.com.br/arquivos/restrito/2serie/agenda_sas/07_julho/AGEN_14_SAS_20-07_2serie.pdf
    # mnum == month number (eg: 07)
    # dnum = day number (eg: 20)
    # mn == month name (all lower)
    # ag == agenda number

    date = str(datetime.now().date())
    mnum = date[5:7]
    dnum = date[8:]
    ag = 15
    mon_names = (
        'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
        'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
    )

    driver.get(
        f'https://colegiooficina.com.br/arquivos/restrito/2serie/agenda_sas/{mnum}_{mon_names[int(mnum) -1]}/AGEN_{ag}_SAS_{dnum}-{mnum}_2serie.pdf'
    )
    log_sleep.log_sleep(15)


get_url()
