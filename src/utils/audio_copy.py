import ffmpeg

def copyAudio2Video (audio_file,video_file,output_file) :
    video = ffmpeg.input(video_file)
    audio = ffmpeg.input(audio_file)

    # 将视频和音频合并到一个文件中
    output = ffmpeg.output(video, audio, output_file, vcodec='copy', acodec='aac', y='-y')

    # 运行命令并等待完成
    return ffmpeg.run(output)
