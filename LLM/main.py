import torch
from Data.generateTxt import generate
from LLM.Train.GPTInstance import gpt, NEW_CONFIG
from TextGeneration.Encode_Decode import text_to_token_ids, token_ids_to_text
import tiktoken

tokenizer = tiktoken.get_encoding("gpt2")

torch.manual_seed(123)

token_ids = generate(
    model = gpt,
    idx = text_to_token_ids("Every effort moves you", tokenizer),
    max_new_tokens = 25,
    context_size =NEW_CONFIG["context_length"],
    top_k = 50,
    temperature=1.5,
)

print("Output text:\n", token_ids_to_text(token_ids, tokenizer))