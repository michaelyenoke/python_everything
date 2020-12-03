from pytube import YouTube

yt=YouTube("影片網址")
print("下載Youtube影片\n 影片標題："+yt.title)

GetVideo=yt.streams.filter(file_extension="mp4",resolution="720p").all()
print(GetVideo)
stream = GetVideo[0]
stream.download("下載路徑")
