from summarizer import Summarizer
model = Summarizer()

class TextSummarizerPredictor:
    def textSumamryPredictor(body):
        result = model(body)
        full = ''.join(result)
        return full
# result = model(body)
# full = ''.join(result)
# print(full)