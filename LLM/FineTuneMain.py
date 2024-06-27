from functools import partial
import tiktoken
from torch.utils.data import DataLoader
import torch
from .FineTune.InstructionDataset import InstructionDataset
from .FineTune.CustomCollate import custom_collate_fn
from .FineTune.Dataset import train_data, val_data, test_data

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
customized_collate_fn = partial(custom_collate_fn, device=device, allowed_max_length=1024)
tokenizer = tiktoken.get_encoding("gpt2")

num_workers = 0
batch_size = 8

torch.manual_seed(123)

train_dataset = InstructionDataset(train_data, tokenizer)
train_loader = DataLoader(
    train_dataset,
    batch_size=batch_size,
    collate_fn=customized_collate_fn,
    shuffle=True,
    drop_last=True
)

val_dataset = InstructionDataset(val_data, tokenizer)
val_loader = DataLoader(
    val_dataset,
    batch_size=batch_size,
    collate_fn=customized_collate_fn,
    shuffle=False,
    drop_last=False
)

test_dataset = InstructionDataset(test_data, tokenizer)
test_loader = DataLoader(
    test_dataset,
    batch_size=batch_size,
    collate_fn=customized_collate_fn,
    shuffle=False,
    drop_last=False
)