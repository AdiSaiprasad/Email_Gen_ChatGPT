import openai

# load and set our key
openai.api_key = open("/Users/adisai/Python_Projects/Chat_GPT_Integration/key.txt", "r").read().strip("\n")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", # this is "ChatGPT" $0.002 per 1k tokens
  messages=[{"role": "user", "content": "What is the circumference in km of the planet Earth?"}]
)
print(completion)

reply_content = completion.choices[0].message.content
print(reply_content)

# In order to keep track of the history of messages use a way to store it
message_history = []
# What is the moon's circumference in km?
user_input = input("> ")
print("User's input was: ", user_input)
message_history.append({"role": "user", "content": f"{user_input}"})
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=message_history
)

# Now we can print the response:
reply_content = completion.choices[0].message.content
print(reply_content)

# "assistant" used to append
message_history.append({"role": "assistant", "content": f"{reply_content}"})

# which moon is that in reference to? -- ontinued user input
user_input = input("> ")
print("User's input was: ", user_input)
print()
message_history.append({"role": "user", "content": f"{user_input}"})

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=message_history
)

reply_content = completion.choices[0].message.content
print(reply_content)

message_history = []

def chat(inp, role="user"):
    message_history.append({"role": role, "content": f"{inp}"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history
    )
    reply_content = completion.choices[0].message.content
    message_history.append({"role": "assistant", "content": f"{reply_content}"})
    return reply_content

for i in range(2):
    user_input = input("> ")
    print("User's input was: ", user_input)
    print(chat(user_input))
    print()