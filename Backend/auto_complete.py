import os
import openai

# NOTE: Change Key Path to you Absolute Path
openai.api_key_path = "/Users/valley/Desktop/External_Finder/Hackathons/la_hacks_2023/Backend/auto_complete_key.txt"

def auto_complete(payload):
    auto_complete_prompt = "Exand on this thought as if it were a continuation of my thought: "
    response = openai.Completion.create(model="text-davinci-003", prompt = auto_complete_prompt + payload, temperature = 0.6, max_tokens = 50)
    return response["choices"][0]["text"].replace("\n", "")

def query_complete(payload, query):
    query_complete_prompt = f"Keeping {payload} in mind, answer the following question to the best of your abilities in a succinct manner and as if it were a continuation of my thought"
    response = openai.Completion.create(model="text-davinci-003", prompt = query_complete_prompt + query, temperature = 0.6, max_tokens = 50)
    return response["choices"][0]["text"].replace("\n", "")
    
# auto_complete("We could create an app that provides resources and tools for people to manage their stress and anxiety levels.")
# print(query_complete("We could create an app that provides resources and tools for people to manage their stress and anxiety levels.", "What features should this app feature?"))

# import cohere
# co = cohere.Client('1g4kF4R2RpuNTB3ehW1tRWW4QMh3pbF8zgdJGSl8')

# response = co.generate(
#   prompt="Exand on this thought: We could create an app that provides resources and tools for people to manage their stress and anxiety levels.",
# )
# print(":: ", response)