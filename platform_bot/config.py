from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

URL = "INSERTURL"

CONFIG_PATH = BASE_DIR / "config.txt"
ALERT_SOUND = BASE_DIR / "platform_alert.wav"
LOG_PATH = BASE_DIR / "platform_log.txt"

#Obtain the JS PATHS in the website you want to monitor
LOADS_JS_PATHS = [
    "body > app-root > div > div.header.ng-star-inserted > ls-navigation > div > div > navigation-menu-items.navigation-menu.ng-star-inserted > div > a:nth-child(1)",
    "body > app-root > div > div.header.ng-star-inserted > ls-navigation > div > div > navigation-menu-items.navigation-menu.ng-star-inserted > div > a.navigation-menu--item.ng-star-inserted.navigation-menu--item--active"
]

REFRESH_BUTTON = (
    "body > app-root > div > div.body > lm-load-list-root > mat-sidenav-container > "
    "mat-sidenav-content > div:nth-child(1) > loads-filter-header > div.button-group-container > "
    "button.button-large-icon.secondary.refresh-button"
)


def load_routes():
    origins, destinations = [], []
    current_section = None
    #This function allows to set the criteria you want to monitor

    with open(CONFIG_PATH, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            if line.startswith("#"):
                header = line.replace("#", "").strip().lower()
                if "origin" in header:
                    current_section = "origin"
                elif "destination" in header:
                    current_section = "destination"
                else:
                    current_section = None
                continue

            if "|" in line:
                continue

            if current_section == "origin":
                origins.append(line.lower())
            elif current_section == "destination":
                destinations.append(line.lower())

    return origins, destinations