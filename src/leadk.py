import re


def leadk(text, k):
    segments = text.split('\n')
    pred_sum = []
    for seg in segments:
        sents = re.split(r"。", seg)
        pred_sum += sents[:k]
    pred_sum = "。".join(pred_sum) + "。"
    return pred_sum


def lead1(text):
    return leadk(text, k=1)
