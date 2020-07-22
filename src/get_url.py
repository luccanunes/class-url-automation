def get_url(file_name):
    import PyPDF2
    from get_pdf import get_pdf
    from console_log import clog

    file = f'E:\coding\python\class-url-automation\src\pdfs\{file_name}'
    read = PyPDF2.PdfFileReader(file)
    page = read.getPage(1)
    content = page.extractText()
    for link in content.strip().split(' '):
        if 'https' in link:
            link = link.replace('\n', '')
            clog.log('7;93', f'ZOOM URL: {link}', True)
            return link
