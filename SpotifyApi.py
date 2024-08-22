import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyAPI:
    def __init__(self, client_id, client_secret):
        self.sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

    def search_tracks(self, query, n_tracks=10):
        # Coba mencari dengan query spesifik terlebih dahulu
        results = self.sp.search(q=query, type='track', limit=n_tracks)
        exact_matches = []

        for track in results['tracks']['items']:
            # Cocokkan secara tepat nama track atau artis
            if query.lower() in track['name'].lower() or query.lower() in track['artists'][0]['name'].lower():
                exact_matches.append(track)

        # Jika ada hasil yang cocok secara spesifik
        if exact_matches:
            track_urls = []
            print("Exact matches found:\n")
            for idx, track in enumerate(exact_matches):
                print(f"{idx + 1}: {track['name']} by {track['artists'][0]['name']}")
                print(f"   Album: {track['album']['name']} | Release Date: {track['album']['release_date']}")
                print(f"   Popularity: {track['popularity']} | Spotify Link: {track['external_urls']['spotify']}")
                track_urls.append(track['external_urls']['spotify'])
                print()
            return track_urls
        
        # Jika tidak ada hasil yang cocok secara spesifik, tampilkan semua hasil
        else:
            print("No exact matches found. Showing closest results:\n")
            track_urls = []
            for idx, track in enumerate(results['tracks']['items']):
                print(f"{idx + 1}: {track['name']} by {track['artists'][0]['name']}")
                print(f"   Album: {track['album']['name']} | Release Date: {track['album']['release_date']}")
                print(f"   Popularity: {track['popularity']} | Spotify Link: {track['external_urls']['spotify']}")
                track_urls.append(track['external_urls']['spotify'])
                print()
            return track_urls
