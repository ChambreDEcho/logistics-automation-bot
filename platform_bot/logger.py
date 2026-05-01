import time
from pathlib import Path
from platform_bot.config import LOG_PATH


def log_event(message: str):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}\n"

    try:
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(line)
    except Exception:
        pass

    print(line, end="")