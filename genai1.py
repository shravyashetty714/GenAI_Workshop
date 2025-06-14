# -*- coding: utf-8 -*-
"""Genai1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hkwX02NZ_vjtaYV5sOWS2iDhJbKqeDk5
"""

# 1.1. Text Generation:
from transformers import pipeline

# Load a text-generation pipeline with GPT-2
generator = pipeline("text-generation", model="gpt2")

# Generate text based on a prompt
prompt = "Once upon a time in the future,"
output = generator(prompt, max_length=20, num_return_sequences=1)

# Print generated text
print(output[0]["generated_text"])

#1.2
from transformers import pipeline

# Load a text-generation pipeline with GPT-2
generator = pipeline("text-generation", model="gpt2")

# Generate text based on a prompt
prompt = "Once upon a time in the future,"
output = generator(prompt, max_length=50, num_return_sequences=1)  #num_return_sequence-->number of output

# Print generated text
print(output[0]["generated_text"])

# 1.3.
from transformers import pipeline

# Load a text-generation pipeline with GPT-2
generator = pipeline("text-generation", model="gpt2")

# Generate text based on a prompt
prompt = "There was a dog near "
output = generator(prompt, max_length=50, num_return_sequences=1)

# Print generated text
print(output[0]["generated_text"])

# 2. Tokenization:
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")
text = "Hello, how are you?"
tokens = tokenizer.tokenize(text)
print(tokens)

tokensid = tokenizer(text)
print(tokensid)
#special char are considered as tokens
#G means space
#attention mask: word is represented with 1 or more zero after tokenization.

# 3. Text Summarization:

from transformers import pipeline

summarizer = pipeline("summarization")
text = "Generative AI is transforming the world by enabling machines to create human-like text. This has applications in chatbots, translation, and content generation."
summary = summarizer(text, max_length=16, min_length=10, do_sample=False)
print(summary[0]["summary_text"])

# 4.1 Sentimental analysis
from transformers import pipeline
sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
print(sentiment_analyzer("I love Hugging Face!,"))

# 4.2 Sentimental analysis
from transformers import pipeline
sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
print(sentiment_analyzer("I hate Hugging Face!,"))

# 5. Question and Answering
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
context = "Hugging Face was founded in 2016 and is known for its open-source NLP models."
question = "When was Hugging Face founded?"
print(qa_pipeline(question=question, context=context))
print(summary[0]["summary_text"])

# 6.1 Text classifier
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
text = "I want to book a flight to Paris next week."
labels = ["travel", "sports", "finance"]
print(classifier(text, candidate_labels=labels))

# 6.2.
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
text = "I want to go for shoping"
labels = ["travel", "man", "finance"]
print(classifier(text, candidate_labels=labels))

# 7. Text Translation:

from transformers import MarianMTModel, MarianTokenizer

# Define source and target languages
src_lang = "en"
tgt_lang = "it"

# Load model and tokenizer
model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Input text to translate
text = "Hello, how are you?"

# Tokenize and translate
tokens = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
translation = model.generate(**tokens)
translated_text = tokenizer.decode(translation[0], skip_special_tokens=True)

print(f"Translated text: {translated_text}")

# 8.1 Code Generator using GenAI Model:

from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2")
model = AutoModelForCausalLM.from_pretrained("microsoft/phi-2")

prompt = "Write a Python function to check if a number is prime."
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=100)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))

# 8.2
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print(is_prime(7)) # True
print(is_prime(10)) # False

# 8.3 Code Generator using GenAI Model:

from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2")
model = AutoModelForCausalLM.from_pretrained("microsoft/phi-2")

prompt = "Write a Python function to check if a number is odd"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=100)0
print(tokenizer.decode(outputs[0], skip_special_tokens=True))

# 9. Name - Entity Extraction:

from transformers import pipeline

ner = pipeline("ner", grouped_entities=True)
text = "Elon Musk founded SpaceX and Tesla in the United States."
print(ner(text))

# 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

# Release Date:

from datetime import datetime

for model in response.data:
    created_ts = model.created
    if created_ts:
        created_date = datetime.fromtimestamp(created_ts)
        if created_date.year >= 2023:
            print(f"{model.id} → Created on {created_date}")



#

# ✅ Extract only the model IDs
model_ids = [model.id for model in response.data]

# ✅ Print model IDs
for mccodel_id in model_ids:
    print(model_id)
print(completion.choices[0].message)

# 10.!pip install transformers

from transformers import pipeline

nlp = pipeline("ner", grouped_entities=True)

text = "Apple Inc. was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in Cupertino, California."
entities = nlp(text)
for entity in entities:

    print(entity)

# 11. Image Generation:

!pip install diffusers transformers accelerate
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
pipe = pipe.to("cpu")  # Use CPU if no GPU

prompt = "a futuristic city at night, neon lights, cyberpunk"
image = pipe(prompt).images[0]
image.show()

from IPython.display import display
display(image)

