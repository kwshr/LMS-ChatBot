import sys
sys.path.insert(0,'C:\dev\LMS-ChatBot\LLM\Data_Objects')
from DataLoader import create_dataloader_v1
from GPTConfig import GPT_CONFIG_124M
from Trainingdata import val_data

val_loader = create_dataloader_v1(
    val_data,
    batch_size=2,
    max_length=GPT_CONFIG_124M["context_length"],
    stride=GPT_CONFIG_124M["context_length"],
    drop_last=False,
    shuffle=False,
    num_workers=0
)