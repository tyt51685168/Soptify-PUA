import lyricsgenius as lg

def search_song(genius_obj, song_name, artist):
    """
    Search for lyrics on "LyricsGenius website", return "None" when no result founded.
    """
    song = genius_obj.search_song(title=song_name, artist=artist)
    if song == None:
        return 'None'
    return song.lyrics

def add_lyrics(genius_obj, list_of_df, song_name_col, singer_name_col):
    for df in list_of_df:
        df['lyrics'] = df.apply(lambda x: search_song(genius_obj, x[song_name_col], x[singer_name_col]), axis=1)

    return df