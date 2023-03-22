import ffmpeg

# 指定视频文件和音频文件
video_file = 'E:\\RES\\2.mp4'
audio_file = 'E:\\RES\\1.mp4'

output_file = 'E:\\RES\\3.mp4'


# 读取视频文件和音频文件
video = ffmpeg.input(video_file)
audio = ffmpeg.input(audio_file)

# 将视频和音频合并到一个文件中
output = ffmpeg.output(video, audio, output_file, vcodec='copy', acodec='aac')

# 运行命令并等待完成
ffmpeg.run(output)
