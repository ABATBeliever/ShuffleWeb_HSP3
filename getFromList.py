from pytube import Playlist

# Replace with your playlist URL
playlist_url = 'hoge'
# Create Playlist object
playlist = Playlist(playlist_url)

# Extract video URLs
video_urls = [video.watch_url for video in playlist.videos]

# Save URLs to a text file
with open('video_urls.txt', 'w') as file:
    for url in video_urls:
        file.write(f'{url}\n')

print(f"Extracted {len(video_urls)} video URLs.")
