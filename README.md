Welcome to My Code Repository
Thank you for downloading my code!

Notes for Use:
Python version: 3.8

PyTorch version: 1.11.0

To start training, simply open the train file and modify the paths as needed.

Common Issues & Solutions:
ModuleNotFoundError: No module named 'xxx'

This error indicates that a required package is missing.

First, install the YOLOv8 environment dependencies using the official installation commands.

If the error persists, manually install the missing package (xxx refers to the specific package name).

RuntimeError: Dataset 'xxxxx' error ❌

Solution: Change all paths in .yaml to absolute paths instead of relative ones.
