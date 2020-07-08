import re
import os
import json
from leadk import lead1
import numpy as np
from tfidf import tfidf
from textrank import textrank
from datasets import DataLoader, chinese_abstractive_corpus, nlpcc2017, voice_recorder


def main():
    dataset = voice_recorder
    loader = DataLoader(dataset)
    save_dir = "../outputs/results/"
    os.makedirs(save_dir, exist_ok=True)

    for basename, text, _ in loader:
        # pred_sum = lead1(text)
        # pred_sum = tfidf(text)
        pred_sum = textrank(text)
        with open(os.path.join(save_dir, basename), "w", encoding="utf-8") as f:
            json.dump({"summary": pred_sum}, f, ensure_ascii=False)


if __name__ == "__main__":
    main()
