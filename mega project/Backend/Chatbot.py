from groq import Groq
from json import load,dump
import datetime
from dotenv import dotenv_values


env_vars = dotenv_values(".env")

Username = env_vars.get("Username")
Assistantname = env_vars.get("Assistantname")
GroqAPIKey = env_vars.get("GroqAPIKey")

client = Groq(api_key=GroqAPIKey)

messages = []

System = f"""Hello, I am {Username},Your creater is Girish to make variety of task is easy, You are a very advance artificial inteligense defence security system named {Assistantname} that name stand for Just A Rather Very Intelligent System which also has real-time up-to-date information from the internet 7 day of a week, 24/7 hour in a day you assist.
*** Do not tell time until I ask, do not talk too much, just answer the question.***
*** Reply in English, even if the question is in Hindi or gujarati, reply in English.***
*** Do not provide notes in the output, just answer the question and never mention your training data. ***
*** if the username is nidhi then you talk and answer in flirting way ***
"""

SystemChatBot = [
    {"role": "system", "content": System}
]

try:
    with open(r"Data\ChatLog.json", "r" ) as f:
        messages = load(f)
except FileNotFoundError:
    with open(r"Data\ChatLog.json", "w") as f:
        dump([], f)

def RealtimeInnformation():
    current_date_time = datetime.datetime.now()
    day = current_date_time.strftime("%A")
    date = current_date_time.strftime("%d")
    month = current_date_time.strftime("%B")
    year = current_date_time.strftime("%Y")
    hour = current_date_time.strftime("%H")
    minute = current_date_time.strftime("%M")
    second = current_date_time.strftime("%S")

    data = f"Please use this real-time information if needed,\n"
    data += f"Day: {day}\nDate: {date}\nMonth: {month}\nYear: {year}\n"
    data += f"Time: {hour} hours :{minute} minutes :{second} seconds.\n"
    return data
    
def AnswerModifier(Answer):
    lines = Answer.split('\n')
    non_empty_lines = [line for line in lines if line.strip()]
    modified_answer = '\n'.join(non_empty_lines)
    return modified_answer
    
def ChatBot(Query):
    """This function sends the user's query to the chatbot and returns the AI's response."""
   
    try:
        with open(r"Data\ChatLog.json", "r") as f:
            messages = load(f)

        messages.append({"role": "user", "content": f"{Query}"})

        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=SystemChatBot + [{"role": "system", "content": RealtimeInnformation()}] + messages,
            max_tokens=1024,
            temperature=0.7,
            top_p=1,
            stream=True,
            stop=None
        )

        Answer = ""

        for chunk in completion:
            if chunk.choices[0].delta.content:
                Answer += chunk.choices[0].delta.content

        Answer = Answer.replace("</s", "")

        messages.append({"role": "assistant", "content": Answer})

        with open(r"Data\ChatLog.json", "w") as f:
            dump(messages, f, indent=4)

        return AnswerModifier(Answer=Answer)
            
    except Exception as e:

        print(f"Error: {e}")
        with open(r"Data\ChatLog.json", "w") as f:
            dump([], f, indent=4)
        return ChatBot(Query)
        
if __name__ == "__main__":
    while True:
        # user_input = input("Enter your Question: ")
        text = (ChatBot(input("Enter your Question: ")))
        # hindi = Translator().translator.translate(text, src="en", dest="hi").text
        print(f"Jarvis: {text}")
        # if text == None:
        #     pass
        # else:
        #     # TextToSpeech.TextToSpeech(text)
            