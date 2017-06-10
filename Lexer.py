class Lexer(object):
    def tokenize(self, tokens, inp):
        consume = []

        while len(inp) > 0:
            long_token = ""
            i = 0
            for token in tokens:
                length = len(token)
                if inp[:length] != token:
                    i += 1
                    inp = inp[i:]
                elif token == inp[:length] and length > len(long_token):
                    long_token = token
            inp = inp[len(long_token):]
            consume.append(long_token)
        return consume
