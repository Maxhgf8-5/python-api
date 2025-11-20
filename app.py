from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)
nlp = spacy.load("fr_core_news_md")  # modèle français

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    message = data.get('message', '')

    doc = nlp(message)
    keywords = [token.lemma_ for token in doc if token.pos_ in ['NOUN', 'VERB', 'PROPN']] 

    return jsonify({'keywords': keywords})

if __name__ == '__main__':
    app.run(port=5000)
