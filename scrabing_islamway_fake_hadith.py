import requests
from bs4 import BeautifulSoup
import time

all_hadiths = []

# حلقه لكل الصفحات
url = f"https://ar.islamway.net/article/399/%D9%85%D8%A6%D8%A9-%D8%AD%D8%AF%D9%8A%D8%AB-%D8%B6%D8%B9%D9%8A%D9%81%D8%A9-%D9%88-%D9%85%D9%88%D8%B6%D9%88%D8%B9%D8%A9-%D9%85%D9%86%D8%AA%D8%B4%D8%B1%D8%A9-%D8%A8%D9%8A%D9%86-%D8%A7%D9%84%D8%AE%D8%B7%D8%A8%D8%A7%D8%A1-%D9%88%D8%A7%D9%84%D9%88%D8%B9%D8%A7%D8%B8"  # الرابط الحقيقي لكل صفحة
print(f"جاري معالجة الصفحة ..")
    
response = requests.get(url)
response.raise_for_status()  
soup = BeautifulSoup(response.text, "html.parser")
    
hadith_elements = soup.find_all("div", class_="main-wrapper")  
for elem in hadith_elements:
        text = elem.get_text(separator="\n", strip=True)
        all_hadiths.append(text)

    
        time.sleep(1)  

with open("all_hadiths.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(all_hadiths))

print(f"تم استخراج {len(all_hadiths)} حديث وحفظهم في all_hadiths.txt")