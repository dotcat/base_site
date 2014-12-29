from django.core.files import Storage
from django.conf import settings
from django.core.files import File


class GoogleDriveStorage(Storage):

    def __init__(self, location=None, base_url=None):
        if location is None:
            location = settings.MEDIA_ROOT
        if base_url is None:
            base_url = settings.MEDIA_URL

        def _open(self, name, mode='rb'):
            return File(open(self.path(name), mode))

        def _save(self, name, content):
        	# TODO: Dokończyć: Integracja z Django
            pass
