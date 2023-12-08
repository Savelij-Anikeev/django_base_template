import os
import boto3
import uuid

from celery import shared_task

from yandex_case.settings import BASE_DIR
from event_app.models import Event


def set_up():
    """
    setting the bucket up
    """

    bucket_name = 'yandexcasebackendstorage'
    endpoint_url = 'https://storage.yandexcloud.net'

    # starting connection
    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        endpoint_url=endpoint_url,
        # Don`t steal it please
        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
    )

    return s3, bucket_name, endpoint_url


@shared_task
def upload_event(obj_id):
    """
    uploading files to the server
    and saving file url to the model instance
    """

    # setting up
    instance = Event.objects.get(id=obj_id)

    s3, bucket_name, endpoint_url = set_up()
    filename = str(uuid.uuid4())    # generating filename

    # uploading
    s3.upload_file((BASE_DIR + instance.photo.url), bucket_name, filename)

    # removing file from server
    os.remove((BASE_DIR + instance.photo.url))

    # setting the url up
    instance.photo = None   # deleting photo cause it`s useless
    instance.photo_url = endpoint_url + '/' + bucket_name + '/' + filename

    # saving instance
    instance.save()


@shared_task
def delete_file(file_url):
    """
    delete file by url
    """

    # setting up
    s3 = set_up()

    # list of obj information
    for_deletion = [
        {
            'key': file_url.split('/')[-1]
        },
    ]

    response = s3.delete_objects(Bucket='bucket-name', Delete={'Objects': for_deletion})

    return response
