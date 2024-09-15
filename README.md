# Spotify Playlist Downloader!

This Python script allows users to easily download songs from a Spotify playlist by extracting track URLs and using [SpotDL](https://github.com/spotDL/spotify-downloader) to download each song. The script supports downloading from both user playlists and liked songs, making it a versatile tool for offline listening.

Features:
- Extracts song URLs from a specified Spotify playlist or user's liked songs.
- Downloads songs using SpotDL via a command-line subprocess.
- Supports batch downloading of multiple songs in one go.
- Includes automatic caching of song URLs for future use.

## How to run the program

Clone this repository into a directory of your choice locally using by first navigating to your chosen directory using `cd path/to/your/directory`, and then cloning the repository using 
```
git clone https://github.com/Titwik/Spotify-Song-Download.git
```
You can then navigate to the repo using `cd Spotify-Song-Download`. 

Begin by installing the pre-requisite packages by running 

```
pip install -r requirements.txt
```
Now, you'll need to get your Client ID and Client Secret from the Spotify for Developers page.

1. Navigate to the [Spotify for Developers](https://developer.spotify.com/) and log into your Spotify account.
2. Go to your dashboard.
3. Click on 'Create an app'
4. Pick an ‘App name’ and ‘App description’ of your choice, set the 'redirect uri' as "http://localhost:5000/callback" and mark the 'Spotify WebAPI' checkbox.
5. After creation, you see your ‘Client Id’ and you can click on 'View client secret' to unhide your 'Client secret'.
6. Open the terminal and navigate to the repository
7. Paste the following lines into the terminal:
~~~
touch .env
nano .env
~~~
8. Paste the following into your .env file:
```
client_id = "YOUR CLIENT ID"
client_secret = "YOUR CLIENT SECRET"
redirect_uri = "http://localhost:5000/callback"
```
9. Copy your Client ID and Client Secret, and paste them in the .env file at the appropriate entries (make sure it's pasted within the "speech marks"). Save the file when done.

Now you're ready to run the program by entering 
```
python download_songs.py
```
into the terminal. 

## Obtaining the playlist ID

To start downloading songs, you will first need the playlist ID of the playlist you want to download. To do this:

1. Open the Spotify website and click on the playlist you would like to download
2. The URL of the playlist should look something like "https://open.spotify.com/playlist/{PLAYLIST ID}".
3. Copy the playlist ID and paste it into the program when prompted.

