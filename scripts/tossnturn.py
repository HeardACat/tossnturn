# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "pynput",
# ]
# ///

from pynput.mouse import Controller
import time


def main() -> None:
    eps = 1
    timeout = 280
    mouse = Controller()
    while True:
        mouse.move(eps, 0)
        mouse.move(-eps, 0)
        time.sleep(timeout)


if __name__ == "__main__":
    main()
