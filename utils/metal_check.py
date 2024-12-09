import torch

def check_device():
    if torch.cuda.is_available():
        print(f"CUDA доступна! Готовьтесь к полету на ракете 🚀. GPU: {torch.cuda.get_device_name(0)}")
        return torch.device("cuda")
    elif torch.backends.mps.is_available():
        print("MPS доступна! Используем ваш Mac как турбо-блендер 🍏.")
        return torch.device("mps")
    else:
        print("Никаких GPU... Придется считать на калькуляторе 🤷‍♂️.")
        return torch.device("cpu")

