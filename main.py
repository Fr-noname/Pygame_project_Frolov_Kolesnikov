import pygame
from data import lobby

if __name__ == "__main__":
    try:
        lobby.lobby()
    except Exception as err:
        print(f"Ошибся, но в {err}?")

