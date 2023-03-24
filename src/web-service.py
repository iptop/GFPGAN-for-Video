from flask import Flask, request
from video_enhance import videoEnhance
app = Flask(__name__)
@app.route('/', methods=['POST'])
def handle_post_request():
    data = request.json  # 获取POST请求的JSON数据

    input_video_path = data.get('input_video_path')
    output_video_path = data.get('output_video_path')

    if input_video_path is None:
        return {'code': 1000 , 'msg':'缺少参数input_video_path'}

    if output_video_path is None:
        return {'code': 1000 , 'msg':'缺少参数output_video_path'}

    videoEnhance(input_video_path,output_video_path)


    return {'code':0}
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)