## 环境配置

```bash
conda create -n GFPGAN-for-Video python=3.9
conda activate GFPGAN-for-Video

cd GFPGAN-for-Video

pip install -r requirements.txt

#背景修复需要用到的
pip install realesrgan
```

## 下载模型
```bash
wget https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.3.pth -P GFPGAN-1.3.8/experiments/pretrained_models
```

## 安装pytouch
gpu版本的pytouch不是必须的，没有安装的话会自动使用cpu计算
```bash
pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu117
```

## 安装ffmpeg
```bash
conda install -c conda-forge ffmpeg
```