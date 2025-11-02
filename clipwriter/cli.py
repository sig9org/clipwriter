#!/usr/bin/env python3

import time

import click
import pyperclip

INTERVAL = 0.1
OUTPUT_FILE = "list.txt"


@click.command()
@click.argument("output", default=OUTPUT_FILE)
def cli(output) -> None:
    try:
        print(
            f"(Writes the contents copied to the clipboard to {output}.Press ESC to exit.)"
        )
        current = pyperclip.paste()
        while True:
            time.sleep(INTERVAL)
            text = pyperclip.paste()
            if text != current:
                with open(output, mode="a") as f:
                    print(text)
                    print(text, file=f)
                current = pyperclip.paste()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    cli()
