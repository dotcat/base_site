from oauth2client.client import SignedJwtAssertionCredentials
from apiclient.http import MediaFileUpload
from apiclient.discovery import build
# import pprint
import httplib2


client_email = '911984682386-rr5rg1e4m5v6j0mk89jniqcon26pgjic@developer\
.gserviceaccount.com'

with open("nudrive.pem") as f:
    private_key = f.read()

credentials = SignedJwtAssertionCredentials(
    client_email,
    private_key,
    'https://www.googleapis.com/auth/drive')

http = httplib2.Http()

http = credentials.authorize(http)


def create_public_folder(service, folder_name):
    body = {
        'title': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }

    file = service.files().insert(body=body).execute()

    permission = {
        'value': '',
        'type': 'anyone',
        'role': 'reader'
    }

    service.permissions().insert(
        fileId=file['id'], body=permission).execute()

    return file


drive_service = build('drive', 'v2', http=http)

folder_id = create_public_folder(drive_service, 'public')['id']
print(folder_id)

FILENAME = "document.txt"

media_body = MediaFileUpload(FILENAME, mimetype='text/plain', resumable=True)
body = {
    'title': 'document2',
    'description': 'A test document',
    'mimeType': 'text/plain',
    'parents': [
        {
            "kind": "drive#fileLink",
            "id": folder_id,
        },
    ]
}
file = drive_service.files().insert(body=body, media_body=media_body).execute()
# pprint.pprint(file)
file_id = file['id']

print('www.googledrive.com/host/' + folder_id + '/' + body['title'])
