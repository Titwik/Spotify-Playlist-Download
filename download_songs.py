import subprocess
import os
import json
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

# Load the environment variables    
load_dotenv()

# Set the client id, client secret, redirect_uri, and scope
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
redirect_uri = os.getenv('redirect_uri')
scope = "user-library-read"

# Initialize the Spotify client  
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

# retrieve URLs of songs in a playlist
# retrieving liked songs is defaulted to False. Switch to True if you want your liked songs
def songs_urls(liked_songs = False):

    # initialize a list to hold the urls
    song_urls = []

    # if you want your liked songs
    if liked_songs == True:
        results = sp.current_user_saved_tracks(limit=50)  # Retrieves 50 tracks per request
        
        while results:
            for item in results['items']:
                track = item['track']
                song_url = track['external_urls']['spotify']  # Retrieve the Spotify URL for the song
                song_urls.append(song_url)
            
            # check if there are more songs, if so, retrieve the next batch
            if results['next']:
                results = sp.next(results)
            else:
                break
    
    else: 

        id = input("What is the ID of the playlist you want to download?\n")       
        playlist_id = f'spotify:playlist:{id}'

        try:
            results = sp.playlist_tracks(playlist_id)
            print('Playlist found!')

        except spotipy.exceptions.SpotifyException as e:
            print(f"Error retrieving playlist. Try another playlist?")
            return []

        while results:
            for item in results['items']:
                track = item['track']
                song_url = track['external_urls']['spotify']  # Retrieve the Spotify URL for the song
                song_urls.append(song_url)

            # Check for more songs and get the next batch
            if results['next']:
                results = sp.next(results)
            else:
                break
    
    # cache the data in case it's needed 
    with open('song_urls.json', 'w') as f:
        json.dump(song_urls, f, indent=4)
    
    return song_urls
    
# run spotDL from the terminal
def download_song(song_url):
    try:
        # call spotDL as a command-line command using subprocess
        subprocess.run(['spotdl', song_url], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while downloading: {e}")
    else:
        print(f"Song downloaded successfully: {song_url}")

# begin downloading the songs
def batch_download_songs(song_urls):
    for url in song_urls:
        try:
            # call spotdl to download each song URL
            subprocess.run(['spotdl', url], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error downloading {url}: {e}")
        else:
            print(f"Downloading: {url}")

# Example usage: replace with the actual Spotify track URL
if __name__ == '__main__':

    # call song_urls to generate a list of URLs
    urls = songs_urls()
    
    # download the songs
    if urls:
        batch_download_songs(urls)
    