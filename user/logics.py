import os

from django.conf import settings


def save_upload_avatar(uid, upload_avatar):
    '''保存上传的用户头像'''
    filename = 'Avatar-%s' % uid
    filepath = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, filename)

    with open(filepath, 'wb') as fp:
        for chunk in upload_avatar.chunks():
            fp.write()