import os

folder_path = "C:\\dars\\term 7\\NLP\\second project\\Corpus"  # Replace with the actual path to your folder
list_of_strings = []

# List all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
                list_of_strings.append(file_content)
        except FileNotFoundError:
            print(f"File not found: {file_path}")

# Now, list_of_strings contains the content of each text file in the folder as a string



