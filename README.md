# Bengali BPE

**`bengali_bpe`** is a Python library for **Byte Pair Encoding (BPE)** specifically designed for the **Bengali language**.  
It enables you to train BPE models on Bengali text, encode words and sentences into subword units, and decode them back.  
This helps improve NLP model performance for Bengali text processing, tokenization, and embedding preparation.

---

## ✨ Features

- 🧠 Train a Byte Pair Encoding model on Bengali text corpus  
- 🔠 Encode Bengali sentences or words into subword tokens  
- 🔁 Decode subword tokens back into full Bengali words  
- ⚙️ Simple, lightweight, and easy to integrate into your NLP pipelines  
- 🪶 Supports Bengali Unicode normalization

---

## 📦 Installation

Install directly from PyPI:

```bash
pip install bengali_bpe

from bengali_bpe import BengaliBPE
from bengali_bpe.utils import normalize_bengali_text

# Sample Bengali corpus
corpus = [
    "বাংলা ভাষা সুন্দর",
    "আমি বাংলা পড়ি",
    "বাংলা ভয়ানক নয়"
]

# Normalize text
corpus = [normalize_bengali_text(sentence) for sentence in corpus]

# Initialize and train the model
bpe = BengaliBPE(num_merges=10)
bpe.train(corpus)

# Encode a sentence
sentence = "বাংলা ভাষা সুন্দর"
encoded = bpe.encode(sentence)
print("Encoded:", encoded)

# Decode back
decoded = bpe.decode(encoded)
print("Decoded:", decoded)


Encoded: [['বা', 'ংলা'], ['ভা', 'ষা'], ['সু', 'ন্', 'দর']]
Decoded: বাংলা ভাষা সুন্দর


from bengali_bpe import BengaliBPE

bpe = BengaliBPE(num_merges=5)
bpe.train(["বাংলা ভাষা সুন্দর"])
encoded_word = bpe.encode_word("বাংলা")
print("Encoded Word:", encoded_word)

decoded_word = bpe.decode([encoded_word])
print("Decoded Word:", decoded_word)


Encoded Word: ['বা', 'ংলা']
Decoded Word: বাংলা




