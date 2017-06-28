# coding: utf-8

import re
import os
import sys
import smtplib

import taf_config as config

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import COMMASPACE, formatdate


def send_mail(send_to, subject, body, attachments=[]):
    """
    Send email
    """
    print "Executing send_mail with send_to=%s, subject=%s, body=%s, attachments=%s" % (send_to, subject, body, attachments)

    _text_type = 'plain'
    if re.search(pattern=r"<[^<]+?>", string=body) is not None:
        _text_type = 'html'

    _msg = MIMEMultipart()
    _msg['Subject'] = subject
    _msg['From'] = config.MAIL_SENDER_ADDR
    _msg['To'] = COMMASPACE.join(send_to)
    _msg['Date'] = formatdate(localtime=True)
    _msg.attach(MIMEText(_text=body, _subtype=_text_type, _charset='utf-8'))

    for _file in attachments:
        _file_name = os.path.basename(_file)
        _attached_file = MIMEText(open(_file, 'rb').read(), 'base64', 'utf-8')
        _attached_file["Content-Type"] = 'application/octet-stream'
        _attached_file["Content-Disposition"] = 'attachment; filename="%s"' % _file_name
        _msg.attach(_attached_file)

    _smtp = smtplib.SMTP()
    try:
        _smtp.connect(config.MAIL_SERVER)
        print "Connect to smtp server successfully."

        _smtp.ehlo()
        _smtp.starttls()
        _smtp.login(config.MAIL_ADMIN_USERNAME, config.MAIL_ADMIN_PASSWORD)
        print "Login smtp server successfully."

        _smtp.sendmail(config.MAIL_SENDER_ADDR, send_to, _msg.as_string())
        print("Send mail successfully!")
    except:
        _type, _value, _tb = sys.exc_info()
        print "Send mail failed, error message: %s" % _value
    finally:
        _smtp.quit()
"""
if __name__ == '__main__':
    send_mail("lixiulan89@163.com", "111111", "aaaaaa", ["E:/ 123.txt"])
"""