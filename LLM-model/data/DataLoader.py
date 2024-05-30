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

import tiktoken
import GPTDataset
from torch.utils.data import DataLoader

def create_dataloader_v1(txt, batch_size=4, max_length=256,
                         stride=128, shuffle=True, drop_last=True, num_workers=0):
    # Initialize the tokenizer
    tokenizer = tiktoken.get_encoding("gpt2")

    # Create dataset
    dataset = GPTDataset(txt, tokenizer, max_length, stride)

    # Create dataloader
    dataloader = DataLoader(
        dataset, batch_size=batch_size, shuffle=shuffle, drop_last=drop_last, num_workers=0)

    return dataloader