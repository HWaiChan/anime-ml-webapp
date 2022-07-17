from surprise import dump
import os
import pandas as pd

# if "DYNO" in os.environ and os.path.isdir(".dvc"):
#     os.system("dvc config core.no_scm true")
#     if os.system(f"dvc pull") != 0:
#         exit("dvc pull failed")
#     os.system("rm -r .dvc .apt/usr/lib/dvc")
model_filename = "./models/model_KNNBasic.pickle"
model_lite_filename = "./models/model_lite_KNNBasic.pickle"
file_name = os.path.expanduser(model_lite_filename)
_, loaded_model = dump.load(file_name)
print(f"{loaded_model.__class__.__name__} loaded.")


def get_similar_items(anime_name):
    return extract_similar_items_from_model(loaded_model, anime_name)["Title"].tolist()


def extract_similar_items_from_model(loaded_knn_model, anime_title, k=30):
    iid = loaded_knn_model.trainset.to_inner_iid(anime_title)
    neighbor_ids = loaded_knn_model.get_neighbors(iid, k=k)
    neightbors = (
        loaded_knn_model.trainset.to_raw_iid(inner_id) for inner_id in neighbor_ids
    )
    df = pd.DataFrame(neightbors, columns=["Title"])
    return df
