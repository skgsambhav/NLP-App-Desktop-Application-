import paralleldots

class Api():
    def __init__(self):
        paralleldots.set_api_key( "uNhHorgfE3Ak28Aln6DDGwBJeZCjNNq8tKniNNVCqZo" )

    def sentiment_analysis(self,text):
        return paralleldots.sentiment(text)

    def emotion_analysis(self,text):
        return paralleldots.emotion(text)

    def abuse_analysis(self,text):
        return paralleldots.abuse(text)

    def name_entity_finder(self,text):
        response =  paralleldots.ner(text)
        for i in response['entities']:
            txt = ""
            for key, value in i.items():
                txt = txt + (str(key) + " --> " + str(value) + "\n")
            return txt

