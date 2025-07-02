import openai
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import csv

openai.api_key = ""


options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get('https://www.openu.ac.il/allnews/pages/default.aspx')
time.sleep(5)

# 🔁 גלילה כדי לטעון את כל הכתבות
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    new_height = driver.execute_script("return document.body.scrollHeight")
    print("Loading pages...")
    if new_height == last_height:
        break
    last_height = new_height

# פתיחת CSV
with open('openu_full_articles.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['institution','Date','Title','URL','tone','mentions_cooperation','mentions_competition','cooperation_type','thematic_tags','justification','length_words'])

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    articles = soup.select('article.homepage-news')
    print(f"🔍 Found {len(articles)} articles")

    # שליפת כתבות
    articles_data = []
    for article in articles:
        try:
            a_tag = article.select_one('a')
            if not a_tag or not a_tag.get('href'):
                continue

            href = a_tag['href'].strip()
            full_url = href if href.startswith('http') else f"https://www.openu.ac.il{href}"
            title = a_tag.get('title', '').strip()
            articles_data.append((title, full_url))
        except Exception as e:
            print(f"⚠️ Failed to parse preview: {e}")

    # שליפת תוכן מתוך כל כתבה
    ArtNum=0
    for i, (title, full_url) in enumerate(articles_data, start=1):
        try:

            driver.get(full_url)
            time.sleep(7)
            inner_soup = BeautifulSoup(driver.page_source, 'html.parser')

            paragraphs = []

            # ✅ שליפה מכל div.rc-rte (כולל p, div, ul, li, a)
            rte_blocks = inner_soup.select('div.rc-rte')
            for block in rte_blocks:
                elements = block.find_all(['p', 'div', 'ul', 'li', 'a', 'h1', 'h2'])
                for el in elements:
                    text = el.get_text(strip=True)
                    if text and text not in paragraphs:
                        paragraphs.append(text)

            # בניית תוכן מלא
            content = '\n'.join(paragraphs)
            article_length = len(content.split())

            if content:
                try:
                    system_prompt = (
                        """
                        אתה עומד לקבל את התוכן המלא של כתבת חדשות אקדמית בעברית.

                        עליך לנתח את הכתבה ולהחזיר שורת מידע אחת בלבד בפורמט CSV עם 8 עמודות, לפי הסדר הבא:
                        institution,title,tone,mentions_cooperation,mentions_competition,cooperation_type,thematic_tags,justification

                        ⚠️ הנחיות פורמט:
                        - ערכים באנגלית בלבד.
                        - שדות מופרדים בפסיקים, בלי מרכאות, גרשיים או תווים מיוחדים.
                        - בין תגיות thematic_tags השתמש בנקודה-פסיק (`;`) בלבד.
                        - בשדה `justification` תן משפט קצר שמסביר מדוע בחרת בטון.

                        --------------------------------------------------

                         טון שיתופי (cooperative):
                        כאשר הכתבה מדגישה שיתופי פעולה, מאמצים משותפים, מטרות קולקטיביות, או שפה מאחדת.

                        סימנים:
                        - ביטויים כמו: "בשיתוף פעולה", "ביחד עם", "חברה ל-", "יוזמה משותפת".
                        - אזכור של שותפויות עם מוסדות אקדמיים אחרים.

                        דוגמה:
                        "אוניברסיטת בן-גוריון חברה לאוניברסיטת תל אביב למחקר בתחום בריאות הנפש."  
                        → tone: cooperative  
                        → justification: The article highlights a partnership with another university for joint research.

                        טון תחרותי (competitive):
                        כאשר הכתבה מדגישה פרסים, דירוגים, ייחודיות, חדשנות או הישגים יוצאי דופן.

                        סימנים:
                        - ביטויים כמו: "הראשונה בישראל", "מובילה עולמית", "תוכנית ייחודית", "זכתה בפרס יוקרתי".
                        - שפה שמדגישה יוקרה, חדשנות או מצוינות.
                        - השוואה גלויה או סמויה לאחרים.

                        דוגמה:
                        "הפקולטה קיבלה את הדירוג הגבוה ביותר בישראל במדעי המחשב לשנת 2024."  
                        → tone: competitive  
                        → justification: The article emphasizes the university's top ranking in a national evaluation.

                        בחר בטון mixed אם מופיעים גם תחרותי וגם שיתופי:
                        כאשר מופיעים סימנים גם לתחרותי וגם לשיתופי – אך אף אחד מהם לא דומיננטי בבירור.
                        - "The article includes both partnership and ranking claims, but neither dominates clearly."

                        בחר בטון neutral כאשר:
                        - אין טון תחרותי ואין טון שיתופי כלל (הכתבה אינפורמטיבית בלבד).
                        בשדה `justification` כתוב הסבר קצר מה הוביל להחלטה — למשל:
                        - "No signs of competition or collaboration were found."



                        --------------------------------------------------
                        דוגמה:
                        "Ben-Gurion University,Updates from the rector,neutral,no,no,none,governance;announcements,No signs of competition or collaboration were found."

                        --------------------------------------------------

                        📋 הסבר שדות:
                        1. institution – שם האוניברסיטה באנגלית (למשל: Reichman University)
                        2. title – כותרת הכתבה
                        3. tone – cooperative / competitive / neutral / mixed
                        4. mentions_cooperation – yes / no
                        5. mentions_competition – yes / no
                        6. cooperation_type – inter-university / industry / international / none
                        7. thematic_tags – נושאים מרכזיים מופרדים ב־`;`
                        8. justification – משפט אחד בלבד שמסביר את בחירת הטון

                        ❌ אל תחזיר את תוכן הכתבה המלא.
                        ❌ אל תחזיר טקסט הסבר מחוץ לשורת ה-CSV.

                        אם לא הצלחת לנתח או אין לך תשובה להחזיר או אין 7 משתנים בשורה – החזר את השורה:
                        ERR,ERR,ERR,ERR,ERR,ERR,ERR,ERR
                        """

                    )

                    messages = [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": content}
                    ]
                    response = openai.ChatCompletion.create(
                        model="gpt-4o",
                        messages=messages
                    )

                    content = response['choices'][0]['message']['content'].strip()
                except Exception as e:
                    content = f"[GPT ERROR: {str(e)}]"

            else:
                content = ''
            results = content.split(',')
            # הדפסה ובסיס נתונים
            print(f"✔️ {content}")
            safe_results = [results[i] if i < len(results) else 'ERR' for i in range(8)]
            writer.writerow(
                ['BGU', 'No DATE', title, full_url, safe_results[2], safe_results[3], safe_results[4], safe_results[5],
                 safe_results[6], safe_results[7], article_length])
            ArtNum += 1
            print(f"✔️ {title}-{ArtNum}")
        except Exception as err:
            print(f"❌ Error: {err}")

driver.quit()
print("✅ Done! All OpenU articles saved.")
