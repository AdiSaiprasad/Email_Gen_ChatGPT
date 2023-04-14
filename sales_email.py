import csv
import openai
import os

# load and set our key
key_file = "/Chat_GPT_Integration/key.txt"
path = os.getcwd() + key_file
openai.api_key = open(path, "r").read().strip("\n")

# key : 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
# Open the CSV file for reading

message_history =[]

def chat(inp, role="user"):
    message_history.append({"role": role, "content": f"{inp}"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history
    )
    reply_content = completion.choices[0].message.content
    message_history.append({"role": "assistant", "content": f"{reply_content}"})
    return reply_content

csv_file = "/Chat_GPT_Integration/sample_csv.csv"
path = os.getcwd() + csv_file

with open(path, 'r') as csvfile:
    # Create a CSV reader object
    reader = csv.reader(csvfile)
    
    # Loop through each row in the CSV file
    print("\n****************************\n")
    for row in reader:
        # Access data in each cell using index
        text = f"Write and email to {row[0]} working for {row[1]} company working in the domain of {row[2]} to sell custom software services, from Techpearl"
        print(chat(text))
        print("\n****************************\n")


