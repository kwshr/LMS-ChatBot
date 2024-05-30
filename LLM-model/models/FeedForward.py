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

import GELU
import torch.nn as nn

class FeedForward(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(cfg["emb_dim"], 4 * cfg["emb_dim"]),
            GELU(),
            nn.Linear(4 * cfg["emb_dim"], cfg["emb_dim"]),
        )

    def forward(self, x):
        return self.layers(x)