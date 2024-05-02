import spacy
import os
import numpy as np
import glob
import re

# Load the spaCy medium model with pre-trained vectors
nlp = spacy.load("en_core_web_md")


def extract_words(filename):
    # Get the basename (filename without path)
    base_name = os.path.basename(filename)
    # Remove the extension
    name_part = os.path.splitext(base_name)[0]
    # Split by underscores to get the words
    words_ = name_part.split("_")
    return words_


def get_embedding_for_words(words_):
    embeddings = []

    for word in words_:
        # Get the spaCy token for the word
        token = nlp(word)
        # Get the vector if it has one, otherwise a zero vector
        embeddings.append(token.vector)

    # Combine embeddings for all words in the filename (using mean)
    return np.mean(embeddings, axis=0)


# List of files to process (recursive search)
file_pattern = "./resampled/**/*.wav"
file_list = glob.glob(file_pattern, recursive=True)

# Dictionary to hold the filename (without extension) and its corresponding embedding
file_embeddings = {}

for file in file_list:
    # Extract words from filename
    words = extract_words(file)
    # Generate the embedding for the words in this filename
    embedding = get_embedding_for_words(words)
    # Use filename without path and extension as key
    key = os.path.splitext(os.path.basename(file))[0]
    file_embeddings[key] = embedding

# Directory for storing embeddings
embeddings_dir = "./embeddings_spacy/"
# Ensure the directory exists
os.makedirs(embeddings_dir, exist_ok=True)

# Save each embedding as a numpy file
for key, embedding in file_embeddings.items():
    np.save(os.path.join(embeddings_dir, f"{key}.npy"), embedding)

print(f"Embeddings saved successfully to {embeddings_dir}")
