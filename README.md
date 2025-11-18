# sentiment-bot
A simple sentiment analysis app built with Python, Transformers, and Gradio.

# Sentiment Bot 🎭  
A simple and clean **Sentiment Analysis Web App** built using **Python, Hugging Face Transformers, and Gradio**.  
This app classifies text into **Positive** or **Negative** and shows confidence scores.

---

## 🚀 Live Demo  
Try the app here:  
👉 https://huggingface.co/spaces/javaria-ibrahim/sentiment-bot  

---

## 🧠 Model  
This app uses the Hugging Face `pipeline("sentiment-analysis")`  
which loads the model:

- **distilbert-base-uncased-finetuned-sst-2-english**

It's lightweight, fast, and perfect for sentiment tasks.

---

## 🎨 Features  
- Real-time sentiment prediction  
- Clean Gradio interface  
- Shows confidence score (%)  
- Fully deployed on Hugging Face  
- Beginner-friendly code structure  

---

## 🖥️ Tech Stack  
- **Python**  
- **Transformers (Hugging Face)**  
- **Gradio**  
- **Torch**

---

## 📂 Project Structure  

```
sentiment-bot/
│
├── app.py               # Main application code
├── requirements.txt     # Dependencies
└── README.md            # Project explanation
```

---

## ▶️ Run Locally  

1️⃣ Clone the repo  
```
git clone https://github.com/javariaibrahim11/sentiment-bot
```

2️⃣ Install dependencies  
```
pip install -r requirements.txt
```

3️⃣ Run the app  
```
python app.py
```

Gradio will open in your browser 🚀  

---

## ✨ How It Works  
1. User enters text  
2. Model receives input  
3. Hugging Face pipeline predicts sentiment  
4. Confidence score + label displayed in UI  

---

## 🛠️ Code Snippet (Main Function)  

```python
def analyze_sentiment(text):
    result = sentiment_model(text)[0]
    sentiment = result["label"]
    score = round(result["score"] * 100, 2)
    return f"Sentiment: {sentiment}\nConfidence: {score}%"
```

---

## 📌 Future Improvements  
- Add Neutral class  
- Add multiple models  
- UI styling  
- Store history of inputs  
- Add emojis for output  
- Deploy via GitHub → Hugging Face auto sync  

---

## 👩‍💻 Author  
**Javaria Ibrahim**  

- GitHub: https://github.com/javariaibrahim11  
- Hugging Face: https://huggingface.co/javaria-ibrahim  

---

## 📜 License  
This project is licensed under the **MIT License**.



