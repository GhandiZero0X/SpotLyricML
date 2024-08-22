import webbrowser
from SpotifyApi import SpotifyAPI

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
    client_id = '39fe95ffe5de45c9af582eca60a0d21f'
    client_secret = '88c534dbbe3b4e5d8e45016024c3dc15'
    
    spotify_api = SpotifyAPI(client_id, client_secret)
    
    while True:
        query = input("Enter your search query (song title, artist, or album) or 'exit' to quit: ").strip()
        
        if query.lower() == 'exit':
            print("Exiting the program.")
            break
        
        if query:
            track_urls = spotify_api.search_tracks(query)
            if track_urls:
                play_track(track_urls)
        else:
            print("Please enter a valid search query.")

if __name__ == "__main__":
    main()
