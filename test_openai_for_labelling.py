import openai

# Set up your API key
openai.api_key = 'your-api-key-here'

# Define your labels and the text you want to label
labels = ["Label1", "Label2", "Label3"]
text_to_label = "Your text goes here."

# Create a prompt
prompt = f"Given the following labels: {', '.join(labels)}, please categorize the following text: \"{text_to_label}\""

# Call the OpenAI model
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # or whichever model you are using
    messages=[
        {"role": "user", "content": prompt}
    ]
)

# Get the response
labeled_text = response['choices'][0]['message']['content']
print(labeled_text)
