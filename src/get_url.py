def get_url(file_name):
    import PyPDF2
    from get_pdf import get_pdf
    from console_log import clog

    file = f'E:\coding\other\class-url-automation\src\pdfs\{file_name}'
    read = PyPDF2.PdfFileReader(file)
    page = read.getPage(1)
    content = page.extractText()
    zoom = ''
    id = ''
    password = ''
    found_zoom = False
    found_id = False
    found_password = False
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
        elif 'Senha:' in array[i] and not found_password:
            password = array[i+1].replace('\n', '')
            found_password = True
            clog.log('7;93', f'PSSWRD: {password}', True)
        if found_zoom and found_id and found_password:
            break
    return {'zoom': zoom, 'id': id, 'password': password}