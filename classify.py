import json
from openai import OpenAI
import os

# load the data
input_file = open('data/support_tickets.json')
data = json.load(input_file)

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ["OPENAI_API_KEY"]
)

# get the tags
file_path = 'data/tags.txt'
with open(file_path, 'r') as file:
    tags = [line.strip() for line in file]
# print(tags)
    
# get the priorities
file_path = 'data/priorities.txt'
with open(file_path, 'r') as file:
    priorities = [line.strip() for line in file]
# print(tags)

examples = "".join([f"Text: {element['description']}\nPriority: {element['priority']}\n" for i, element in enumerate(data[:5])])
count, score_priority, score_tags = 0, 0

for element in data[100:110]:
    # print(element)
    ticket_text = element['description']

    # Prompt – Classify Priority
    user_prompt_priority = f"""
    Classify the text into one of the following classes.
    Classes: {priorities}
    {examples}
    Text: {ticket_text}
    Priority: """
    # print("Prompt: "+user_prompt_priority)

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
    if(response.choices[0].message.content == element['priority']):
        score_priority += 1
    count += 1

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
    print("Predicted Tags: \n"+response.choices[0].message.content)
    print("Actual Tags:")
    print(element['tags'])

print("__________________")
print(f"Priority Accuracy: {score_priority/count}")


