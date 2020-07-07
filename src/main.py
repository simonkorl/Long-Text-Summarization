import nltk
import glob
import re
import jieba
from leadk import lead1
import rouge
from zhon import hanzi
import numpy as np
from tfidf import tfidf
from textrank import textrank
from datasets import ChineseAbstractiveCorpus, NLPCC2017, DataLoader


def main():
    r1s = []
    r2s = []
    rls = []
    rouge_eval = rouge.Rouge()
    dataset = NLPCC2017()
    loader = DataLoader(dataset)
    for text, gt_sum in loader:
        pred_sum = lead1(text)
        # pred_sum = tfidf(text)
        # pred_sum = textrank(text)
        pred_list = re.findall(f'[{hanzi.characters}]', pred_sum)
        gt_list = re.findall(f'[{hanzi.characters}]', gt_sum)
        pred_sum = " ".join(pred_list)
        gt_sum = " ".join(gt_list)
        if not (pred_sum and gt_sum):
            continue
        scores, = rouge_eval.get_scores(pred_sum, gt_sum)
        rouge1 = scores["rouge-1"]["f"]
        rouge2 = scores["rouge-2"]["f"]
        rougel = scores["rouge-l"]["f"]
        r1s.append(rouge1)
        r2s.append(rouge2)
        rls.append(rougel)
        # print(f"{rouge1} {rouge2} {rougel}")
    # import ipdb; ipdb.set_trace()
    print(f"R1 {np.mean(r1s)}, R2 {np.mean(r2s)}, RL {np.mean(rls)}")


if __name__ == "__main__":
    main()
