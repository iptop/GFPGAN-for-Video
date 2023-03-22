import os
from utils import GFPGANer

# 获取当前脚本所在目录
CURRENT_SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(CURRENT_SCRIPT_PATH,'../gfpgan/weights', 'GFPGANv1.3' + '.pth')

restorer = GFPGANer(
    model_path=model_path,
    upscale=1,
    arch='clean',
    channel_multiplier=2,
    bg_upsampler='realesrgan')

dir(restorer)