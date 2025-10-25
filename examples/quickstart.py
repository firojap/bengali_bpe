from bengali_bpe import BengaliBPE, normalize_bengali_text

corpus = ["বাংলা ভাষা সুন্দর", "আমি বাংলা পড়ি", "বাংলা ভয়ানক নয়"]
corpus = [normalize_bengali_text(s) for s in corpus]

bpe = BengaliBPE(num_merges=10)
bpe.train(corpus)
enc = bpe.encode("বাংলা ভাষা সুন্দর")
print("Encoded:", enc)
print("Decoded:", bpe.decode(enc))
