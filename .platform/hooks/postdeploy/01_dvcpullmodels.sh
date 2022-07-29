#!/bin/sh
pip install dvc[gdrive]
mkdir -p .dvc/tmp
dvc remote modify myremote gdrive_use_service_account true
echo "${GDRIVE_CREDENTIALS_DATA}" > .dvc/tmp/credentials.json
dvc remote modify --local myremote gdrive_service_account_json_file_path .dvc/tmp/credentials.json
dvc pull -v