import random


def choose_word(words: list) -> str:
    """Vybere náhodné slovo ze seznamu."""
    return random.choice(words)


def get_user_char(used_chars: list):
    """Získá a ověří vstup od uživatele."""
    while True:
        char = input("Zadej písmeno: ").strip().lower()

        if len(char) != 1:
            print("Zadej právě jedno písmeno!")
            continue

        if not char.isalpha():
            print("Zadej pouze písmeno!")
            continue

        if char in used_chars:
            print("Toto písmeno už jsi zkusil!")
            continue

        used_chars.append(char)
        return char, used_chars


def replace_chars(current_state: str, secret_word: str, char: str) -> str:
    """Nahradí _ správně uhodnutými písmeny."""
    new_state = list(current_state)

    for i in range(len(secret_word)):
        if secret_word[i] == char:
            new_state[i] = char

    return "".join(new_state)