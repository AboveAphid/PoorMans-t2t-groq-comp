# Poor Man's Groq T2T Component

## What is this for?
*Start your poor man's journey of free T2T apis for JAISON!*

You tired of OpenAI's ***evil*** pricing of a couple cents per request??

***Well no more I tell you!*** 

With Groq's free, fresh, and *slightly outdated models* we can get a free T2T api
that doesn't need to take up all your non-existent processing power!

You can visit Groq's docs here: 
https://console.groq.com/docs/overview

> [!NOTE]
> Keep in mind Groq does not support finetuning models like OpenAI

## Setup

Windows
```
conda create -n jaison-comp-t2t-groq-api python=3.12
conda activate jaison-comp-t2t-groq-api
pip install -r requirements.txt
```

Unix
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Furthermore, create a `.env` file in the root of this project with the following:
```
GROQ_API_KEY=<groq api key like gsk_...>
MODEL=<name of model like llama3-8b-8192>
```
> [!TIP]
> You can see other groq models here: https://console.groq.com/docs/models

## Testing
You better be in the right virtual environment and in the root directory!
Then we can test!
```
python ./src/main.py --port=5000
```
If it runs, *everything should be swell*!

## Configuration
Check Setup for what you need in your .env!

## Related stuff
Project J.A.I.son: https://github.com/limitcantcode/jaison-core
Join the community Discord: https://discord.gg/Z8yyEzHsYM

*Other Poor Man plugins/components coming soon!*
