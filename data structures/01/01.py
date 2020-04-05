text = "X-DSPAM-Confidence:    0.8475";

pos = text.find("0.")
text2 = float(text[pos : pos + 7])
print(text2)