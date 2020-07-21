from get_pdf import get_pdf
from send_text_wpp import send_same_textURL as send_wpp

PDF = get_pdf()

send_wpp(['5571999930704'], PDF)
