import re
import pandas as pd

df = pd.read_csv("all_hadiths_clean.csv", encoding="utf-8-sig")
ftwa_df=pd.read_csv("88kData.csv", encoding="utf-8-sig")
print(ftwa_df.columns)
invisible_chars = ''.join([
    '\u200c', '\u200d', '\u200e', '\u200f',
    '\ufeff', '\u202a', '\u202b', '\u202c', '\u202d', '\u202e'
])

pattern_invisible = f'[\\x00-\\x1F\\x7F{invisible_chars}]'

old_hadiths = [
    re.sub(pattern_invisible, '', str(i))
    for i in df["text_ar"]
]
old_hadithss=[]
old_hadithss = [i.split('"')[1] if len(i.split('"')) > 1 else i for i in old_hadiths]

# قراءة الجديد
with open("all_fake_hadiths.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
i = 0
while i < len(lines):
    if "الدرجة:" in lines[i].strip():
        i += 3
    else:
        new_lines.append(lines[i])
        i += 1
print(len(new_lines))

cleaned = "|".join(new_lines)
cleaned = re.sub(r'[0-9٠-٩]+', '', cleaned)
cleaned = re.sub(r'"[^"]*"', '', cleaned)
cleaned = re.sub(r'[\(\)]', '', cleaned)
cleaned = re.sub(r'[،\-‹›»]', '', cleaned)
cleaned = cleaned.replace("وحديث:", "").replace("حديث:", "")
cleaned = re.sub(pattern_invisible, '', cleaned)
new_hadiths=[]
for line in cleaned.split("|") :
  if line.strip()!="":
   new_hadiths .append(line)
print(old_hadithss[0:2])

# دمجهم داخل DataFrame
all_hadiths_df = pd.DataFrame({
   
    "text_ar": old_hadithss [0:len(old_hadithss)]+ new_hadiths,
    "class_of_hadiths":  [1] * len(old_hadithss)+ [0] * len(new_hadiths),
})

print(all_hadiths_df["class_of_hadiths"].iloc[-12])
print(all_hadiths_df["text_ar"].iloc[-12])
