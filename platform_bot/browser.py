import time
from selenium.webdriver.support.ui import WebDriverWait
from platform_bot.logger import log_event


def click_js(driver, selector, name="element", timeout=20):
    try:
        wait = WebDriverWait(driver, timeout)

        wait.until(lambda d: d.execute_script(
            "return document.querySelector(arguments[0]) !== null;", selector
        ))

        result = driver.execute_script("""
            const el = document.querySelector(arguments[0]);
            if (!el) return "NOT_FOUND";

            try {
                el.click();
                return "CLICK_OK";
            } catch (e1) {
                try {
                    el.dispatchEvent(new MouseEvent('click', {
                        bubbles: true,
                        cancelable: true
                    }));
                    return "DISPATCH_OK";
                } catch (e2) {
                    return "ERROR:" + e2.message;
                }
            }
        """, selector)

        if result in ("CLICK_OK", "DISPATCH_OK"):
            log_event(f"Click executed on {name} [{result}]")
            return True

        raise Exception(result)

    except Exception as e:
        log_event(f"Failed clicking {name}: {e}")
        return False