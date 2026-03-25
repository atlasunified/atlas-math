from __future__ import annotations

SIZE_PRESETS = {
    "small": 100,
    "medium": 1000,
    "large": 5000,
    "full": 20000,
}

DEFAULT_LEVELS = ["level_1", "level_2", "level_3", "level_4", "level_5"]

DEFAULT_DIFFICULTY_MIXES = {
    "balanced": {
        "level_1": 0.20,
        "level_2": 0.20,
        "level_3": 0.20,
        "level_4": 0.20,
        "level_5": 0.20,
    },
    "curriculum": {
        "level_1": 0.35,
        "level_2": 0.25,
        "level_3": 0.20,
        "level_4": 0.12,
        "level_5": 0.08,
    },
    "advanced": {
        "level_1": 0.08,
        "level_2": 0.12,
        "level_3": 0.20,
        "level_4": 0.25,
        "level_5": 0.35,
    },
    "middle_heavy": {
        "level_1": 0.10,
        "level_2": 0.20,
        "level_3": 0.40,
        "level_4": 0.20,
        "level_5": 0.10,
    },
}

DEFAULT_MAX_BATCH_SIZE = 64
DEFAULT_MIN_YIELD_RATIO = 0.10
DEFAULT_EXHAUSTION_PATIENCE = 3
DEFAULT_TARGET_TOLERANCE = 0.05
DEFAULT_MAX_ROUNDS = 4
DEFAULT_MIN_UNIQUE_RATE = 0.01
DEFAULT_RETRY_OVERSHOOT = 1.10
DEFAULT_GENERATION_MODE = "auto"

ANSI = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "dim": "\033[2m",
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bright_black": "\033[90m",
    "bright_red": "\033[91m",
    "bright_green": "\033[92m",
    "bright_yellow": "\033[93m",
    "bright_blue": "\033[94m",
    "bright_magenta": "\033[95m",
    "bright_cyan": "\033[96m",
    "bright_white": "\033[97m",
    "bg_black": "\033[40m",
    "bg_red": "\033[41m",
    "bg_green": "\033[42m",
    "bg_yellow": "\033[43m",
    "bg_blue": "\033[44m",
    "bg_magenta": "\033[45m",
    "bg_cyan": "\033[46m",
    "bg_white": "\033[47m",
    "home": "\033[H",
    "clear": "\033[2J",
    "hide_cursor": "\033[?25l",
    "show_cursor": "\033[?25h",
}

LEVEL_COLORS = {
    "level_1": ANSI["bright_green"],
    "level_2": ANSI["bright_cyan"],
    "level_3": ANSI["bright_yellow"],
    "level_4": ANSI["bright_magenta"],
    "level_5": ANSI["bright_red"],
}
