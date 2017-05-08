import configparser
import imaplib

def check_login(server,port,login,password):
    mail = imaplib.IMAP4_SSL(server,port)
    try:
        mail.login(login,password)
        return(1)
    except:
        return(0)

config = configparser.ConfigParser()
config.read('credentials.conf')

server = config['IMAP']['server']
port = config['IMAP']['port']
login = config['IMAP']['login']
password = config['IMAP']['password']

print(check_login(server,port,login,password))
