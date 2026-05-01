from selenium.webdriver.common.by import By


def extract_route(row):
    cell = row.find_element(By.CSS_SELECTOR, "td.cdk-column-deliveryInformation")
    text = cell.text.strip()

    lines = [l.strip() for l in text.splitlines() if l.strip()]

    if len(lines) >= 3:
        return lines[0].lower(), lines[2].lower()

    if len(lines) >= 2:
        return lines[0].lower(), lines[1].lower()

    raise Exception("Unable to parse route information")