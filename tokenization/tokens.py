import tiktoken

encoder = tiktoken.encoding_for_model('gpt-4o')

# vocab size means how many unique words the model supports / tokenization algorithm supports
print(f'The vocab sixe of tokenizer of this model is {encoder.n_vocab}')

text = "What is the gravity?"

tokens = encoder.encode(text)
print(f'Tokens for the text - {text} is \n {tokens}')


#orginal text
decode = encoder.decode(tokens)
print(f'The original text of tokens - {tokens} is \n {decode}')