import spotipy

def show_playlist_info(spotify_obj, playlist_uri):
    """
    spotify_obj: 放入API obj
    playlist_uri: 想顯示資訊的 playlist uri
    """
    playlist_data = spotify_obj.playlist(playlist_uri)
    thumbups = playlist_data['followers']['total']
    number_of_songs = playlist_data['tracks']['total']

    print(f"{playlist_data['name']}: {playlist_data['description']}")
    print(f"{thumbups}人按讚。共{number_of_songs}首歌")