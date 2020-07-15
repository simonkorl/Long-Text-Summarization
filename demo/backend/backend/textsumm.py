import re

import textrank4zh
from jieba import analyse
from zhon import hanzi


def textrank(text):
    tr4s = textrank4zh.TextRank4Sentence()
    tr4s.analyze(text=text, lower=True, source='no_stop_words')
    select_topk = len(text.split("\n"))  # number of paragraphs
    selected_sents = tr4s.key_sentences[:select_topk]
    selected_sents = sorted(selected_sents, key=lambda x: x['index'])
    selected_sents = [sent['sentence'] for sent in selected_sents]
    summary = "，".join(selected_sents) + "。"
    return summary


def tfidf(text):
    sents = re.split(r"[。]+", text)
    scores = []
    for sent in sents:
        sent = re.sub(f'[^{hanzi.characters}]+', ' ', sent)
        keywords = analyse.tfidf(sent, withWeight=True)
        score = sum([s for _, s in keywords])  # / len(keywords)
        scores.append(score)

    assert len(scores) == len(sents)
    thresh = sum(scores) / len(scores)
    selected_sents = [sent for score, sent in zip(scores, sents) if score > thresh]
    summary = "，".join(selected_sents) + "。"
    return summary


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
