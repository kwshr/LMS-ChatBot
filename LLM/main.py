import torch
import sys
sys.path.insert(2,'C:\dev\LMS-ChatBot\LLM\TextGeneration')
from GenerateText import generate
sys.path.insert(4,'C:\dev\LMS-ChatBot\LLM\GPT_Weights')
from gpt_download import download_and_load_gpt2
from LoadWeightsIntoGPT import load_weights_into_gpt
import sys
sys.path.insert(2,'C:\dev\LMS-ChatBot\LLM\TextGeneration')
from GenerateText import generate
sys.path.insert(4,'C:\dev\LMS-ChatBot\LLM\GPT_Weights')
from gpt_download import download_and_load_gpt2
from LoadWeightsIntoGPT import load_weights_into_gpt
import tiktoken
sys.path.insert(1,'C:\dev\LMS-ChatBot\LLM\Model')
from GPTModel import GPTModel

CHOOSE_MODEL = "gpt2-small (124M)"
INPUT_PROMPT = "Every effort moves"

BASE_CONFIG = {
    "vocab_size": 50257,     # Vocabulary size
    "context_length": 1024,  # Context length
    "drop_rate": 0.0,        # Dropout rate
    "qkv_bias": True         # Query-key-value bias
}

model_configs = {
    "gpt2-small (124M)": {"emb_dim": 768, "n_layers": 12, "n_heads": 12},
    "gpt2-medium (355M)": {"emb_dim": 1024, "n_layers": 24, "n_heads": 16},
    "gpt2-large (774M)": {"emb_dim": 1280, "n_layers": 36, "n_heads": 20},
    "gpt2-xl (1558M)": {"emb_dim": 1600, "n_layers": 48, "n_heads": 25},
}

BASE_CONFIG.update(model_configs[CHOOSE_MODEL])

model_size = CHOOSE_MODEL.split(" ")[-1].lstrip("(").rstrip(")")
settings, params = download_and_load_gpt2(model_size=model_size, models_dir="gpt2")

model = GPTModel(BASE_CONFIG)
load_weights_into_gpt(model, params)
model.eval()

start_context = "Every effort moves you"

tokenizer = tiktoken.get_encoding("gpt2")
encoded = tokenizer.encode(start_context)
encoded_tensor = torch.tensor(encoded).unsqueeze(0)

out = generate(
    model=model,
    idx=encoded_tensor,
    max_new_tokens=25,
    context_size=BASE_CONFIG["context_length"],
    top_k=50,
    temperature=5.0
)
decoded_text = tokenizer.decode(out.squeeze(0).tolist())

print("Output text:", decoded_text)