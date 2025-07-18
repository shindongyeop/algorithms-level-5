import torch

if torch.cuda.is_available():
    print(f'CUDA available')
else:
    print(f'CUDA unavailable')