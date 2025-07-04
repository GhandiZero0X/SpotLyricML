import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class SpotifyAPI:
    def __init__(self, client_id, client_secret):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyClientCredentials(
                client_id=client_id,
                client_secret=client_secret
            )
        )

    def search_tracks(self, query, n_tracks=50):  # Meningkatkan limit agar dapat lebih banyak hasil
        # Memecah query menjadi bagian-bagian
        parts = query.split(',')
        queries = [part.strip().lower() for part in parts]

        # Membuat hasil pencarian dari Spotify API
        results = self.sp.search(q=query, type='track', limit=n_tracks)
        print(f"Total tracks fetched from API: {len(results['tracks']['items'])}")

        # Menyaring hasil yang cocok dengan kriteria spesifik
        exact_matches = []
        for track in results['tracks']['items']:
            track_name = track['name'].lower()
            artist_name = track['artists'][0]['name'].lower()
            album_name = track['album']['name'].lower()

            for q in queries:
                if q in track_name or q in artist_name or q in album_name:
                    exact_matches.append(track)
                    break  # Jika cocok dengan satu query, langsung simpan dan keluar dari loop

        # Mengembalikan hasil pencarian yang cocok
        track_urls = []
        if exact_matches:
            print("Exact matches found:\n")
            for idx, track in enumerate(exact_matches[:5]):  # Ambil maksimal 5 lagu
                print(f"{idx + 1}: {track['name']} by {track['artists'][0]['name']}")
                print(f"   Album: {track['album']['name']} | Release Date: {track['album']['release_date']}")
                print(f"   Popularity: {track['popularity']} | Spotify Link: {track['external_urls']['spotify']}")
                track_urls.append(track['external_urls']['spotify'])
                print()
        else:
            print("No exact matches found. Showing closest results:\n")
            for idx, track in enumerate(results['tracks']['items']):
                print(f"{idx + 1}: {track['name']} by {track['artists'][0]['name']}")
                print(f"   Album: {track['album']['name']} | Release Date: {track['album']['release_date']}")
                print(f"   Popularity: {track['popularity']} | Spotify Link: {track['external_urls']['spotify']}")
                track_urls.append(track['external_urls']['spotify'])
                print()

        return track_urls
