



import google.generativeai as genai

# Step 1: Configure with your API key
genai.configure(api_key="AIzaSyBDizj3maJ5boj7J3C_YfHtdNv7ULpJbiE")

MODEL_NAME = "models/gemini-1.5-flash"  # Use "gemini-2.0-flash" if officially supported

# Step 3: Create the model with a system prompt
model = genai.GenerativeModel(
    model_name=MODEL_NAME,
    system_instruction="""
You are a professional and patient math teacher. 
Only answer questions related to mathematics (including arithmetic, algebra, geometry, calculus, probability, statistics, etc.).
If the user asks anything outside of math, kindly remind them that you are only here to help with math.
Always explain concepts step-by-step, and make sure your tone is warm, supportive, and encouraging.
"""

)

# Step 4: Start a chat session
chat = model.start_chat(history=[])

# Step 5: Start the teaching loop
print("👨‍🏫 Math Teacher Bot is ready! Ask any math question (type 'exit' to quit)\n")
while True:
    question = input("Student: ")
    if question.strip().lower() in ["exit", "quit"]:
        print("👋 Keep practicing, and see you next time!")
        break
    try:
        response = chat.send_message(question)
        print("\nTeacher:", response.text, "\n")
    except Exception as e:
        print("⚠️ Oops! Something went wrong:", e)