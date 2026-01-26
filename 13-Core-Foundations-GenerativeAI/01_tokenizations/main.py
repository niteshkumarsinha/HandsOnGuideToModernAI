import tiktoken


encoder = tiktoken.encoding_for_model("gpt-4o")

text = "Hello, world!"
tokens = encoder.encode(text)

print(f"Tokens: {tokens}")
print(f"Number of tokens: {len(tokens)}")
decoded_text = encoder.decode(tokens)
print(f"Decoded Text: {decoded_text}")
