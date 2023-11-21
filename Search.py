import spacy
import os
import re
import numpy as np
from numpy.linalg import norm

nlp = spacy.load("en_core_web_sm")

def preprocess_text_spacy(text):
    # Load the spaCy English model
    nlp = spacy.load("en_core_web_sm")

    text = re.sub(r'[^\w\s]','',text)

    # Process the text using spaCy
    doc = nlp(text)

    # Remove stop words and perform lemmatization
    preprocessed_tokens = [token.lemma_ for token in doc if not token.is_stop]

    return preprocessed_tokens

all_tokens = []
all_tokens_counts = {}  
doc_list  = []

class Document:
    def __init__(self, text):
        self.original_text = text
        self.tokens = preprocess_text_spacy(self.original_text)
        global all_tokens
        all_tokens = list(set(all_tokens + self.tokens))
        self.term_count = {}
        self.TF = {}
        self.cos_sim = 0

    
def init():
    global all_tokens
    global all_tokens_counts
    global doc_list 

    # # Sample documents
    # document1 = "Natural language processing (NLP) is a subfield of artificial intelligence (AI)."
    # document2 = "Artificial intelligence (AI) involves the development of algorithms and models."
    # document3 = "Machine learning (ML) is a branch of artificial intelligence that focuses on building systems that can learn from and make decisions based on data."
    # document4 = "In the field of data science, data preprocessing is a crucial step to clean, transform, and organize raw data for analysis."
    # document5 = "Computer vision is a field of study that enables computers to interpret and make decisions based on visual data, often using image and video processing techniques."
    # document6 = "The Internet of Things (IoT) connects devices and enables them to communicate and share data, leading to smart and interconnected systems."
    # document7 = "Cybersecurity is the practice of protecting computer systems, networks, and data from unauthorized access, attacks, and damage."

    # # Creating Document instances
    # doc_list = [Document(document1), Document(document2), Document(document3),
    #             Document(document4), Document(document5), Document(document6), Document(document7)]

    folder_path = "Corpus"  

    # List all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()
                    doc_list.append(Document(file_content))
            except FileNotFoundError:
                print(f"File not found: {file_path}")




    all_tokens.sort()


    for document in doc_list:
        document.term_count = {token: document.tokens.count(token) for token in all_tokens}
        document.TF = {token: (document.term_count[token]/len(document.tokens)) for token in all_tokens}


def cos_sim(doc1 , doc2 ):

    A = np.array(list(doc1.values()))
    B = np.array(list(doc2.values()))

    # compute cosine similarity
    cosine = np.dot(A,B)/(norm(A)*norm(B))
    
    return cosine

def compare(text):
    global doc_list
    global all_tokens
    input_tokens = preprocess_text_spacy(text)
    all_tokens = list(set(all_tokens + input_tokens))
    init()
    input_term_count = {token: input_tokens.count(token) for token in all_tokens}
    input_TF = {token: (input_term_count[token]/len(input_tokens)) for token in all_tokens}
    max = 0
    max_doc = Document
    for doc in doc_list:
        doc.cos_sim = cos_sim(input_TF,doc.TF)
        if max <=  doc.cos_sim:
            max = doc.cos_sim
            max_doc = doc
    
    return max_doc
        



import tkinter as tk
from tkinter import scrolledtext

def perform_search():
    query = entry.get()
    query = compare(query)
    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)  # Clear existing text
    result_text.insert(tk.END, f"Search Result: \n{query.original_text}")
    result_text.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Search UI")
root.geometry("1000x500")  # Set the initial size of the window

# Create and place widgets with additional styling
label = tk.Label(root, text="Enter search query:", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=10)

search_button = tk.Button(root, text="Search", command=perform_search, font=("Arial", 12), bg="blue", fg="white")
search_button.pack(pady=10)

# Create a scrolled text widget
result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=10, font=("Arial", 14))
result_text.pack(pady=10)

# Disable text editing in the result_text
result_text.config(state=tk.DISABLED)

root.mainloop()

# init()

# selected_tokens = all_tokens[-20:]

# # Create and display tables side by side

# # Create a combined table
# combined_table = PrettyTable()
# combined_table.field_names = ["Document"] + selected_tokens

# for i, document in enumerate(doc_list):
#     row_data = [f"Doc {i + 1}"] + [document.term_count[token] for token in selected_tokens]
#     combined_table.add_row(row_data)

# print(combined_table)
