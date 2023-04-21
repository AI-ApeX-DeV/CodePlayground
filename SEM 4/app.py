from flask import Flask, request, render_template
import pywhatkit
import datetime
import openai

app = Flask(__name__)

# Set up OpenAI API key
openai.api_key = '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'

messages = [
    {"role": "system", "content": "You are a kind helpful assistant for assisting people for mental fitnesss and mental health."},
]

@app.route('/')
def home():
    return render_template('index.html', messages=messages)

@app.route('/chat', methods=['POST','GET'])
def chat():
    global messages
    command = request.form['command']

    if 'play' in command:
        words_to_replace = ["play", "music",'song','play the song','hello','hi']
        for word in words_to_replace:
            command = command.replace(word,"")
        print("ok,playing the song for you on youtube")
        pywhatkit.playonyt(command)
        reply = "Playing " + command + " on YouTube."
        messages.append({"role": "assistant", "content": reply})
    elif 'time' in command:
        now = datetime.datetime.now()
        day_name = now.strftime("%A")
        day_num = now.strftime("%d")
        month = now.strftime("%B")
        hour = now.strftime("%H")
        minute = now.strftime("%M")

        reply = "Today is "+ day_name+" "+ day_num+" "+ month + " and the time is "+  hour +  " : "+ minute
        messages.append({"role": "assistant", "content": reply})
    elif 'quit' in command or "end" in command:
        reply = "Thank you for using the mental health checkup app!"
        messages.append({"role": "assistant", "content": reply})
    else:
        message = command
        if message:
            try:
                # Split the message into words and check if it has more than 20 words
                if len(message.split()) > 45:
                    raise ValueError("Input contains more than 45 words. Please try again.")
                messages.append({"role": "user", "content": message})
                chat = openai.Completion.create(
                    model="text-davinci-002", prompt=f"{messages[-1]['content']} Assistant: ", max_tokens=360
                )
            except ValueError as e:
                print(f"Error: {e}")
            reply = chat.choices[0].text
            messages.append({"role": "assistant", "content": reply})

    return render_template('index.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
