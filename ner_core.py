import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk import pos_tag
from nltk import ne_chunk
from nltk import tree
from geotext import GeoText


class NerCore:
    def __init__(self, sentence):
        self.sentence = sentence

    def __preprocessing(self, lang):
        sentences = sent_tokenize(self.sentence)
        sentences = [word_tokenize(sent) for sent in sentences]
        sentences = [pos_tag(sent, lang=lang) for sent in sentences]
        return sentences

    def extract_names(self, lang):
        names = []
        sentences = self.__preprocessing(lang)
        for tagged_sentence in sentences:
            for chunk in ne_chunk(tagged_sentence):
                if isinstance(chunk, tree.Tree):
                    if chunk.label() == 'PERSON':
                        names.append(' '.join([c[0] for c in chunk]))
        return names

    def extract_location(self, lang):
        locations = []
        sentences = self.__preprocessing(lang)
        for tagged_sentence in sentences:
            for chunk in ne_chunk(tagged_sentence):
                if isinstance(chunk, tree.Tree):
                    if chunk.label == 'LOCATION':
                        locations.append(' '.join([c[0] for c in chunk]))

        cities = GeoText(self.sentence).cities
        for city in cities:
            locations.append(''.join([c[0] for c in city]))
        nationalities = GeoText(self.sentence).nationalities
        for national in nationalities:
            locations.append(''.join([n[0] for n in national]))
        countries = GeoText(self.sentence).countries
        for country in countries:
            locations.append(''.join([c[0] for c in country]))
        return locations

    def extract_date_time(self):
        dateTimes = []
        grammar = r"DATE: {<NNP><CD>}"
        parser = nltk.RegexpParser(grammar)

        phrase_tagger = nltk.pos_tag(word_tokenize(self.sentence))
        phrase_chunk = nltk.ne_chunk(phrase_tagger)

        phrase_date = parser.parse(phrase_chunk)
        for word in phrase_date:
            if isinstance(word, nltk.tree.Tree) and word.label() == 'DATE':
                dateTimes.append(' '.join([w[0] for w in word]))
        return dateTimes
