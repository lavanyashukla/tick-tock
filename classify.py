import json
from openai import OpenAI
import os

# load the data
input_file = open('data/support_tickets.json')
data = json.load(input_file)

# what am I looking at
for element in data: 
    # print(element)
    break

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ["OPENAI_API_KEY"]
)

# get the tags
file_path = 'tags.txt'
with open(file_path, 'r') as file:
    tags = [line.strip() for line in file]
# print(tags)

# Prompt 1 – Add Class: in the prompt
ticket_text = element['description']
user_prompt_2 = f"""
Classify the text into one of the following classes.
Classes: {tags}
Text: {ticket_text}
Class: """

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": user_prompt_2},
    ],
    max_tokens=100
)
print("Predicted: \n"+response.choices[0].message.content)
print("Actual:")
print(element['tags'])