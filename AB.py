list_ = []

class Substitute(object):
    def getValue(self, key, code):

        global var
        result = ""
        k = 0

        for i in key:
            list_.append(i)

        for alphabet in code:
            for i, j in enumerate(list_):
                if j == alphabet:
                    result += str((i+1)%10)
        return int(result)


mysys = Substitute()
print mysys.getValue("TRADINGFEW", "LGXWEV")
