import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser

# Masukkan Client ID dan Client Secret dari Spotify
client_id = '39fe95ffe5de45c9af582eca60a0d21f'
client_secret = '88c534dbbe3b4e5d8e45016024c3dc15'

# Mengatur otentikasi
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

def search_tracks(query, n_tracks=10):
    results = sp.search(q=query, type='track', limit=n_tracks)
    if results['tracks']['items']:
        track_urls = []
        for idx, track in enumerate(results['tracks']['items']):
            print(f"{idx + 1}: {track['name']} by {track['artists'][0]['name']}")
            print(f"   Album: {track['album']['name']} | Release Date: {track['album']['release_date']}")
            print(f"   Popularity: {track['popularity']} | Spotify Link: {track['external_urls']['spotify']}")
            track_urls.append(track['external_urls']['spotify'])
            print()
        return track_urls
    else:
        print(f"No results found for query: '{query}'")
        return None

def play_track(track_urls):
    while True:
        if track_urls:
            try:
                choice = int(input("Enter the number of the track you want to play (or 0 to search again): "))
                if choice == 0:
                    break
                elif 1 <= choice <= len(track_urls):
                    webbrowser.open(track_urls[choice - 1])
                else:
                    print("Invalid selection. Please choose a number from the list.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("No tracks available to play.")
            break

def main():
    while True:
        query = input("Enter your search query (song title, artist, or album) or 'exit' to quit: ").strip()
        
        if query.lower() == 'exit':
            print("Exiting the program.")
            break
        
        if query:
            track_urls = search_tracks(query)
            if track_urls:
                play_track(track_urls)
        else:
            print("Please enter a valid search query.")

if __name__ == "__main__":
    main()
