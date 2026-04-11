# Write a function that extracts all dates (in the format DD/MM/YYYY) from a given text using regex.

import re

def extract_dates(texts):
    pattern = r"\b\d{2}/\d{2}/\d{4}\b"
    return re.findall(pattern, texts)



sample_text = "We met on 12/04/2026 and again on 25/12/2026."
print(extract_dates(sample_text))