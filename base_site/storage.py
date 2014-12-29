from django.core.files.storage import Storage
from django.conf import settings
from django.core.files import File
import nudrive
import requests
import StringIO


def retrieve_file(url):
    response = requests.get(url)
    return StringIO.StringIO(response.content)


class GoogleDriveStorage(Storage):

    def __init__(self, location=None, base_url=None):
        if location is None:
            location = settings.MEDIA_ROOT
        if base_url is None:
            base_url = settings.MEDIA_URL

        def _open(self, name, mode='rb'):
            f = retrieve_file(name)
            # ContentFIle if error
            return File(open(f, mode))

        def _save(self, name, content):
            
            pass
