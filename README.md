# anime-ml-webapp

Simple webapp that uses the models in anime-ml repo https://github.com/HWaiChan/anime-ml. 
We can query similar anime shows using various techniques such as Baseline, nearest neighbors (kNN) and matrix factorisation.


## Architecture

JS FE <-----> python BE (with the models to load)

## Next
- Introduce React in FE/Client.
- Connectivity to Hugging Face

## Things I have tried and given up
### Heroku dyno to load up model
I had the plan to get Heroku web dyno to fetch the whole model to provide recommendations/similar shows.
The web dyno will use dvc to make calls to my Google Drive to fetch for the model. Once fetched the dyno will load the web app with the model pickle file will be present for the web app to use.

It works fine, however the model is too big (varies from 500MB to 1GB) whilst the RAM limit for free tier Heroku dyno was 512MB. 


## Later plans

- A way to pull data (new ratings and animes shows) from MyAnimeList to update models.
  -  MyAnimeList [API] (https://myanimelist.net/apiconfig/references/api/v2) doesn't have endpoints to fetch ratings from other users
  -  One
- Add profiles (either locally or grabbing from MyAnimeList users) to recommend anime shows. 

