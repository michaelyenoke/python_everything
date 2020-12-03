from pytube import YouTube

yt=YouTube("https://www.youtube.com/watch?v=VW8AJq6FgxU&feature=youtu.be")
print("下載Youtube影片\n 影片標題："+yt.title)

GetVideo=yt.streams.filter(file_extension="mp4",resolution="720p").all()
print(GetVideo)
stream = GetVideo[0]
stream.download("C:/Users/MichaelCHEN/Desktop/youtube_download")