# 11. Image Generation:

!pip install diffusers transformers accelerate
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
pipe = pipe.to("cuda")  # Use CPU if no GPU

prompt = "a futuristic city at night, neon lights, cyberpunk"
image = pipe(prompt).images[0]
image.show()
print("Harish Kunder")

from IPython.display import display

display(image)

# 11. Image Generation:

!pip install diffusers transformers accelerate
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
pipe = pipe.to("cuda")  # Use CPU if no GPU

prompt = "funny white cat wallpaper hiding inside thw cover of brown color lying on the floor "
image = pipe(prompt).images[0]
image.show()
print("Harish Kunder")

from IPython.display import display

display(image)

# 11. Image Generation:

!pip install diffusers transformers accelerate
from diffusers import StableDiffusionPipeline

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
pipe = pipe.to("cuda")  # Use CPU if no GPU

prompt = "funny white cat wallpaper hiding inside thw cover of brown color lying on the floor cover its body with a mat and only face is visible"
image = pipe(prompt).images[0]
image.show()
print("Harish Kunder")

from IPython.display import display

display(image)

# UI Creation:
# C

# https://www.gradio.app/https://www.gradio.app/
# /https://www.gradio.app/

!pip install gradio
import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch()

#Streamlit
!pip install streamlit
import streamlit as st

st.title("Welcome App")

name = st.text_input("Enter your name:")

if name:
    st.write(f"Your name is {name}. Welcome!")
!streamlit run app.py &>/dev/null &

#ngrok

!pip install pyngrok
from pyngrok import ngrok

# Kill any existing tunnel
ngrok.kill()

#Replace with your token
!ngrok config add-authtoken 2wZbeoOt25PV8OjmQLxDmWVV58I_5zc8ipzZ9r3YewvnBD5tU

# Set up a tunnel to the streamlit port 8501
public_url = ngrok.connect(addr="8501", proto="http")

print(f"🚀 Your Streamlit app is live at: {public_url}")

# Start the app
!streamlit run app.py &>/dev/null &

#Generating the code with Gradio UI:

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import gradio as gr

# Load the better model (codegen-2B-mono)
model_name = "Salesforce/codegen-2B-mono"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name).to("cuda")

def generate_code(prompt):
    # Add code-specific prompt context
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to("cuda")
    # Generate code output
    output = model.generate(input_ids, max_length=256, temperature=0.5, do_sample=True, top_p=0.95)
    # Decode output tokens to string
    generated_code = tokenizfffer.decode(output[0], skip_special_tokens=True)
    return generated_code

# Gradio Interface
gr.Interface(
    fn=generate_code,
    inputs=gr.Textbox(lines=2, placeholder="Ask for code e.g. 'Python code to check if a number is prime'"),
    outputs=gr.Code(language="python"),
    title="🧑‍💻 GenAI Code Generator",
    description="Enter a coding problem description and get generated Python code using a GenAI model."
).launch()

# Email Writer:


import requests

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYTc2NDI5ZDMtZjlhOS00ZDIwLWFjYWUtMTFmNWMzZTU1NGI4IiwidHlwZSI6ImFwaV90b2tlbiJ9.bL2bJor-1d_5xOyuoSAxpYhOkYHwWV1M8chtqhlkOtQ",
    "Content-Type": "application/json"
}

url = "https://api.edenai.run/v2/workflow/a2de4dac-040f-40a7-98e6-161d75959a10/execution/"

payload = {
    "recipient": "meghagraj97@gmail.com",
    "email_topic": "wishing her best of luck in her new role",
    "email_tone": "Praising",
    "email_length": 50
}

response = requests.post(url, json=payload, headers=headers)

try:
    result = response.json()
    print(result)
except ValueError:
    print("Invalid JSON response")
    print(response.text)

import requests
import time

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYTc2NDI5ZDMtZjlhOS00ZDIwLWFjYWUtMTFmNWMzZTU1NGI4IiwidHlwZSI6ImFwaV90b2tlbiJ9.bL2bJor-1d_5xOyuoSAxpYhOkYHwWV1M8chtqhlkOtQ",  # Replace with your actual token
    "Content-Type": "application/json"
}

workflow_id = "a2de4dac-040f-40a7-98e6-161d75959a10"
execution_id = "a2d17275-7c05-4e76-b994-b93f096b7f1f"
url = f"https://api.edenai.run/v2/workflow/{workflow_id}/execution/{execution_id}"

# Polling loop
while True:
    response = requests.get(url, headers=headers)
    try:Executing (38s)

        data = response.json()
        status = data.get("content", {}).get("status")

        print("Current status:", status)

        if status == "succeeded":
            print("🎉 Final Result:")
            print(data["content"]["results"])
            break
        elif status == "failed":
            print("❌ Workflow failed.")
            print(data)
            break
        else:
            time.sleep(5)  # Wait before checking again
    except ValueError:
        print("Invalid JSON response")
        print(response.text)
        break

