from openai import OpenAI

client = OpenAI(
  api_key="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"
)

response = client.responses.create(
  model="gpt-5-nano",
  input="write a haiku about ai",
  store=True,
)

print(response.output_text);