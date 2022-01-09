import pkg_resources
from symspellpy import SymSpell, Verbosity
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import spacy
import logging as logger
logger.basicConfig(level=print)

class NLPCharades:
    def __init__(self):
        try:
            self.THERSHOLD = 0.7
            print("Initializing NLPCharades")

            print("Loading spacy model")
            self.nlp = spacy.load("en_core_web_sm")
            print("Loaded spacy model")

            print("Loading SymSpell")
            self.sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
            dictionary_path = "symspellpy_lookup_dictionary/frequency_dictionary_en_82_765.txt"

            # term_index is the column of the term and count_index is the
            # column of the term frequency
            self.sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)
            print("Loaded SymSpell")

        except Exception as e:
            print("Exception in NLPCharades.__init__: {}".format(e))
        
    def predict(self, obsecured_word, description):
        try:
            # lookup suggestions for single-word input strings
            input_term = obsecured_word 
            # max edit distance per lookup
            # (max_edit_distance_lookup <= max_dictionary_edit_distance)
            suggestions = self.sym_spell.lookup(input_term, Verbosity.CLOSEST, max_edit_distance=2)
            # display suggestion term, term frequency, and edit distance
            word = "" 
            for suggestion in suggestions:
                word = suggestion
            else:
                word = "unknown"

            print("Word: {}".format(word))

            word = "debate"

            doc_vec = self.nlp(description).vector.reshape(1,-1)
            word_vec = self.nlp(word).vector.reshape(1,-1)

            cos_sim = cosine_similarity(doc_vec, word_vec)[0][0]
            print("Cosine similarity between {} and {} is {}".format(description, word, cos_sim))

            if cos_sim > self.THERSHOLD and word != "unknown":
                pred_val = word
            else:
                pred_val = obsecured_word
        except Exception as e:
            logger.error("Exception in NLPCharades.predict: {}".format(e))
            pred_val = obsecured_word
            
        return pred_val


if __name__ == "__main__":
    nlpcharades = NLPCharades()

    obsecured_word = "d bat "
    description = "a discussion in which reasons are advanced for and against some proposition or proposal"
    print(nlpcharades.predict(obsecured_word, description))