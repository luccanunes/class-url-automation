import os


def log(c, t, decoration=False, ending='\n'):
    os.system("")
    if decoration:
        print(f'[{str(c)}m' + '-'*len(t)*2 + '[0m', end=ending)
        print(f'[{str(c)}m{t:^{len(t)*2}}[0m', end=ending)
        print(f'[{str(c)}m' + '-'*len(t)*2 + '[0m', end=ending)
    else:
        print(f'[{str(c)}m{t}[0m', end=ending)


def warning(t, decoration=False, ending='\n'):
    os.system("")
    if decoration:
        print('[33m' + '-'*len(t)*2 + '[0m', end=ending)
        print(f'[33m{t:^{len(t)*2}}[0m', end=ending)
        print('[33m' + '-'*len(t)*2 + '[0m', end=ending)
    else:
        print(f'[33m{t}[0m', end=ending)


def error(t, decoration=False, ending='\n'):
    os.system("")
    if decoration:
        print('[91m' + '-'*len(t)*2 + '[0m', end=ending)
        print(f'[91m{t:^{len(t)*2}}[0m', end=ending)
        print('[91m' + '-'*len(t)*2 + '[0m', end=ending)
    else:
        print(f'[91m{t}[0m', end=ending)


#log(32, 'sucessfully joined niver da chavosidade server', True)
# log(32, 'Sucessfuly joined "W2S" server', True)
# error('EXITING PROGRAM', True)
