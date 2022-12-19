"""В1. Використовуючи Scrapy, заходите на "https://chrome.google.com/webstore/sitemap", переходите
на кожен лінк з тегів <loc>, з кожного лінка берете посилання на сторінки екстеншинів, парсите їх
і зберігаєте в CSV файл ID, назву та короткий опис кожного екстеншена (пошукайте уважно де його
можна взяти). Наприклад:
“aapbdbdomjkkjkaonfhkkikfgjllcleb”, “Google Translate”,
“View translations easily as you browse the web. By the Google Translate team.”"""

import subprocess

if __name__ == "__main__":
    subprocess.run(["scrapy", "crawl", "google_spider", "-O", "all_inform.csv"])