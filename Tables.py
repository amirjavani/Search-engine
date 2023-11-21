import spacy
import os
import re
from prettytable import PrettyTable

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








init()

selected_tokens = all_tokens[-20:]

# Create and display tables side by side

# Create a combined table
combined_table = PrettyTable()
combined_table.field_names = ["Document"] + selected_tokens

for i, document in enumerate(doc_list):
    row_data = [f"Doc {i + 1}"] + [document.term_count[token] for token in selected_tokens]
    combined_table.add_row(row_data)

print(combined_table)
