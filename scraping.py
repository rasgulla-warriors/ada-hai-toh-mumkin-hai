import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup
import csv


async def main():
    # Step 1: Launch the browser
    browser = await launch(headless=True)
    page = await browser.newPage()

    # Step 2: Load the webpage
    url = "https://www.indiavotes.com/lok-sabha/2019/all-states/17/0"
    await page.goto(url)

    # Wait for the page to load completely
    await page.waitForSelector("table")

    # Step 3: Get the page content
    content = await page.content()
    await browser.close()

    # Step 4: Parse the HTML content
    soup = BeautifulSoup(content, "html.parser")

    # Step 5: Locate the tables in the HTML
    tables = soup.find_all("table")

    # Step 6: Extract the table data and save to CSV
    for index, table in enumerate(tables):
        data = []
        headers = [header.text for header in table.find_all("th")]
        rows = table.find_all("tr")

        for row in rows:
            cols = row.find_all("td")
            cols = [col.text.strip() for col in cols]
            data.append(cols)

        # Save to CSV
        with open(f"table_{index + 1}.csv", "w", newline="") as file:
            writer = csv.writer(file)
            if headers:
                writer.writerow(headers)
            writer.writerows(data)
        print(f"Table {index + 1} saved to table_{index + 1}.csv")


# Run the main function
asyncio.get_event_loop().run_until_complete(main())
