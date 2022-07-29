from flask import Flask, request, url_for, redirect, render_template, jsonify
import anime
import os


# Initalise the Flask app
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    # html -> python
    similar_shows = []
    if request.method == "POST":
        anime_name = request.form["anime_show"]
        print(f"{anime_name}")
        similar_shows = anime.get_similar_items(anime_name)
    return render_template("index.html", shows=similar_shows)


@app.route("/similar-item", methods=["POST"])
def similar_items():
    return render_template("index.html")


# if "DYNO" in os.environ and os.path.isdir(".dvc"):
#     os.system("dvc config core.no_scm true")
#     if os.system(f"dvc pull") != 0:
#         exit("dvc pull failed")
#     os.system("rm -r .dvc .apt/usr/lib/dvc")

def load_up_models():
    if os.path.isdir(".dvc"):
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
            try:
                os.system("rm -r .dvc .apt/usr/lib/dvc")
            except OSError as error:
                print("OS Error: {0}".format(error))
        else:
            print("model_lite_KNNBasic.pickle doesn't exist")

if __name__ == "__main__":
    load_up_models()
    app.run()

    print("App is running....")
