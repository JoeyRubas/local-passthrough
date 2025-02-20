import datetime
from flask import render_template
from flask_mail import Message

from deployer.extensions import mail

__email = 'joeymrubas@gmail.com'


def __send_email(subject, recipient, text_body, html_body):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp}.txt"
    
    email_content = f"Subject: {subject}\nRecipient: {recipient}\n\n{text_body}\n\n{html_body}"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(email_content)
    
    print(f"Email simulated and saved as {filename}")
    return True  



def send_confirmation(tournament, password):
    txt = render_template('mail/confirmation.txt',
                          tournament_name=tournament.name,
                          password=password)
    html = render_template('mail/confirmation.html',
                           tournament_name=tournament.name,
                           password=password)
    subject = 'Your MIT-Tab Tournament Has Been Created!'
    return __send_email(subject, tournament.email, txt, html)


def send_warning(tournament):
    txt = render_template('mail/warning.txt', tournament=tournament)
    html = render_template('mail/warning.html', tournament=tournament)
    subject = 'Your mit-tab tournament will be deleted soon!'
    return __send_email(subject, tournament.email, txt, html)


def send_notification(tournament_name):
    """
    Notify myself when tournaments are created so I'm not clueless
    """
    txt = 'Tournament: {}'.format(tournament_name)
    html = '<p>Tournament: {}</p>'.format(tournament_name)
    subject = 'A tournament has been created'
    return __send_email(subject, __email, txt, html)
