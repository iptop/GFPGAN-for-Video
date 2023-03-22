## 环境配置

```bash
conda create -n GFPGAN-for-Video python=3.9
conda activate GFPGAN-for-Video

cd GFPGAN-for-Video

pip install -r requirements.txt
```

## 下载模型
```bash
wget https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.3.pth -P GFPGAN-1.3.8/experiments/pretrained_models
```