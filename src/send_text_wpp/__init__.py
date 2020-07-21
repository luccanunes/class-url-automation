def send_same_textURL(phone_numbers, text, mlog='default_message_log'):
    from selenium import webdriver
    from console_log.clog import log, error, warning
    from console_log.log_sleep import log_sleep, partial_log_sleep
    from datetime import datetime

    log('7;97', 'LAUNCHING PROGRAM', True)
    log(36, f'Target chats: {phone_numbers}')
    log(36, f'Message type: single text')
    log(36, f'Message content: "{text}"')
    log(36, f'Method: URL')
    log(36, f'Logging process in: {mlog}.txt')
    msg_log = open(f"{mlog}.txt", "a")
    msg_log.write('\nProgram launch {\n')
    msg_log.write(f'\tTimestamp: {datetime.now().today()}\n')
    msg_log.write(f'\tTarget chats: {phone_numbers}\n')
    msg_log.write(f'\tMethod: URL\n')
    msg_log.write(f'\tMessage type: single text\n')
    msg_log.write(f'\tMessage content: "{text}"\n')
    options = webdriver.ChromeOptions()
    options.add_argument('lang=pt-br')
    driver = webdriver.Chrome(
        executable_path=r'E:\coding\python\chromedriver.exe', chrome_options=options)
    for number in phone_numbers:
        try:
            driver.get(
                f'https://web.whatsapp.com/send?phone={number}&text={text}')
        except:
            error('ERROR: url not valid or not found. Perhaps the URL is invalid', True)
            msg_log.write(
                f'\t\tERROR: url not valid or not found. Timestamp: {datetime.now().today()}\n')
            if number != phone_numbers[-1]:
                log(31, 'skipping to next phone number')
        else:
            log(92, f"Sucessfully opened {number}'s conversation chat!", True)
            msg_log.write('\tSucessfull connection to website {\n')
            msg_log.write(f'\t\tTimestamp: {datetime.now().today()}\n')
            if number == phone_numbers[0]:
                partial_log_sleep(15, True, 'so the page can load')
            else:
                log_sleep(8, True, 'to send the message')
            try:
                send_button = driver.find_element_by_xpath(
                    '//*[@id="main"]/footer/div[1]/div[3]')
            except:
                error('ERROR: send button somehow not found', True)
                msg_log.write(
                    f'\t\tERROR: send button somehow not found. Timestamp: {datetime.now().today()}\n')
                if number != phone_numbers[-1]:
                    log(31, 'skipping to next phone number')
            else:
                send_button.click()
                log(92, f'Sucessfuly sent message to {number}!')
                log_sleep(3, True)
    msg_log.write('\t}\n')
    msg_log.write('};\n')
    msg_log.close()
    log('7;91', 'EXITING PROGRAM', True)
