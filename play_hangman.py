from hangman_logic import choose_word, get_user_char, replace_chars
from hangman_display import (
    load_pics,
    show_welcome_message,
    show_game_state,
    show_feedback,
    show_game_over,
)


def main():
    show_welcome_message()

    pics = load_pics()

    words = ["python", "programovani", "hangman", "parametr", "funkce"]
    secret_word = choose_word(words)

    state = "_" * len(secret_word)
    wrong = 0
    used = []

    while "_" in state and wrong < len(pics) - 1:
        show_game_state(state, pics, wrong, used)

        char, used = get_user_char(used)

        if char in secret_word:
            show_feedback(True)
            state = replace_chars(state, secret_word, char)
        else:
            show_feedback(False)
            wrong += 1

    win = "_" not in state
    show_game_over(win, secret_word)


if __name__ == "__main__":
    main()