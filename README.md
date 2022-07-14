# anime-ml-webapp

Simple webapp that uses the models in anime-ml repo https://github.com/HWaiChan/anime-ml. 
We can query similar anime shows using various techniques such as Baseline, nearest neighbors (kNN) and matrix factorisation.


## Architecture

JS FE <-----> python BE (with the models to load)

## Next
- CI/CD with Heroku (Need to set up the basic MLOps using dvc-gdrive)
- Introduce React in FE/Client.
- 

## Later plans

- A way to pull data (new ratings and animes shows) from MyAnimeList to update models.
- Add profiles (either locally or grabbing from MyAnimeList users) to recommend anime shows. 

