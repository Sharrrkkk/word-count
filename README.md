# **Word Count**
About
A static web interface for uploading a file, a backend in python flask,
result: a counter of lines, words, characters, bytes, of the file uploaded
to the website, delivers the same result as the wc command in unix-like
systems (gnu-linux, mac)



## **LICENSE**
This project is licensed under the MIT License.

## **Notes**
This project is intended 100% for educational purposes.


## **Project Structure**
```
.
├── LICENSE
├── README.md
├── app.py
├── backend
│   ├── __init__.py
│   ├── blueprints
│   │   ├── __init__.py
│   │   ├── api
│   │   │   ├── __init__.py
│   │   │   ├── api.py
│   │   │   └── test
│   │   │       └── test.txt
│   │   ├── embedded
│   │   │   ├── __init__.py
│   │   │   ├── embedded.py
│   │   │   ├── templates
│   │   │   │   └── word_count_embedded.html
│   │   │   └── test
│   │   │       └── test.txt
│   │   └── home
│   │       ├── __init__.py
│   │       ├── home.py
│   │       ├── templates
│   │       │   └── word_count_home.html
│   │       └── test
│   │           └── test.txt
│   └── word_count
│       ├── __init__.py
│       ├── test
│       │   ├── spencer.jpg
│       │   └── test.txt
│       └── wc.py
├── index.html
├── requirements.txt
├── scripts
│   └── main.js
├── styles
│   └── style.css
└── test
    └── test.py    
```