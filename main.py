import torch

print("PyTorch работает") if torch.cuda.is_available() else print ("Видюхи нет")