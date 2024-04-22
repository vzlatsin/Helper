import openai  # Correct import statement

# Set your API key
openai.api_key = "<SECRET>"  # Replace with your actual key

# Create a completion
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant."},
        {"role": "user", "content": "Compose a poem that explains recursion."},
    ],
)

print(completion.choices[0].message['content'])  # Accessing the response content
