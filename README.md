Welcome to download my code. Please note that the author's Python version is 3.8, PyTorch version is 1.11.0, and CUDA version is 11.3. Open the train file and modify the path to start training. Before training, please ensure that the following packages are installed:
cv2, otherwise pip install opencv-python;
psutil, otherwise pip install psutil;
torch, otherwise pip install torch
matplotlib, otherwise run pip install matplotlib
yaml, otherwise run pip install pyyaml
tqdm, otherwise run pip install tqdm
requests, otherwise run pip install requests
timm, otherwise run pip install timm
einops, otherwise run pip install einops
efficientnet_pytorch, otherwise run pip install efficientnet_pytorch
dill, otherwise run pip install dill
pywt, otherwise run pip install PyWavelets
When encountering the following issues:
1. ModuleNotFoundError: No module named xxx
Solution: The corresponding package is missing. First, install the packages using the installation commands for the YOLOV8 environment. If the missing package is still displayed, install the corresponding package (where xxx is the corresponding package).
2. RuntimeError: Dataset ‘xxxxx’ error ❌
Change all paths in the .yaml file to absolute paths.
