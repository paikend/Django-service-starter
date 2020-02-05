from django.conf import settings
from django.core.files.storage import get_storage_class
from storages.backends.s3boto3 import S3Boto3Storage

if settings.DEBUG:
    PublicMediaStorage = get_storage_class()
    PrivateMediaStorage = get_storage_class()
else:
    from config.settings import production
    class PublicMediaStorage(S3Boto3Storage):
        location = production.AWS_PUBLIC_MEDIA_LOCATION
        file_overwrite = False


    class PrivateMediaStorage(S3Boto3Storage):
        location = production.AWS_PRIVATE_MEDIA_LOCATION
        file_overwrite = False
        default_acl = 'private'
        custom_domain = False
