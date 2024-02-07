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
    
# get the priorities
file_path = 'priorities.txt'
with open(file_path, 'r') as file:
    priorities = [line.strip() for line in file]
# print(tags)


ticket_text = element['description']

# Prompt – Classify Priority
user_prompt_priority = f"""
Classify the text into one of the following classes.
Classes: {priorities}
Text: {ticket_text}
Priority: """

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": user_prompt_priority},
    ],
    max_tokens=100
)
print("Predicted Priority: \n"+response.choices[0].message.content)
print("Actual Priority:")
print(element['priority'])
print("__________________")


# Prompt – Classify Class
user_prompt_tag = f"""
Classify the text into one of the following classes.
Classes: {tags}
Text: {ticket_text}
Class: """

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": user_prompt_tag},
    ],
    max_tokens=100
)
print("Predicted Tag: \n"+response.choices[0].message.content)
print("Actual Tag:")
print(element['tags'])
