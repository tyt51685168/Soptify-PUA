import spotipy
import pandas as pd

class playlist_info:
    
    def __init__(self, spotify_obj, playlist_uri=None):
        self.playlist_uri = playlist_uri
        self.track = spotify_obj.playlist_tracks(self.playlist_uri)

    def get_contents(self) -> pd.DataFrame:
        """
        照著 playlist 順序取出 song name & artists name & uri
        """
        temp_list = []

        for song in self.track['items']:
            temp_dict = {}

            song_name = song['track']['name']
            song_uri = song['track']['uri']    
               
            for i in range(len(song['track']['artists'])):
                singer_name = song['track']['artists'][i]['name']
                singer_uri = song['track']['artists'][i]['uri']
                
                temp_dict['song_name'] = song_name
                temp_dict['singer_name'] = singer_name
                temp_dict['song_uri'] = song_uri
                temp_dict['singer_uri'] = singer_uri
            
            temp_list.append(temp_dict)
        
        df = pd.DataFrame(temp_list)

        return df