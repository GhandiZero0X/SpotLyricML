# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
# import pandas as pd
# import time

# # Set your Spotify API credentials
# client_id = '39fe95ffe5de45c9af582eca60a0d21f'
# client_secret = '88c534dbbe3b4e5d8e45016024c3dc15'
# redirect_uri = 'https://github.com/GhandiZero0X/SpotLyricML.git'

# # Initialize Spotipy with user authorization
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
#     client_id=client_id,
#     client_secret=client_secret,
#     redirect_uri=redirect_uri,
#     scope="user-read-recently-played"
# ))

# # Function to get audio features of a track
# def get_track_features(track_id):
#     features = sp.audio_features(track_id)[0]
#     return {
#         'Danceability': features['danceability'],
#         'Energy': features['energy'],
#         'Loudness': features['loudness'],
#         'Speechiness': features['speechiness'],
#         'Acousticness': features['acousticness'],
#         'Instrumentalness': features['instrumentalness'],
#         'Liveness': features['liveness'],
#         'Valence': features['valence'],
#         'Tempo': features['tempo']
#     }

# # Function to get recently played tracks and save to CSV
# def get_recently_played_tracks():
#     results = sp.current_user_recently_played(limit=50)
#     track_data = []

#     for item in results['items']:
#         track = item['track']
#         track_info = {
#             'Track Name': track['name'],
#             'Artist': track['artists'][0]['name'],
#             'Album': track['album']['name'],
#             'Release Date': track['album']['release_date'],
#             'Duration (ms)': track['duration_ms'],
#             'Played At': item['played_at']
#         }
        
#         # Get audio features and merge with track info
#         track_features = get_track_features(track['id'])
#         track_info.update(track_features)
        
#         track_data.append(track_info)
#         time.sleep(0.1)  # Optional delay to avoid rate limits

#     # Convert list of dictionaries to a DataFrame and save to CSV
#     df = pd.DataFrame(track_data)
#     df.to_csv('spotify_recently_played.csv', index=False)
#     print("Data saved to spotify_recently_played.csv")

# # Run the function
# get_recently_played_tracks()

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import time

# Set your Spotify API credentials
client_id = '39fe95ffe5de45c9af582eca60a0d21f'
client_secret = '88c534dbbe3b4e5d8e45016024c3dc15'
redirect_uri = 'https://github.com/GhandiZero0X/SpotLyricML.git'

# Initialize Spotipy with necessary scope
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope="user-library-read"
))

# Function to get track data by release year
def get_tracks_by_year(year):
    tracks = []
    query = f'year:{year}'  # Search filter for release year
    limit = 50
    offset = 0
    
    while True:
        results = sp.search(q=query, type='track', limit=limit, offset=offset)
        if not results['tracks']['items']:
            break
        
        for item in results['tracks']['items']:
            track = item
            track_info = {
                'Track Name': track['name'],
                'Artist': track['artists'][0]['name'],
                'Album': track['album']['name'],
                'Release Date': track['album']['release_date'],
                'Track ID': track['id']
            }
            
            # Get audio features if available
            track_features = get_track_features(track['id'])
            track_info.update(track_features)
            
            tracks.append(track_info)
        
        # Increment offset for pagination
        offset += limit
        time.sleep(0.1)  # Short delay to prevent rate limiting

    return tracks

# Function to get audio features for a specific track
def get_track_features(track_id):
    features = sp.audio_features(track_id)[0]
    if features:  # Check if features are available
        return {
            'Danceability': features['danceability'],
            'Energy': features['energy'],
            'Loudness': features['loudness'],
            'Speechiness': features['speechiness'],
            'Acousticness': features['acousticness'],
            'Instrumentalness': features['instrumentalness'],
            'Liveness': features['liveness'],
            'Valence': features['valence'],
            'Tempo': features['tempo']
        }
    return {}

# Collect data for a range of years and save to CSV
def collect_data_for_years(start_year, end_year):
    all_tracks = []
    
    for year in range(start_year, end_year + 1):
        print(f"Collecting tracks for year {year}...")
        tracks = get_tracks_by_year(year)
        all_tracks.extend(tracks)
        time.sleep(0.5)  # Delay between years to avoid rate limits

    # Convert list of dictionaries to DataFrame and save as CSV
    df = pd.DataFrame(all_tracks)
    df.to_csv('spotify_tracks_by_year.csv', index=False)
    print("Data saved to spotify_tracks_by_year.csv")

# Example: Collect data from 2018 to 2020
collect_data_for_years(2018, 2020)
