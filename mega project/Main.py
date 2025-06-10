from Backend import TextToSpeech, Chatbot, RealtimeSearchEngine, Model, Automation#,ImageGeneration
import asyncio
import eel
import os
import sqlite3


file_path=".env"

eel.init('Frontend')

@eel.expose
def S(text):
    text = str(text)
    
    d = Model.FirstLayerDMM(text)
    G = any([i for i in d if i.startswith("general")])
    R = any([i for i in d if i.startswith("realtime")])

    if G == True:
        res = Chatbot.ChatBot(text)
        # print("Jarvis: ",res)          
        return res           
        
    elif R == True:
        res = RealtimeSearchEngine.RealtimeSearchEngine(text)
        # print("Jarvis: ",res)
        return res
        
    elif G == False and R == False:
        asyncio.run(Automation.Automation(d))

        if text.startswith("play "):
            return f"playing {text.removeprefix('play ')} on youtube."
        if text.startswith("open "):
            return f"opening {text.removeprefix('open ')}"
        if text.startswith("close "):
            return f"closing {text.removeprefix('close ')}"
     


@eel.expose
def speak(data):
     data = str(data)
     d=(TextToSpeech.TextToSpeech(data))
     return d

@eel.expose
def check_login(email, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    result = c.fetchall()
    conn.close()
    for name in result:
        lines = []
    
    # Read existing lines
        with open(file_path, "r") as file:
            lines = file.readlines()

        # Modify if key exists
        for i, line in enumerate(lines):
            if line.startswith(f"Username="):
                lines[i] = f"Username={name[0]}\n"
                break

        # Write back to file
        with open(file_path, "w") as file:
            file.writelines(lines)

        print(f"Username updated to {name[0]}")
        print("i am ",name[0])
        Chatbot.ChatBot(f"i am {name[0]}")
        RealtimeSearchEngine.RealtimeSearchEngine(f"i am {name[0]}")
        
    print(result)
    if result:
        print("login successful")
        return "s"

    else:
        print("login failed")
        return "email or password is incorrect"
    




@eel.expose
def register_user(name,email,password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (name,email,password) VALUES (?, ?, ?)", (name,email, password))
        conn.commit()
        return "s"
    except sqlite3.IntegrityError:
        return "exists"
    finally:
        conn.close()




eel.start('login.html', size=(1900, 1000))
                
