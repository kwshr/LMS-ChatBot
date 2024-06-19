from flask import Flask, request, jsonify
import torch
# import sys
# sys.path.insert(2,'C:\dev\LMS-ChatBot\LLM\TextGeneration')
from TextGeneration.GenerateText import generate
# sys.path.insert(4,'C:\dev\LMS-ChatBot\LLM\GPT_Weights')
from GPT_Weights.gpt_download import download_and_load_gpt2
from GPT_Weights.LoadWeightsIntoGPT import load_weights_into_gpt
import tiktoken
# sys.path.insert(1,'C:\dev\LMS-ChatBot\LLM\Model')
from Model.GPTModel import GPTModel
from ModelConfigurations import model_configs
from flask_cors import CORS 

CHOOSE_MODEL = "gpt2-small (124M)"
BASE_CONFIG = {
    "vocab_size": 50257,     # Vocabulary size
    "context_length": 1024,  # Context length
    "drop_rate": 0.1,        # Dropout rate
    "qkv_bias": True         # Query-key-value bias
}

BASE_CONFIG.update(model_configs[CHOOSE_MODEL])

model_size = CHOOSE_MODEL.split(" ")[-1].lstrip("(").rstrip(")")
settings, params = download_and_load_gpt2(model_size=model_size, models_dir="gpt2")

model = GPTModel(BASE_CONFIG)
load_weights_into_gpt(model, params)
model.eval()

app = Flask(__name__)
CORS(app) 

@app.route('/generate', methods=['GET'])
def generate_text():
    start_context = request.args.get("prompt")
    max_tokens = 100

    tokenizer = tiktoken.get_encoding("gpt2")
    encoded = tokenizer.encode(start_context)
    encoded_tensor = torch.tensor(encoded).unsqueeze(0)

    out = generate(
        model=model,
        idx=encoded_tensor,
        max_new_tokens=max_tokens,
        context_size=BASE_CONFIG["context_length"],
        top_k=50,
        temperature=5.0
    )
    decoded_text = tokenizer.decode(out.squeeze(0).tolist())
    return jsonify({'generated_text': decoded_text}) 

if __name__ == '__main__':
    app.run()