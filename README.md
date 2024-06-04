# Summer school project

## Setup

```bash
# clone repo
git clone https://github.com/linomp/playlist-gen

# create virtual environment & install requirements
python -m venv venv
pip install -r requirements.txt
```

Then create an .env file with the follwoing API keys:

```
OPENAI_API_KEY=....
```

## Usage

```bash
# activate virtual environment
source venv/Scripts/activate

# run script, for example the image caption demo:
python img-caption.py
```
