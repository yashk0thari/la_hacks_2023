import whisper
import ssl
import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

# Temporary Fix for whisper run-time:
ssl._create_default_https_context = ssl._create_unverified_context

def run_whisper(file):
    model = whisper.load_model("base")
    result = model.transcribe(file, fp16 = False)
    # return result["text"]
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt= "Please break the following text into sentences: \n" + result["text"] + "\n"
    )

    if response.choices:
        return response.choices[0].text.strip()
    else:
        return ""

# print(run_whisper("/Users/arjunrajloomba/Desktop/recording1.wav"))