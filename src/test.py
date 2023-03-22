import os
from utils.gfpganer import GFPGANer
import cv2
from basicsr.utils import imwrite
#当前脚本所在目录
CURRENT_SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))

#模型文件路径
model_path = os.path.join(CURRENT_SCRIPT_PATH,'../gfpgan/weights', 'GFPGANv1.3' + '.pth')

#加载模型
restorer = GFPGANer(
    model_path=model_path,
    upscale=1,
    arch='clean',
    channel_multiplier=2,
    bg_upsampler=None)


img_path = os.path.join( CURRENT_SCRIPT_PATH ,'../GFPGAN-1.3.8/' , 'inputs/cropped_faces/Adele_crop.png' )

save_restore_path = os.path.join( CURRENT_SCRIPT_PATH ,'../GFPGAN-1.3.8/' , 'results/Adele_crop.png' )

input_img = cv2.imread(img_path, cv2.IMREAD_COLOR)

# restore faces and background if necessary
cropped_faces, restored_faces, restored_img = restorer.enhance(
    input_img,
    has_aligned=False,
    only_center_face=False,
    paste_back=True,
    weight=0.5)

# save restored img
if restored_img is not None:
    imwrite(restored_img, save_restore_path)