import argparse
import cv2
from utils.restorer import Restorer
from utils.audio_copy import copyAudio2Video
from utils.tools import get_temp_path,remove_file


def videoEnhance (video_path , output_video_path):
    restorer = Restorer()

    output_temp_path = get_temp_path(output_video_path)
    video_capture = cv2.VideoCapture(video_path)

    # 获取输入视频文件的基本信息
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 设置输出视频文件的编解码器和帧率
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video = cv2.VideoWriter(output_temp_path, fourcc, fps, (width, height))

    # 循环读取视频中的每一帧
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

    # 把源视频的音频拷贝过去合成新视频文件
    copyAudio2Video(video_path, output_temp_path, output_video_path)

    # 删除中间的临时文件
    remove_file(output_temp_path)

    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i',
        '--input',
        type=str,
        required=True,
        metavar='请输入要处理的视频文件路径',
        help='请输入要处理的视频文件路径')

    parser.add_argument(
        '-o',
        '--output',
        type=str,
        required=True,
        metavar='请输入输出文件的路径',
        help='请输入输出文件的路径')

    args = parser.parse_args()
    videoEnhance(args.input, args.output)

if __name__ == '__main__':
    main()