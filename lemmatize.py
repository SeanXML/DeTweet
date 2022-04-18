# pip install simplemma
import simplemma
langdata = simplemma.load_data('de')

def lemmatize(tokens_list):
    # Input your list of tokens
    lem_token = []
    for token in tokens_list:
        lem_token.append(simplemma.lemmatize(token, langdata))
    return lem_token