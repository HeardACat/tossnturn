# Toss 'n' Turn

A simple application that keeps a session alive by emulating a mouse.

Installation is via `pip` or `pipx`

```sh
brew install pipx
pipx install tossnturn
```

![screenshot](./screenshot.png)

To use:

```sh
tossnturn  # for a GUI
tossnturn cli  # if no gui interaction is needed
```

## Standalone Mode

`tossnturn` can be run standalone using

```sh
uv run scripts/tossnturn.py
```

This script is managed using `uv init --script` mode
