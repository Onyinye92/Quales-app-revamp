import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

#variable declaration
wait = 3
url = "https://quales.vercel.app/"

#browser initials
driver = webdriver.Chrome()
driver.get("https://quales.vercel.app/")
driver.maximize_window()

#explore talent button functionality
driver.find_element(By.CSS_SELECTOR, "section.relative.flex-col > article a.btn.glass.rounded-full").click()
time.sleep(3)

# Locate and click the QA Engineer button
qa_engineer_button = driver.find_element(By.CSS_SELECTOR,
    "section.bg-white.px-5.xl\\:px-28.mt-20 > div.grid.grid-cols-1.md\\:grid-cols-4 > a.flex.flex-col.items-center.md\\:border-r.md\\:border-gray-400.px-3.sm\\:px-8.pb-8.cursor-pointer > h4")
qa_engineer_button.click()
time.sleep(3)

# Locate and click the Abati Adeotan Senayon element
abati_adeotan = driver.find_element(By.CSS_SELECTOR,
    "section.flex.flex-col.bg-white.px-5.xl\\:px-28.mt-10 > div.grid.grid-cols-2.lg\\:grid-cols-3.gap-10 > a:nth-child(1) > div > article > h3")
abati_adeotan.click()
time.sleep(3)

# Find the introduction paragraph
qa_intro = driver.find_element(By.CSS_SELECTOR, "section.bg-white .lg\\:flex-row article.text-primary > p")
time.sleep(3)

# Find and click the Use Cases button
use_cases_button = driver.find_element(By.CSS_SELECTOR, "nav .navbar-end ul > li:nth-child(2) > a")
use_cases_button.click()
time.sleep(3)

# Find the Real-World Success Stories with Quales paragraph
success_stories_paragraph = driver.find_element(By.CSS_SELECTOR, "section.bg-white.px-5.lg\\:px-28.py-10.flex.flex-col.md\\:flex-row.items-center")
time.sleep(3)

# Find the "Thought Leadership" button and click it
thought_leadership_button = driver.find_element(By.CSS_SELECTOR, "body > main > nav > div.navbar-end.w-auto.ml-auto > ul > li:nth-child(3) > a")
thought_leadership_button.click()
time.sleep(3)

# Locate the header with paragraph
career_insights_paragraph = driver.find_element(By.CSS_SELECTOR, "body > main > section.bg-white.px-5.xl\\:px-28 > header")
time.sleep(3)

# Scroll down a bit using the PAGE_DOWN key
driver.find_element(By.TAG_NAME, "html").send_keys(Keys.PAGE_DOWN)
# Wait to observe the scrolling effect
time.sleep(3)

# Find "Our Recent Blogs" header
recent_blogs_header = driver.find_element(By.CSS_SELECTOR, "body > main > section.bg-white.px-5.xl\\:px-28 > section > h4")
time.sleep(3)

# Scroll back up using the PAGE_UP key
driver.find_element(By.TAG_NAME, "html").send_keys(Keys.PAGE_UP)
time.sleep(3)

# Locate the About Us button and click it
about_us_button = driver.find_element(By.CSS_SELECTOR, "body > main > nav > div.navbar-end.w-auto.ml-auto > ul > li:nth-child(4) > a")
about_us_button.click()
time.sleep(3)


