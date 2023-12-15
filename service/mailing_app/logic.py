from django.core.mail import send_mail
from yandex_case.config import config
import celery
from celery import shared_task
from django.template.loader import render_to_string
from event_app.models import UserEventRel


@shared_task
def send_to_defined_person(instance_id):
    """
    function that sends email to the user that
    created relation with event
    """

    # getting instance
    instance = UserEventRel.objects.filter(id=instance_id)[0]

    # creating context
    context = {
        'user_name': instance.user.username,
        'event_name': instance.event.event_name,
        'event_place': instance.event.event_place,
        'event_date': instance.event.event_date,
        'event_time': instance.event.event_time,
    }

    # getting html code
    msg_html = render_to_string(template_name='mailing_app/join-event-person.html', context=context)

    # sending email
    send_mail(subject="Hello! You have joined event!",
              message="",
              from_email=config.get('mail').get('EMAIL_HOST_USER'),
              recipient_list=[instance.user.email],
              fail_silently=False,
              html_message=msg_html)


if __name__ == '__main__':
    send_to_defined_person()
