import torch
from utils.metal_check import check_device


device = check_device()

print(f"Используем устройство: {device}")
