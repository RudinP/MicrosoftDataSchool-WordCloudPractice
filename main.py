from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from kiwipiepy import Kiwi
from collections import Counter
from wordcloud import WordCloud
import re
import matplotlib.pyplot as plt

NOUN_TAG = '^N+'
STOPWORDS = {'이', '것', '수', '등'}
font_path = 'C:/Windows/Fonts/malgun.ttf'

def dataScrap():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.techdaily.co.kr/")

    section = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
            "#cus-idx-default > div:nth-child(3) > div.index-columns.grid-5.width-full > div > article:nth-child(3) > section"))
    )

    links_elements = section.find_elements(By.TAG_NAME, "a")
    links = list({a.get_attribute("href") for a in links_elements})

    articles = []
    for link in links:
        driver.get(link)
        
        article = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, "article-view-content-div"))
        )
        
        articles.append(article.text)

    driver.quit()
    return articles


def make_tokens(data):
    kiwi = Kiwi()
    results = []

    for item in data:
        forms = [
            t.form
            for t in kiwi.tokenize(item)
            if re.match(NOUN_TAG, t.tag)
            and t.form not in STOPWORDS
        ]
        results.extend(forms)
    
    return results

def make_Wordcloud(words):
    counter = Counter(words)

    wc = WordCloud(
        font_path=font_path,
        background_color='white',
        width=800,
        height=400
    )

    wc.generate_from_frequencies(counter)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

data = dataScrap() 
words = make_tokens(data)
make_Wordcloud(words)   