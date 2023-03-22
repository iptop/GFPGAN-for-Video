import os
from .gfpganer import GFPGANer
import cv2
from basicsr.utils import imwrite


class Restorer():

    def __init__(self):
        # 当前脚本所在目录
        CURRENT_SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))

        # 模型文件路径
        model_path = os.path.join(CURRENT_SCRIPT_PATH, '../../gfpgan/weights', 'GFPGANv1.3' + '.pth')

        # 加载模型
        restorer = GFPGANer(
            model_path=model_path,
            upscale=1,
            arch='clean',
            channel_multiplier=2,
            bg_upsampler=None)

        self.restorer = restorer

    def enhance(self, input_img):
        cropped_faces, restored_faces, restored_img = self.restorer.enhance(
            input_img,
            has_aligned=False,
            only_center_face=False,
            paste_back=True,
            weight=0.5)

        return restored_img
