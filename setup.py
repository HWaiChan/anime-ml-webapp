import os


if "DYNO" in os.environ and os.path.isdir(".dvc"):
    os.system("dvc config core.no_scm true")
    gdrive_data = os.getenv("GDRIVE_CREDENTIALS_DATA")
    f = open(".dvc/tmp/credentials.json", "a")
    f.write(gdrive_data)
    f.close()
    os.system(
        "dvc remote modify --local myremote gdrive_service_account_json_file_path .dvc/tmp/credentials.json"
    )
    if os.system(f"dvc pull") != 0:
        exit("dvc pull failed")
    os.system("rm -r .dvc .apt/usr/lib/dvc")
