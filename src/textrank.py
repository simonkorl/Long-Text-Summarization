from jieba import analyse
import re
from zhon import hanzi
import textrank4zh


def textrank(text):
    tr4s = textrank4zh.TextRank4Sentence()
    tr4s.analyze(text=text, lower=True, source = 'no_stop_words')
    SELECT_TOPK = 1
    selected_sents = [sent['sentence'] for sent in tr4s.key_sentences[:SELECT_TOPK]]
    summary = "，".join(selected_sents) + "。"
    return summary
