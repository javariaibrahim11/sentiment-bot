# -*- coding: utf-8 -*-
"""sentiment-bot





from transformers import pipeline
import gradio as gr

# Load model
sentiment_model = pipeline("sentiment-analysis")

# Function
def analyze_sentiment(text):
    result = sentiment_model(text)[0]
    sentiment = result["label"]
    score = round(result["score"] * 100, 2)
    return f"Sentiment: {sentiment}\nConfidence: {score}%"

# Gradio UI
chat_interface = gr.Interface(
    fn=analyze_sentiment,
    inputs="text",
    outputs="text",
    title="Sentiment Classifier 😊😡",
    description="Write something & I’ll tell you whether it's Positive/Negative 😊😡"
)

# Run app
chat_interface.launch()
