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

```
pip install bengali_bpe
```
---

## Usage Examples
### Train a BPE Model and Encode Sentences

```
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
```
---

## Output

```
Encoded: [['বা', 'ংলা'], ['ভা', 'ষা'], ['সু', 'ন্', 'দর']]
Decoded: বাংলা ভাষা সুন্দর
```
---

## Encode and Decode a Single Word

```
from bengali_bpe import BengaliBPE

bpe = BengaliBPE(num_merges=5)
bpe.train(["বাংলা ভাষা সুন্দর"])
encoded_word = bpe.encode_word("বাংলা")
print("Encoded Word:", encoded_word)

decoded_word = bpe.decode([encoded_word])
print("Decoded Word:", decoded_word)
```

## Output

```
Encoded Word: ['বা', 'ংলা']
Decoded Word: বাংলা
```
---
## Normalize Bengali Text

```
from bengali_bpe.utils import normalize_bengali_text

text = "বাংলা    ভাষা    সুন্দর।।"
print(normalize_bengali_text(text))
```
---

## Output

```
বাংলা ভাষা সুন্দর।।
```
---

## Example: Training and Applying BPE on a Bengali Paragraph

```
from bengali_bpe import BengaliBPE
from bengali_bpe.utils import normalize_bengali_text

text = """বাংলা একটি মধুর ভাষা। এটি বিশ্বের অন্যতম প্রাচীন ও সমৃদ্ধ ভাষাগুলোর একটি।
বাংলা ভাষার ইতিহাস ও ঐতিহ্য হাজার বছরের পুরোনো।"""

corpus = [normalize_bengali_text(text)]
bpe = BengaliBPE(num_merges=15)
bpe.train(corpus)

encoded = bpe.encode("বাংলা একটি মধুর ভাষা")
print("Encoded:", encoded)

decoded = bpe.decode(encoded)
print("Decoded:", decoded)
```
---

## Full Example: Combine All Steps

```
from bengali_bpe import BengaliBPE
from bengali_bpe.utils import normalize_bengali_text

corpus = [
    "আমি বাংলা ভাষা ভালোবাসি",
    "বাংলা একটি সুন্দর ভাষা",
    "বাংলা আমাদের মাতৃভাষা"
]

corpus = [normalize_bengali_text(c) for c in corpus]
bpe = BengaliBPE(num_merges=12)
bpe.train(corpus)

sentence = "আমি বাংলা ভালোবাসি"
encoded = bpe.encode(sentence)
decoded = bpe.decode(encoded)

print("Original:", sentence)
print("Encoded:", encoded)
print("Decoded:", decoded)
```
---

## Output

```
Original: আমি বাংলা ভালোবাসি
Encoded: [['আ', 'মি'], ['বা', 'ংলা'], ['ভা', 'লো', 'বা', 'সি']]
Decoded: আমি বাংলা ভালোবাসি
```
---

## Example Use Cases

| Use Case                     | Description                                                              |
| ---------------------------- | ------------------------------------------------------------------------ |
| 🔤 **Subword Tokenization**  | Split Bengali words into meaningful subword units for NLP models         |
| 🧩 **Embedding Preparation** | Generate stable subword tokens for embedding or transformer-based models |
| 🧠 **Text Compression**      | Apply BPE for efficient text representation                              |
| 📚 **Data Preprocessing**    | Clean and normalize Bengali text before training models                  |

---
## API References

| Function                       | Description                                           |
| ------------------------------ | ----------------------------------------------------- |
| `train(corpus)`                | Train the BPE model on a list of Bengali sentences    |
| `encode(text)`                 | Encode an entire Bengali sentence into subword tokens |
| `encode_word(word)`            | Encode a single Bengali word                          |
| `decode(encoded_words)`        | Decode BPE tokens back to full Bengali text           |
| `normalize_bengali_text(text)` | Normalize and clean Bengali text (NFC normalization)  |

---
## Project Structure

```
bengali_bpe/
├── bengali_bpe/
│   ├── __init__.py
│   ├── encoder.py
│   └── utils.py
├── tests/
│   └── test_encoder.py
├── README.md
├── setup.py
└── LICENSE
```
---
## Developer

**Firoj Ahmmed Patwary**</br>
BSc & MSc in Statistics, Jagannath University</br>
MSc in Data Science, Freie Universität Berlin</br>
Researcher in Data Science, Machine Learning, NLP, and Explainable AI

---
## Contact:

```
🌐 Website: www.firoj.net

📧 Email: firoj.stat@gmail.com
```


