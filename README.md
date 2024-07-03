# First create a virtual environment

```bash
python3 -m venv .venv
```

## and activate it

```bash
source .venv/bin/activate
```

# Install Dependencies

```bash
pip3 install flask
```

```bash
pip3 install requests
```

## Additionally you can output the dependencies to a text file

```bash
pip3 freeze > requirements.txt
```

Whenever you add a new dependencie you should do this so that anyone working with it can have them

# Running Flask

```bash
python3 app.py
```

# Showcase Flask

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def greetings():
    return "Hey there!"

if __name__ == '__main__':
    app.run(debug=True)
```