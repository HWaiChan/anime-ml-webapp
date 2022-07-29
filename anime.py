from surprise import dump
import os
import pandas as pd
import surprise

model_lite_filename = "model_lite_KNNBasic.pickle"
file_name = os.path.expanduser(model_lite_filename)
_, loaded_model = dump.load(file_name)
print(f"{loaded_model.__class__.__name__} loaded.")
# loaded_model = surprise.KNNBaseline()


def get_similar_items(anime_name):
    return [
        "This tool doesn't work as heroku free tier cannot support the size of my model. Visit https://huggingface.co/spaces/NomiWai/anime-collaborative-filtering-space for a working MVP"
    ]
    # return extract_similar_items_from_model(loaded_model, anime_name)["Title"].tolist()


def extract_similar_items_from_model(loaded_knn_model, anime_title, k=30):
    iid = loaded_knn_model.trainset.to_inner_iid(anime_title)
    neighbor_ids = loaded_knn_model.get_neighbors(iid, k=k)
    neightbors = (
        loaded_knn_model.trainset.to_raw_iid(inner_id) for inner_id in neighbor_ids
    )
    df = pd.DataFrame(neightbors, columns=["Title"])
    return df
