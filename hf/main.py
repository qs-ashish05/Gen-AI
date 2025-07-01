from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM
from transformers import Pipeline
import os
import torch

model_id = "google/gemma-3-1b-it"

tokenizer = AutoTokenizer.from_pretrained(model_id)

print(tokenizer("hello world"))

input_tokens = tokenizer("Hello world how are you?")['input_ids']
print(input_tokens)


model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype = torch.bfloat16)

gen_pipeline = Pipeline('text-genartion', model=model, tokenizer=tokenizer)

ans = gen_pipeline("what is gravity?", max_new_tokens = 28)
print(ans)