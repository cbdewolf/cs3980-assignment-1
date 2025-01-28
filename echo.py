# echo.py


def echo(text: str, repitions: int = 3) -> str:
    length = len(text)
    return (
        text[length - repitions : length]
        + "\n"
        + text[length - repitions + 1 : length]
        + "\n"
        + text[length - repitions + 2 : length]
        + "\n"
        + "."
    )


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
