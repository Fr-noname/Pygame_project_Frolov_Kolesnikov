from data import lobby

if __name__ == "__main__":
    try:
        lobby.lobby()  # Начало игры
    except Exception as err:
        print(f"Ошибся, но в {err}?")
