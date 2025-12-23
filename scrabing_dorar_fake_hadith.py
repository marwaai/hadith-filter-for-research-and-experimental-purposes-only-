import requests
from bs4 import BeautifulSoup
import time

all_hadiths = []

# حلقه لكل الصفحات
for i in range(1, 93):
    url = f"https://dorar.net/fake-hadith?page={i}"  # الرابط الحقيقي لكل صفحة
    print(f"جاري معالجة الصفحة {i} ...")
    
    response = requests.get(url)
    response.raise_for_status()  
    soup = BeautifulSoup(response.text, "html.parser")
    
    hadith_elements = soup.find_all("div", class_="card card-personal z-depth-4 animated fadeIn h-100 rounded")  
    for elem in hadith_elements:
        text = elem.get_text(separator="\n", strip=True)
        all_hadiths.append(text)

    
    time.sleep(1)  

with open("all_fake_hadiths.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(all_hadiths))

print(f"تم استخراج {len(all_hadiths)} حديث وحفظهم في all_hadiths.txt")