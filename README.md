# obscured-character-detect
simple deep learning model in python to identify the correct word from the obscured input and description


## Dataset:
1. Dictinary words with description: https://www.kaggle.com/tybens/sentiment-analysis-and-rating-correlation

## symspellpy installation:
1. python -m pip install -U symspellpy
2. Download Symspell Lookup Dictionary: 

* curl -LJO https://raw.githubusercontent.com/mammothb/symspellpy/master/symspellpy/frequency_dictionary_en_82_765.txt

* curl -LJO https://raw.githubusercontent.com/mammothb/symspellpy/master/symspellpy/frequency_bigramdictionary_en_243_342.txt


## pretrained language model
1. install spacy: pip install spacy
2. download Model: python -m spacy download en_core_web_sm


Reference
1. To download spacy model: https://spacy.io/usage/models
2. Symspell implementation: https://symspellpy.readthedocs.io/en/latest/examples/lookup.html#basic-usage
3. Symspell lookup dictionary download: https://symspellpy.readthedocs.io/en/latest/users/installing.html