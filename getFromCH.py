import youtube_dl

# チャンネルのURLを設定
channel_url = 'https://www.youtube.com/@TheFatRat/videos'  # チャンネルのURLをここに入力

# youtube_dlのオプションを設定
ydl_opts = {
    'quiet': True,
    'extract_flat': True,
    'force_generic_extractor': True,
}

# 動画URLを保存するリスト
video_urls = []

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    # チャンネルの情報を取得
    channel_info = ydl.extract_info(channel_url, download=False)

    # 各動画のURLをリストに追加
    if 'entries' in channel_info:
        for video in channel_info['entries']:
            video_urls.append(video['url'])

# URLをテキストファイルに保存
with open('channel_video_urls.txt', 'w') as file:
    for url in video_urls:
        file.write(f'https://youtube.com/watch?v={url}\n')

print(f"{len(video_urls)} 件の動画URLを抽出しました。")
