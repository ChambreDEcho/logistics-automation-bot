import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from platform_bot.config import URL, load_routes
from platform_bot.logger import log_event
from platform_bot.browser import click_js
from platform_bot.parser import extract_route
from platform_bot.alerts import show_alert


def monitor():
    origins, destinations = load_routes()

    log_event("ORIGINS: " + ", ".join(origins))
    log_event("DESTINATIONS: " + ", ".join(destinations))

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get(URL)

    input("Log in to the platform, then press ENTER...")

    while True:
        rows = driver.find_elements(By.CSS_SELECTOR, "tbody tr")

        for row in rows:
            try:
                origin, destination = extract_route(row)

                for o in origins:
                    for d in destinations:
                        if o in origin and d in destination:
                            log_event(f"MATCH FOUND: {origin} → {destination}")
                            show_alert(f"Route detected:\n{origin.upper()} → {destination.upper()}")
                            return

            except Exception as e:
                log_event(f"Error parsing row: {e}")

        time.sleep(5)