from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from clean import all_hadiths_df

vectorizer = TfidfVectorizer(max_features=10000000000)
X = vectorizer.fit_transform(all_hadiths_df["text_ar"])
y = all_hadiths_df["class_of_hadiths"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=49
)

# أهم خطوة
model = LogisticRegression(    class_weight={0:(( 22+10310)/(299+171))*8, 1:1},

    max_iter=100
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
# اختبار على أحاديث
test_hadiths = [   "من نام عن صلاة الفجر فهو في أمان الله",
    "من لم يزر جاره في كل أسبوع لن تُقبل له دعوته",
    "إذا شربت الماء على الريق يغفر لك الله ذنوبك",
    "من أحب التفاح أكثر من أي طعام آخر نال بركة في حياته",
    "من لبس الحذاء الأحمر في الجمعة يكتب له سبعون حسنة",
    "إذا قرأ الإنسان سورة قصيرة بعد الأكل يضاعف رزقه",
    "من جلس تحت شجرة في منتصف النهار يقيه من الغضب",
    
    
        "صوموا تصحوا",
    
    
         "لو يعلم العباد ما في رمضان لتمنت أمتي أن يكون رمضان السنة كلها…",
        
    
        "اللهم بارك لنا في رجب وشعبان وبلغنا رمضان"
    ,
      "من صلى علي صلاة واحدة صلى الله عليه عشراً",
    "من كذب علي متعمداً فليتبوأ مقعده من النار",
    "كل أمتي يدخلون الجنة إلا من أبى، من أطاعني دخل الجنة، ومن عصاني فقد أبى",
    "من رغب عن سنتي فليس مني",
    "لا يؤمن أحدكم حتى أكون أحب إليه من والده وولده والناس أجمعين",
    "أنا أغنى الشركاء عن الشرك من عمل عملاً أشرك فيه معي غيري تركته وشركه",
    "المؤمن القوي خير وأحب إلى الله من المؤمن الضعيف، وفي كل خير، احرص على ما ينفعك، واستعن بالله ولا تعجز، وإن أصابك شيء فلا تقل: لو أني فعلت كان كذا وكذا، ولكن قل: قدَر الله وما شاء فعل، فإن لو تفتح عمل الشيطان",
    "الإيمان بضع وستون شعبة، والحياء شعبة من الإيمان",
    "إن لله تسعة وتسعين اسما مائة إلا واحدا، من أحصاها دخل الجنة",
    "سبقت رحمتي غضبي",
    "إن الله يغار وغيرة الله أن يأتي المؤمنُ ما حرم عليه",
    "لا يؤمن أحدكم حتى يحب لأخيه ما يحب لنفسه",
    "خيركم من تعلم القرآن وعلمه",
    "إن الله يرفع بهذا الكتاب أقواما، ويضع به آخرين"


]



# تحويل للأرقام
X_test_hadiths = vectorizer.transform(test_hadiths)

# التوقع
y_test_preds = model.predict(X_test_hadiths)

# طباعة النتائج
for hadith, pred in zip(test_hadiths, y_test_preds):
    print("الحديث:", hadith)
    if pred==0:
        print("تصنيفه:ضعيف")
    else:
         print("تصنيفه:صحيح")

    
    print("---")
