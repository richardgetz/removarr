from pyarr import SonarrAPI
from pyarr import RadarrAPI
import json


secrets = None
with open("secrets.json", "r") as f:
    secrets = json.load(f)
def shows():
    print("Checking Sonarr")
    # Instantiate SonarrAPI Object
    sonarr = SonarrAPI(secrets["sonarr"]["host"], secrets["sonarr"]["key"])

    # Get and print TV Shows
    for series in sonarr.get_series():
        if (not series["monitored"] and series["episodeFileCount"] == 0):
            print(f'Removing {str(series["title"])} from monitoring.')
            sonarr.del_series(id_=series["id"], delete_files=True)
        
def movies():
    print("Checking Movies")
    # Instantiate SonarrAPI Object
    radarr = RadarrAPI(secrets["radarr"]["host"], secrets["radarr"]["key"])

    # Get and print TV Shows
    for movie in radarr.get_movie():
        # print(movie["title"], movie["monitored"], movie["id"], movie["hasFile"])
        if (not movie["monitored"] and not movie["hasFile"]):
            print(f'Removing {str(movie["title"])} from monitoring.')
            radarr.del_movie(id_=movie["id"], delete_files=True, add_exclusion=False)

shows()
movies()