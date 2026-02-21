# In nutshell, here also we are using the same technique called Recursive Character Text 
# Splitter to split the text into smaller chunks. The only difference is that we are using a 
# different text as input means the code file or the markdown files like for that reason you 
# can use the document strcutre based text splitter.

#  You can call this as the Markdown Text Splitter

from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
# Project Name: Smart Student Tracker

A simple Python-based project to manage and track student data, including their grades, age, and academic status.


## Features

- Add new students with relevant info
- View student details
- Check if a student is passing
- Easily extendable class-based design


## 🛠 Tech Stack

- Python 3.10+
- No external dependencies


## Getting Started

1. Clone the repo  
   ```bash
   git clone https://github.com/your-username/student-tracker.git

"""
# The only thing you need to ass from_language then tell which language is going to use in the text here we used the PYTHON that's why we use this 

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=400,
    chunk_overlap=0,
)

chunk = splitter.split_text(text)

print(len(chunk))
print(chunk[0])