# 💌 AI Spam Detector — Stylish Chat Input Version (Colab Ready)

!pip install -q nltk
import pandas as pd, string, nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from google.colab import files
from IPython.display import HTML, display
from datetime import datetime
nltk.download('stopwords', quiet=True)

# ------------------ Upload Dataset ------------------
display(HTML("<h2 style='text-align:center;color:#2c3e50;'>📂 Upload spam.csv dataset</h2>"))
uploaded = files.upload()

file_name = next(iter(uploaded))
data = pd.read_csv(file_name, encoding='latin-1')

if 'v1' in data.columns and 'v2' in data.columns:
    data = data.rename(columns={'v1':'label','v2':'message'})[['label','message']]
elif 'Category' in data.columns and 'Message' in data.columns:
    data = data.rename(columns={'Category':'label','Message':'message'})[['label','message']]
else:
    raise ValueError("Dataset must contain spam/ham labels and messages!")

# ------------------ Clean Data ------------------
stop_words = set(stopwords.words('english'))
def clean_text(t):
    t = t.lower()
    t = "".join(ch for ch in t if ch not in string.punctuation)
    return " ".join(w for w in t.split() if w not in stop_words)
data['cleaned'] = data['message'].astype(str).apply(clean_text)
data['label'] = data['label'].map({'spam':1,'ham':0})

# ------------------ Train Model ------------------
X = TfidfVectorizer(max_features=2000).fit_transform(data['cleaned'])
y = data['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# ------------------ Results ------------------
acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=["Ham","Spam"])

html = f"""
<center>
<div style='background:linear-gradient(135deg,#f8f9fa,#e8f6f3);padding:30px;width:80%;border-radius:20px;
            box-shadow:0 0 20px rgba(0,0,0,0.2);font-family:Poppins;'>
<h1 style='color:#1abc9c;'>🤖 SPAM DETECTION DASHBOARD</h1>
<p style='font-size:18px;'>Algorithm: <b>Logistic Regression</b> | Accuracy: <b style="color:#27ae60;">{acc*100:.2f}%</b></p>

<div style='display:flex;justify-content:center;gap:50px;margin-top:20px;'>
<div style='background:#fff;padding:20px;border-radius:15px;box-shadow:0 0 10px #ccc;'>
<h3 style='color:#2980b9;'>📊 Confusion Matrix</h3>
<table border='1' style='border-collapse:collapse;text-align:center;width:200px;'>
<tr style='background:#d6eaf8;'><th></th><th>Pred Ham</th><th>Pred Spam</th></tr>
<tr><td><b>Actual Ham</b></td><td>{cm[0][0]}</td><td>{cm[0][1]}</td></tr>
<tr><td><b>Actual Spam</b></td><td>{cm[1][0]}</td><td>{cm[1][1]}</td></tr>
</table>
</div>

<div style='background:#fff;padding:20px;border-radius:15px;box-shadow:0 0 10px #ccc;'>
<h3 style='color:#c0392b;'>📈 Classification Report</h3>
<pre style='text-align:left;font-size:13px;background:#f9f9f9;padding:10px;border-radius:10px;'>{report}</pre>
</div>
</div>
</div>
</center>
"""
display(HTML(html))

# ------------------ Multi-Message Stylish Prediction ------------------
vectorizer = TfidfVectorizer(max_features=2000)
vectorizer.fit(data['cleaned'])

display(HTML("""
<center>
<div style='background:linear-gradient(135deg,#e8daef,#f5eef8);padding:20px;width:70%;
border-radius:15px;box-shadow:0 0 10px rgba(0,0,0,0.2);font-family:Poppins;'>
<h2 style='color:#6c3483;'>💬 Interactive Message Tester</h2>
<p style='font-size:16px;color:#4a235a;'>Type your message below — type <b>'exit'</b> to end.</p>
</div>
</center>
"""))

while True:
    print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    msg = input("💌 Enter a message to analyze (or type 'exit' to quit): ")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    if msg.lower() == "exit":
        print("\n👋 Exiting Spam Detection System. Have a great day!")
        break

    cleaned = clean_text(msg)
    pred = model.predict(vectorizer.transform([cleaned]))[0]
    time = datetime.now().strftime("%I:%M %p")

    if pred == 1:
        gradient = "linear-gradient(135deg,#f1948a,#e74c3c)"
        status = "🚫 SPAM MESSAGE DETECTED!"
        desc = "⚠️ This message appears to be promotional or unwanted."
    else:
        gradient = "linear-gradient(135deg,#a9dfbf,#2ecc71)"
        status = "✅ NOT SPAM"
        desc = "💬 This message seems safe and normal."

    display(HTML(f"""
    <center>
    <div style='background:{gradient};color:white;padding:25px;width:70%;
                border-radius:20px;margin-top:20px;box-shadow:0 0 15px rgba(0,0,0,0.3);font-family:Poppins;'>
    <h2 style='color:white;'>{status}</h2>
    <p style='font-size:18px;'>{desc}</p>
    <p style='font-size:14px;color:#fdfefe;'>🕒 Analyzed at: {time}</p>
    </div>
    </center>
    """))
