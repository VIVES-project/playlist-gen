# Summer school project

## Setup

```bash
# clone repo
git clone https://github.com/linomp/playlist-gen

# create virtual environment
python -m venv venv

# activate virtual environment
source venv/Scripts/activate

# install requirements
pip install -r requirements.txt
```

Then create an .env file with the follwoing API keys:

```
OPENAI_API_KEY=....
SPOTIFY_CLIENT_ID=...
SPOTIFY_CLIENT_SECRET=...
```

## Usage

```bash
# activate virtual environment
source venv/Scripts/activate

# run script, for example the image caption demo:
python img-caption.py
```
