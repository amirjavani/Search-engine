# Search-engine
A search engine using NLP (lem , stop word , vectorization , etc) 

Search engine

Using this pre-processing technique can improve the quality of the text:

- Removing punctuation marks

- Stop word removal

- Tokenization

- Lemmatization

After extracting all the tokens that we need, we vectorize each of them.
![Screenshot 2023-11-21 104556](https://github.com/amirjavani/Search-engine/assets/87892692/2a9ab080-31d6-406f-9096-dbf274103c1f)

We are utilizing Term-frequency
![Screenshot 2023-11-21 104634](https://github.com/amirjavani/Search-engine/assets/87892692/d28df786-6959-4d35-bef4-750d15ea49f2)
![Screenshot 2023-11-21 104650](https://github.com/amirjavani/Search-engine/assets/87892692/3cb3c9fc-d83e-4686-9b49-8c30aacb0767)

And in the end, we calculate the cosine similarity of the documents and compare it with the input of the search, and the most closely related document will be displayed in the text box.
![Screenshot 2023-11-21 104752](https://github.com/amirjavani/Search-engine/assets/87892692/be45aec4-f4f1-4a53-bf7d-34fdfdfab131)
![Screenshot 2023-11-21 104731](https://github.com/amirjavani/Search-engine/assets/87892692/a0d265e5-009e-4e41-801e-89c3db431262)
  
Search.py is for searching, and Tables.py shwoing vectorizetion before calculating term frequency.


