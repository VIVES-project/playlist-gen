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

Then create an .env file with the following API keys:

```
OPENAI_API_KEY=....
SPOTIFY_CLIENT_ID=...
SPOTIFY_CLIENT_SECRET=...
```

If you're part of the VIVES project team, you can download the `.env` file directly from our shared google drive folder and paste it in the project's root directory. It should be ignored by git (always double check that)!
<details>
<summary>
  (optional) Create your own API key and client secrets.
</summary>

Check [this tutorial](https://platform.openai.com/docs/quickstart) for setting up your OpenAI API key, and [this one](https://developer.spotify.com/documentation/web-api/tutorials/getting-started) for the spotify client id and client secret.

**Important**: you will also need to add specific user accounts to this list, to be able to interact with the app in development mode:

<img src="https://github.com/VIVES-project/playlist-gen/assets/40581019/da83fc79-2958-49c8-8815-62f584f55595" width="70%"/>

</details>

## Usage

```bash
# activate virtual environment
source venv/Scripts/activate

# run script, for example the image caption demo:
python imgCaption.py
```

### Start streamlit UI

```bash
# activate virtual environment
source venv/Scripts/activate

streamlit run st-example.py
```

The first time, activate the "run on save" option here:

![immagine](https://github.com/VIVES-project/playlist-gen/assets/40581019/d7085403-7c85-4871-8684-d2441259bf3f)

You can also edit the visual theme there.
