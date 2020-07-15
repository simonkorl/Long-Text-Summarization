from jieba import analyse
import re
from zhon import hanzi
import textrank4zh


def textrank(text):
    tr4s = textrank4zh.TextRank4Sentence()
    tr4s.analyze(text=text, lower=True, source='no_stop_words')
    SELECT_TOPK = len(text.split("\n")) # number of paragraphs
    selected_sents = tr4s.key_sentences[:SELECT_TOPK]
    selected_sents = sorted(selected_sents, key=lambda x: x['index'])
    selected_sents = [sent['sentence'] for sent in selected_sents]
    summary = "，".join(selected_sents) + "。"
    return summary
