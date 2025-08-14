import os
import google.generativeai as genai
import datetime

# --- Your Settings ---
# Put a list of article ideas here. The robot will pick one.
TOPIC_LIST = [
    "five tips for growing tomatoes indoors",
    "how to create the perfect soil mix for potted plants",
    "the easiest vegetables for a beginner to grow",
    "understanding natural sunlight versus grow lights",
    "how often should you water different types of houseplants"
]
# --- End of Settings ---

# Get the secret key
api_key = os.environ.get('GEMINI_API_KEY')
if not api_key:
    raise ValueError("API key not found. Please set the GEMINI_API_KEY secret.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

# Choose a topic
topic = TOPIC_LIST[datetime.datetime.now().day % len(TOPIC_LIST)] # Picks a new topic each day

# Ask the AI to write
prompt = f"Write a simple, helpful, 500-word blog post for beginners about '{topic}'. Use a friendly tone. Use HTML formatting with h1 for the title and p for paragraphs."
response = model.generate_content(prompt)

# Save the article as an HTML file
with open("index.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("Article generated successfully!")
