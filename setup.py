import os
from pathlib import Path


if "DYNO" in os.environ and os.path.isdir(".dvc"):
    os.system("dvc config core.no_scm true")
    Path(".dvc/tmp").mkdir(parents=True, exist_ok=True)
    gdrive_data = os.getenv("GDRIVE_CREDENTIALS_DATA")
    f = open(".dvc/tmp/credentials.json", "w")
    f.write(gdrive_data)
    f.close()
    os.system(
        "dvc remote modify --local myremote gdrive_service_account_json_file_path .dvc/tmp/credentials.json"
    )
    if os.system(f"dvc pull") != 0:
        exit("dvc pull failed")
    if os.path.exists("model_lite_KNNBasic.pickle"):
        print("model_lite_KNNBasic.pickle exists")
        os.system("rm -r .dvc .apt/usr/lib/dvc")
    else:
        print("model_lite_KNNBasic.pickle doesn't exist")
