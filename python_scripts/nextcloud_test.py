import os
from pathlib import Path

from webdav3.client import Client

# requirements
# ---
# webdavclient3


PASSWORD = os.environ.get("NC_PASSWORD")
URL = os.environ.get("NC_URL")
USER = os.environ.get("NC_USER")

options = {
    "webdav_hostname": URL,
    "webdav_login": USER,
    "webdav_password": PASSWORD,
}
print(options)
client = Client(options)
client.verify = True
file: Path = Path("Readme.md")
client.download_file(remote_path=f"/{file}", local_path=str(file))
# client.upload_file(remote_path=f"/updloaded-{file.name}", local_path=str(file))
