import json
import os

import boto3

from celery import shared_task
import uuid
from django.conf import settings

from yandex_case.settings import BASE_DIR
from event_app.models import Event
# from file_uploader_app.models import ImageTestTable


def set_up():
    bucket_name = 'yandexcasebackendstorage'
    endpoint_url = 'https://storage.yandexcloud.net'

    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        endpoint_url=endpoint_url,
        aws_access_key_id='YCAJE5PDVsfeJkHYmNI2dyfTH',
        aws_secret_access_key='YCPu2Ut6tDGKTBU1zwBRdeCPDc2kdWCSCJ1gcjFY',
    )

    return s3, bucket_name, endpoint_url


@shared_task
def upload_event(instance):
    # setting up
    instance = Event.objects.get(id=instance)

    s3, bucket_name, endpoint_url = set_up()
    filename = str(uuid.uuid4())

    # uploading
    s3.upload_file((BASE_DIR + instance.photo.url), bucket_name, filename)
    os.remove((BASE_DIR + instance.photo.url))

    # setting url
    instance.photo = None
    instance.photo_url = endpoint_url + '/' + bucket_name + '/' + filename
    instance.save()


@shared_task
def delete_file(file_url):
    s3 = set_up()
    for_deletion = [
        {
            'key': file_url.split('/')[-1]
        },
    ]
    response = s3.delete_objects(Bucket='bucket-name', Delete={'Objects': for_deletion})
    return response


@shared_task
def test_script():
    print('Hi! 2+2=4')


if __name__ == '__main__':
    pass
    # upload_event()

