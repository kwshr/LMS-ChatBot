# Copyright (c) Sebastian Raschka under Apache License 2.0 (see LICENSE.txt).
#This file includes code from "Build A Large Language Model From Scratch" by Sebastian Raschka.
#      - https://www.manning.com/books/build-a-large-language-model-from-scratch
# Original source: https://github.com/rasbt/LLMs-from-scratch
# 
# If you find this book or code useful for your research, please consider citing it:
#
# @book{build-llms-from-scratch-book,
#   author       = {Sebastian Raschka},
#   title        = {Build A Large Language Model (From Scratch)},
#   publisher    = {Manning},
#   year         = {2023},
#   isbn         = {978-1633437166},
#   url          = {https://www.manning.com/books/build-a-large-language-model-from-scratch},
#   note         = {Work in progress},
#   github       = {https://github.com/rasbt/LLMs-from-scratch}
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import torch.nn as nn
from MultiHeadAttention import MultiHeadAttention
from FeedForward import FeedForward
from LayerNorm import LayerNorm

class TransformerBlock(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.att = MultiHeadAttention(
            d_in=cfg["emb_dim"],
            d_out=cfg["emb_dim"],
            context_length=cfg["context_length"],
            num_heads=cfg["n_heads"],
            dropout=cfg["drop_rate"],
            qkv_bias=cfg["qkv_bias"])
        self.ff = FeedForward(cfg)
        self.norm1 = LayerNorm(cfg["emb_dim"])
        self.norm2 = LayerNorm(cfg["emb_dim"])
        self.drop_shortcut = nn.Dropout(cfg["drop_rate"])

    def forward(self, x):
        # Shortcut connection for attention block
        shortcut = x
        x = self.norm1(x)
        x = self.att(x)   # Shape [batch_size, num_tokens, emb_size]
        x = self.drop_shortcut(x)
        x = x + shortcut  # Add the original input back

        # Shortcut connection for feed-forward block
        shortcut = x
        x = self.norm2(x)
        x = self.ff(x)
        x = self.drop_shortcut(x)
        x = x + shortcut  # Add the original input back

        return x