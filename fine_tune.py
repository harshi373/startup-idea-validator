from openai import OpenAI

client = OpenAI()

response = client.fine_tuning.create(
    training_file="file-5onZeyGXqJn9JshWR1Bf6a",
    model="gpt-3.5-turbo-1106"
)

print(response)
