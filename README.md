# Summer school project

## Setup

```bash
# clone repo
git clone https://github.com/VIVES-project/playlist-gen

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
python imgCaption.py
```

## Start streamlit UI

```bash
# activate virtual environment
source venv/Scripts/activate

streamlit run st-example.py
```

The first time, activate the "run on save" option here:

![immagine](https://github.com/VIVES-project/playlist-gen/assets/40581019/d7085403-7c85-4871-8684-d2441259bf3f)

You can also edit the visual theme there.
