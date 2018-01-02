# coding=utf-8
import ner_core
import utils

sentence = """5/08/2016 The first Indonesian Youtube video to hit 100 million
views was a music video published in October 2016. It is from a major music label, but clips from self-made Youtube stars
like Reza Oktovian from Jakarta and Agung Hapsah from Samarinda have also been seen by millions. Developing countries in Asia-Pacific are
expected to contribute significantly to the growth of online video globally, as mobile broadband becomes ubiquitous.
Where people are paying attention, there are others wanting to divert some of it to their benefit. Marketers now
think there is a way to increase the number of people buying products right after seeing them in an online clip –
with shoppable videos. They let you click on something you see in the video – say you like the dress someone’s
wearing. A pop-up window with product information opens and you can buy it on the spot. In May, Instagram began
testing shoppable videos with some brands, apparently with encouraging results in February 2018."""


if __name__ == '__main__':
    ner = ner_core.NerCore(sentence)

    names = ner.extract_names("eng")
    locations = ner.extract_location("eng")
    dates = ner.extract_date_time()

    print("==============================")
    print("Result data extract (English)")
    print("========================")
    print("Name")
    print("====================")
    utils.get_result(names)

    print
    print("========================")
    print("Location")
    print("====================")
    utils.get_result(locations)

    print
    print("========================")
    print("Date time")
    print("====================")
    utils.get_result(dates)


