def get_pdf():
    from console_log import clog, log_sleep
    from datetime import datetime

    date = str(datetime.now().date())

    log = open(f"log.txt", "a")
    log.write('Program launch {\n')
    log.write(f'\tTimestamp: {datetime.now().today()}\n')
    log.write(f'\tDate: {date}\n')
    log.write('\tSucessfully generated URL {\n')

    # URL pattern: 'https://colegiooficina.com.br/arquivos/restrito/2serie/agenda_sas/{mnum}_{mn}/AGEN_{ag}_SAS_{date}_2serie.pdf'
    # eg: https://colegiooficina.com.br/arquivos/restrito/2serie/agenda_sas/07_julho/AGEN_14_SAS_20-07_2serie.pdf
    # mnum == month number (eg: 07)
    # dnum = day number (eg: 20)
    # mn == month name (all lower)
    # ag == agenda number

    mnum = date[5:7]
    dnum = date[8:]
    ag = int(dnum) - (int(dnum)//7) * 2
    mon_names = (
        'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
        'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
    )
    file_name = f'AGEN_{ag}_SAS_{dnum}-{mnum}_2serie.pdf'

    URL = f'https://colegiooficina.com.br/arquivos/restrito/2serie/agenda_sas/{mnum}_{mon_names[int(mnum) -1]}/{file_name}'

    clog.log('7;95', f'PDF URL: {URL}', True)

    log.write(f'\t\tDate: {date}\n')
    log.write(f'\t\tURL: {URL}\n')
    log.write('\t}\n')
    log.write('};\n\n')
    log.close()

    return (URL, file_name)