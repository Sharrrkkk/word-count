# File Analyzer Web App

A simple web application that analyzes a file and reports the number of
lines, words, characters, and bytes it contains.

The application works directly from the browser: users select a file,
send it to the backend, and receive the analysis results instantly.
It supports UTF-8 text files and binary files.

---

## Overview

This project is a small but complete web application composed of:

- A **backend service** built with Flask
- A **frontend** hosted on GitHub Pages using vanilla HTML, CSS, and JavaScript

The backend performs file analysis similar in spirit to the Unix `wc` tool,
while the frontend provides an accessible web-based interface.

The application supports two response modes:
- **API mode** (JSON response)
- **Embedded mode** (HTML fragment response)

---

## What does it do?

Given a file uploaded from the browser, the backend analyzes it and returns:

- Number of lines
- Number of words (UTF-8 text files only)
- Number of characters (UTF-8 text files only)
- Number of bytes

For non-UTF-8 or binary files, the application still reports:
- Lines
- Bytes

---

## Use cases

- Quickly checking word counts for documents with strict limits
- Inspecting file size and structure
- Learning and experimenting with file handling in web applications
- Educational purposes (Flask, file uploads, frontend-backend interaction)

---

## Tech Stack

### Backend
- **Python**
- **Flask**
- **Flask-CORS** (to allow cross-origin requests)
- **Pytest** (doctests automated via test suite)

### Frontend
- HTML
- CSS
- Vanilla JavaScript
- Fetch API
- Manual DOM manipulation

No database, authentication, or persistent storage is used.

---

## Architecture

The backend follows a **Model–View–Presenter (MVP)**-style organization,
with a clear separation of responsibilities and modular design.

Flask **blueprints** are used to isolate different routes and behaviors,
making the codebase easier to reason about and extend.

---


## Project Structure

```text
.
├── app.py
├── backend
│   ├── blueprints
│   │   ├── api
│   │   ├── embedded
│   │   └── home
│   └── word_count
├── index.html
├── scripts
│   └── main.js
├── styles
│   └── style.css
├── requirements.txt
├── test
│   └── test.py
├── README
└── LICENSE
```

## Key directories

### backend/word_count/
- Core file analysis logic.

### backend/blueprints/
Flask blueprints, separated by responsibility:

- API responses

- Embedded HTML responses

- Home route

### scripts/main.js
Frontend logic using fetch and DOM manipulation.


## How it works

1. The user opens the frontend in the browser.

2. A file is selected using an <input type="file">.

3. The file is sent to the backend using fetch.

4. The backend analyzes the file contents.

5. The response is returned in one of two modes:
- API mode: JSON data, parsed and rendered by JavaScript.
- Embedded mode: HTML fragment inserted directly into the DOM.


## API vs Embedded Mode
### API Mode

- Backend returns a JSON response.
- Frontend updates the UI by manually manipulating DOM elements.

### Embedded Mode

- Backend returns a rendered HTML fragment.
- Frontend injects the fragment directly into the page using innerHTML.

Both modes are explicitly selectable from the frontend UI.


## Local Execution
The application can be executed locally in different modes depending on how you want to interact with it.

### Backend (Flask server)
The backend is configured to run on:

- Host: localhost
- Port: 5000

Start the backend server with:
```bash
python3 app.py
```
Or
```bash
flask run
```
Once running, the backend exposes multiple routes.

### Home Mode (SSR)
By default, accessing:

> http://localhost:5000

activates Home Mode.

In this mode:
- The frontend is server-side rendered (SSR) using Flask templates.
- No separate frontend server is required.
- The entire interface is rendered directly by the backend.

This is the simplest way to use the application locally.

### API and Embedded Modes (Frontend + Backend)
To use API mode or Embedded mode, the frontend must be served separately.

These modes rely on:

- A static frontend (HTML, CSS, JS)
- Requests made via fetch to the Flask backend
- Cross-origin communication (handled via CORS)

Start a local frontend server
From the project root, run:
```bash
python3 -m http.server 8080
```

This starts a simple static server.

Now access the frontend at:

> http://localhost:8080

From there:
- API and Embedded modes are fully available
The frontend communicates with the backend running on 
> http://localhost:5000


### Summary of modes

| Mode        | URL               | Frontend source    | Notes                              |
|-------------|-------------------|--------------------|------------------------------------|
| Home (SSR)  | `localhost:5000`  | Backend template   | No frontend server needed          |
| API         | `localhost:8080`  | Static frontend    | JSON response + DOM updates        |
| Embedded    | `localhost:8080`  | Static frontend    | HTML fragment injection            |


## Design decisions

- No database or authentication to keep the project focused and simple.

- Flask blueprints used for clarity and modularity.

- Explicit routes and minimal abstractions.

- Manual DOM manipulation instead of frontend frameworks.


## License
This project is licensed under the MIT License.