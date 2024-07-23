from pathlib import Path

from pydantic import EmailStr
from app.tasks.celery import celery_app
from PIL import Image

import smtplib

from app.tasks.email_templates import create_new_message

from app.config import settings



from time import sleep

@celery_app.task
def process_pic(
    path: str,
):
    im_path = Path(path)
    im = Image.open(im_path)
    im_resized_1000_500 = im.resize((1000, 500))
    im_resized_200_100 = im.resize((200, 100))
    im_resized_1000_500.save(f"app/static/images/im_resized_1000_500_{im_path.name}")
    im_resized_200_100.save(f"app/static/images/resized_200_100_{im_path.name}")
    
@celery_app.task
def send_comfirmation_email(
    registration_info: dict,
    email_to: EmailStr
    ):
    msg_content = create_new_message(registration_info, email_to)
    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg_content)
    