import nltk
import re
nltk.download('punkt')

def data_preprocess(word_chunks: str):
  clean_word_chunks = re.sub(r"[^a-zA-Z0-9\s.,!?']", "", word_chunks) #regex based cleaning for text
  sentences = nltk.sent_tokenize(clean_word_chunks)
  return sentences
  

