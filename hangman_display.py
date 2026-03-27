import json


def load_pics(filename: str = "hangman.json") -> list:
    """Načte obrázky šibenice ze souboru."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def show_welcome_message():
    print("Vítej ve hře šibenice!")
    print("Zadávej písmena a pokus se uhodnout tajné slovo. "
          "Ale pozor, ať neskončíš na šibenici!")


def show_game_state(state: str, pics: list, wrong: int, used: list):
    print(pics[wrong])
    print(f"Slovo: {state}")
    print(f"Použitá písmena: {', '.join(used)}")


def show_feedback(is_correct: bool):
    if is_correct:
        print("Správně! 👍")
    else:
        print("Špatně! ❌")


def show_game_over(win: bool, secret_word: str):
    if win:
        print(f"Gratuluji! Uhodl jsi slovo: {secret_word}")
    else:
        print(f"Konec hry! Tajné slovo bylo: {secret_word}")