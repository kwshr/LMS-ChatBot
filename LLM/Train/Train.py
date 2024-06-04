import torch
import tiktoken
from TrainModelSimple import train_model_simple
from TrainLoaderConfig import train_loader
from ValLoader import val_loader
import sys
sys.path.insert(1,'C:\dev\LMS-ChatBot\LLM\Model')
from GPTModel import GPTModel
from GPTConfig import GPT_CONFIG_124M
import sys
sys.path.insert(2,'C:\dev\LMS-ChatBot\LLM\TextGeneration')
from GenerateText import generate
from Encode_Decode import text_to_token_ids

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = tiktoken.get_encoding("gpt2")
torch.manual_seed(123)
model = GPTModel(GPT_CONFIG_124M)
model.to(device)
optimizer = torch.optim.AdamW(model.parameters(), lr=0.0004, weight_decay=0.1)

num_epochs = 10
train_losses, val_losses, tokens_seen = train_model_simple(
    model, train_loader, val_loader, optimizer, device,
    num_epochs=num_epochs, eval_freq=5, eval_iter=5,
    start_context="Every effort moves you", tokenizer=tokenizer
)

token_ids = generate(
    model=model,
    idx=text_to_token_ids("Every effort moves you", tokenizer),
    max_new_tokens=15,
    context_size=GPT_CONFIG_124M["context_length"],
    top_k=25,
    temperature=1.4
)
torch.save(model.state_dict(), "model.pth")