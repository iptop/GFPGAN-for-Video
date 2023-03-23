import cv2
from utils.restorer import Restorer
from utils.audio_copy import copyAudio2Video
from utils.tools import get_temp_path,remove_file

restorer = Restorer()

video_path = 'E:\\RES\\1.mp4'
output_video_path = 'E:\\RES\\2.mp4'
output_temp_path = get_temp_path(output_video_path)
video_capture = cv2.VideoCapture(video_path)

# 获取输入视频文件的基本信息
fps = video_capture.get(cv2.CAP_PROP_FPS)
width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 设置输出视频文件的编解码器和帧率
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter(output_temp_path, fourcc, fps, (width, height))

# 循环读取视频中的每一帧，并将其保存为图片
while True:
    # 读取一帧视频
    success, image = video_capture.read()
    # 判断视频是否已经读取完毕
    if not success:
        break
    frame = restorer.enhance(image)
    output_video.write(frame)

# 关闭视频文件
video_capture.release()
output_video.release()

#把源视频的音频拷贝过去合成新视频文件
copyAudio2Video(video_path,output_temp_path,output_video_path)

#删除中间的临时文件
remove_file(output_temp_path)
