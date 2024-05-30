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

import torch

def generate_text_simple(model, idx, max_new_tokens, context_size):
    # idx is (B, T) array of indices in the current context
    for _ in range(max_new_tokens):

        # Crop current context if it exceeds the supported context size
        # E.g., if LLM supports only 5 tokens, and the context size is 10
        # then only the last 5 tokens are used as context
        idx_cond = idx[:, -context_size:]

        # Get the predictions
        with torch.no_grad():
            logits = model(idx_cond)

        # Focus only on the last time step
        # (batch, n_token, vocab_size) becomes (batch, vocab_size)
        logits = logits[:, -1, :]

        # Get the idx of the vocab entry with the highest logits value
        idx_next = torch.argmax(logits, dim=-1, keepdim=True)  # (batch, 1)

        # Append sampled index to the running sequence
        idx = torch.cat((idx, idx_next), dim=1)  # (batch, n_tokens+1)

    return idx