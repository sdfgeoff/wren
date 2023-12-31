import sys
import requests


OCTOPRINT_API_URL = "http://192.168.0.109/api"
OCTOPRINT_AUTH_KEY = "EEB5B000E4CC45E0A9AAB6932B2703BC"



def octo(path):
    return f"{OCTOPRINT_API_URL}/{path}"

headers = {
    "Authorization": f"Bearer {OCTOPRINT_AUTH_KEY}"
}

def upload_file(remote_path, local_file_path):
    print(f"Uploading {local_file_path}")
    upload_file_request = requests.post(
        octo(f'files/local'), 
        headers=headers, 
        files={
            "file": (remote_path, open(local_file_path).read())
        }
    )

    #print(upload_file_request.request.body.decode('utf-8'))
    assert upload_file_request.status_code == 201, f"Failed to upload file: {upload_file_request.text}"


if __name__ == "__main__":
    PROJECT_NAME = sys.argv[1]
    LOCAL_BASE_DIR = sys.argv[2]
    LOCAL_FILES = sys.argv[3:]

    for local_file_path in LOCAL_FILES:
        remote_path = local_file_path.replace(LOCAL_BASE_DIR, f'{PROJECT_NAME}')
        upload_file(remote_path, local_file_path)