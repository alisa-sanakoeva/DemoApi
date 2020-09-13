from flask_restful import Resource, reqparse
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.probability import FreqDist
from flask import jsonify
import spacy

class TemSentenceTokenizer(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('sentence',
                        type=str,
                        required=True,
                        help="გთხოვთ შეიყვანოთ სწორი წინადადება")

    def get(self):
        data = TemSentenceTokenizer.parser.parse_args()
        sentence = data['sentence']
        try:
            tokenized_words = word_tokenize(sentence)

        except Exception as error:
            print(f'error: {error}')
            return jsonify({'error': f"დაფიქსირდა შეცდომა: {error}"}), 400

        else:
            return jsonify({'result': tokenized_words}), 200

class FrequencyDistribution(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('text',
                        type=str,
                        required=True,
                        help="გთხოვთ შეიყვანოთ სწორი ტექსტი")

    def get (self):
        data = FrequencyDistribution.parser.parse_args()
        text = data['text']
        clean_text=word_tokenize(text)
        freqdist=FreqDist(clean_text)



        return {'result': freqdist}


class SentenceTokenizer(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('sentence',
                        type=str,
                        required=True,
                        help="გთხოვთ შეიყვანოთ სწორი წინადადება")

    def get(self):
        data = SentenceTokenizer.parser.parse_args()
        sentence = data['sentence']
        try:


            tokenized_words = sent_tokenize(sentence)

        except Exception as error:
            return {'error' : error}

        else:
            return {'result': tokenized_words}, 200


class DepTreeSvgMaker(Resource):

	parser = reqparse.RequestParser()
	parser.add_argument("sentence",
						type=str,
						required=True,
						help="გთხოვთ შეიყვანოთ სწორი წინადადება")

	nlp = spacy.load("en_core_web_sm")

	def get(self):
		data = self.parser.parse_args()
		sentence = data["sentence"]

		try:
			text = self.nlp(sentence)
			svg = spacy.displacy.render(text,style="dep")

		except Exception as error:
			return {'error' : error}

		return jsonify({'result': svg})

