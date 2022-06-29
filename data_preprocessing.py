import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import lyricsgenius as lg
import os
import config.playlists as conf
import tools.playlists as pl
import tools.lyrics_search as ls

def get_playlist_info_with_lyrics(spotify_id=None, spotify_secret=None, lyricsGenius_token=None, search_for_lyrics=False):
    
    try:
        # 記得在設定完環境變數後要重開 vscode，才不會一直以為自己沒設定成功
        id = os.environ.get(spotify_id)
        secret = os.environ.get(spotify_secret)
        token = os.environ.get(lyricsGenius_token)

        # 建立 API obj. 
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=id, client_secret=secret))
        genius = lg.Genius(token)

        # 取得 config. 歌單
        uri = conf.personal_playlists()

        # 抓取歌單 info.
        pua = []
        for playlist_ in uri: # 雖然 playlist dict 裡只有一個歌單，還是用 for 去寫，未來有可能一次做多個歌單的分析
            pua.append(pl.playlist_info(spotify_obj=spotify, playlist_uri=playlist_))

        # 透過自定義 get_contents func. 將每個歌單資訊轉換成 df，欄位僅包含 singer & song 的名字與 uri
        contents = []
        for obj in pua:
            contents.append((obj.get_contents()))

        # 預設先不加 lyrics search，要花滿多時間搜尋
        if search_for_lyrics == True:
            contents = ls.add_lyrics(genius_obj=genius, list_of_df=contents, song_name='song_name', singer_name='singer_name')
    
    except Exception as e:
        print('Data pre-processing error:' + str(e))
    
    finally:
        return contents