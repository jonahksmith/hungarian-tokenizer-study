def fertility(text, tokenize):
    """ average number of tokens per work """
    words = text.split()
    tokens = tokenize(text)
    return len(tokens) / len(words)