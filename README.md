This script downloades phrases/sententences/song lines from Twitter and azlyrics.com by Nicki Minaj. The script
only takes ~8 min and gets ~6000 rows of data.


### 1. How to start:

Clone the repository and go to it on the command line:

```
https://github.com/Jakondak/mynalabs_task
```

```
cd mynalabs_task
```

Create and activate the virtual environment:

```
python3 -m venv env
```

```
source venv/bin/activate
```

Install dependencies from the requirements.txt file:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Run start.py file:

```
python3 start.py
```

### 2. How data is downloaded:

A) Twitter:

1) Description: I decided to use html scrapper by reason of that I was not given access to the
Twitter's API. I used a library snscrape for this purposes.

2) Processing: deleted short tweets, emojis

3) Good & bad examples: 
  3.1) Good: 
- 'As I sit back, relax, crack jokes for a minute'. It seems to be a telling
example, as Nicki Minaj says.
  3.2) Bad:
- 'Who’s team you on for this reunion? Lmk rq #Rhop b4 I spk'. 
   Hashtags are unnecessary parts.

B) Lyrics from azlyrics.com:

1) Description: I used BeautifulSoup for parsing azlyrics.com link. I found
list of her songs, chose the ones without other performers (without any 'feat'.
I have to find only her phrases) and downloaded lyrics from html file.

3) Processing: deleted short sentences, got rid of 'feats'

4) Good & bad examples:
  3.2) Bad:
- Lines of songs with a lot of repetition


### 3. What else can be used:

Steps:
1) Take pretrained voicefilter model(https://github.com/mindslab-ai/voicefilter).
This model can recognize a certain speaker from an audio. Also it trained on the
dataset where there is the voice of Nicki Minaj
(https://www.robots.ox.ac.uk/~vgg/data/voxceleb/vox1.html). 
2) After I have to download audios from YouTube interviews with Nicki.
3) And determine the marks where the voice of the Nicki is and where it is not 
using the model
4) At the end of take the voice-to-text model (https://github.com/NVIDIA/NeMo) and get Niki's answers on questions
