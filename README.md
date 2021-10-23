# Wishful Thinking

Text analysis for similar book recommendations and automatic genre
determination
- Unsupervised machine learning

## Data obtention
Project Gutenberg data list was obtained by running
`wget -w 2 -m http://www.gutenberg.org/robot/harvest?filetypes[]=txt&langs[]=en`
and `cat www.gutenberg.org/robot/* | urlscan -d -n > urls`
Then, `mkdir zip && cd zip && xargs -P 100 wget <urls` gives the zipped
text files in `zip/` as we're using in our text analysis scripts.

License for our original code is Affero GPL.
We make no such warranty about the license for data used by this
program, like the Project Gutenberg corpus.

## Setup

- Download the Gutenberg files as described above
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 analyze.py
deactivate
```
