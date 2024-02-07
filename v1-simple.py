from openai import OpenAI
import os

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ["OPENAI_API_KEY"]
)

# Prompt 1
ticket_text = "I've been trying to clone a workspace for a new member of our team, but the clone operation fails every time with a vague error message. This workspace setup is crucial for standardizing our project environments. Could you provide some insight or assistance on cloning workspaces successfully?"
user_prompt_1 = f"""
Classify the text into one of the following classes.
Classes: [artifacts, reports, workspaces, sweeps, prompts, launch, tables, performance, deployment]
Text: {ticket_text}
"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": user_prompt_1},
    ],
    max_tokens=100
)
print ("Prompt 1: \n"+response.choices[0].message.content)

# Prompt 2 – Add Class: in the prompt
ticket_text = "I've been trying to clone a workspace for a new member of our team, but the clone operation fails every time with a vague error message. This workspace setup is crucial for standardizing our project environments. Could you provide some insight or assistance on cloning workspaces successfully?"
user_prompt_2 = f"""
Classify the text into one of the following classes.
Classes: [artifacts, reports, workspaces, sweeps, prompts, launch, tables, performance, deployment]
Text: {ticket_text}
Class: """

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": user_prompt_2},
    ],
    max_tokens=100
)
print ("Prompt 2: \n"+response.choices[0].message.content)

# Prompt 3 – Add Examples: in the prompt
ticket_text = "I've been trying to clone a workspace for a new member of our team, but the clone operation fails every time with a vague error message. This workspace setup is crucial for standardizing our project environments. Could you provide some insight or assistance on cloning workspaces successfully?"
user_prompt_2 = f"""
Classify the text into one of the following classes.
Classes: [artifacts, reports, workspaces, sweeps, prompts, launch, tables, performance, deployment]
Text: {ticket_text}
Class: """

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": user_prompt_2},
    ],
    max_tokens=100
)
print ("Prompt 2: \n"+response.choices[0].message.content)










