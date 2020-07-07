from jieba import analyse
from zhon import hanzi
import re


def tfidf(text):
    sents = re.split(f"[。]+", text)
    scores = []
    for sent in sents:
        sent = re.sub(f'[^{hanzi.characters}]+', ' ', sent)
        keywords = analyse.tfidf(sent, withWeight=True)
        score = sum([s for _, s in keywords]) # / len(keywords)
        scores.append(score)

    assert len(scores) == len(sents)
    thresh = sum(scores) / len(scores)
    selected_sents = [sent for score, sent in zip(scores, sents) if score > thresh]
    summary = "，".join(selected_sents) + "。"
    return summary
