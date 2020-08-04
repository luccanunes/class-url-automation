def get_url(file_name):
    import PyPDF2
    from get_pdf import get_pdf
    from console_log import clog

    file = f'E:\coding\other\class-url-automation\src\pdfs\{file_name}'
    read = PyPDF2.PdfFileReader(file)
    page = read.getPage(1)
    content = page.extractText()
    zoom = id = password = ''
    found_zoom = found_id = found_password = False

    array = content.strip().split(' ')
    for i in range(len(array)):
        if 'https' in array[i] and not found_zoom:
            zoom = array[i].replace('\n', '')
            found_zoom = True
            clog.log('7;93', f'ZOOM URL: {zoom}', True)
        elif 'reunião:' in array[i] and not found_id:
            id = array[i+1].replace('\n', '') + array[i + 2].replace('\n', '') + array[i+3].replace('\n', '')
            found_id = True
            clog.log('7;93', f'ID: {id}', True)
        elif 'acesso:' in array[i] and not found_password:
            password = array[i+1].replace('\n', '')
            found_password = True
            clog.log('7;93', f'PSSWRD: {password}', True)

    return {'zoom': zoom, 'id': id, 'password': password}

def spanish(file_name):
    import PyPDF2
    from get_pdf import get_pdf
    from console_log import clog

    file = f'E:\coding\other\class-url-automation\src\pdfs\{file_name}'
    read = PyPDF2.PdfFileReader(file)
    page = read.getPage(1)
    content = page.extractText()
    found_zoom = found_id = found_password = False
    azoom = aid = apassword = '' # * afternoon stuff
    afound_zoom = afound_id = afound_password = False # * afternoon stuff

    array = content.strip().split(' ')
    for i in range(len(array)):
        if 'https' in array[i]:
            if not found_zoom:
                found_zoom = True
            else:
                azoom = array[i].replace('\n', '')
                afound_zoom = True
                clog.log('7;93', f'AFTERNOON ZOOM URL: {azoom}', True)
        elif 'reunião:' in array[i]:
            if not found_id:
                found_id = True
            else:
                aid = array[i+1].replace('\n', '') + array[i + 2].replace('\n', '') + array[i+3].replace('\n', '')
                afound_id = True
                clog.log('7;93', f'AFTERNOON ID: {aid}', True)
        elif 'acesso:' in array[i]:
            if not found_password:
                found_password = True
            else:
                apassword = array[i+1].replace('\n', '')
                afound_password = True
                clog.log('7;93', f'AFTERNOON PSSWRD: {apassword}', True)   
                   
    afternoon = {'zoom': azoom, 'id': aid, 'password': apassword}

    return {'zoom': azoom, 'id': aid, 'password': apassword, 'afternoon': afternoon}

