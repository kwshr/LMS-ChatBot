# This file includes code from "Build A Large Language Model From Scratch" by Sebastian Raschka.
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

import torch
import torch.nn as nn

class LayerNorm(nn.Module):
    def __init__(self, emb_dim):
        super().__init__()
        self.eps = 1e-5
        self.scale = nn.Parameter(torch.ones(emb_dim))
        self.shift = nn.Parameter(torch.zeros(emb_dim))

    def forward(self, x):
        mean = x.mean(dim=-1, keepdim=True)
        var = x.var(dim=-1, keepdim=True, unbiased=False)
        norm_x = (x - mean) / torch.sqrt(var + self.eps)
        return self.scale * norm_x + self.shift