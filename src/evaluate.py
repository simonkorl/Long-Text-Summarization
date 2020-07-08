import rouge
from datasets import DataLoader, chinese_abstractive_corpus, nlpcc2017, voice_recorder
import os
import json
import re
from zhon import hanzi
import numpy as np


def main():
    r1s = []
    r2s = []
    rls = []
    rouge_eval = rouge.Rouge()
    dataset = voice_recorder
    loader = DataLoader(dataset)
    save_dir = "../outputs/results/"
    os.makedirs(save_dir, exist_ok=True)

    for basename, _, gt_sum in loader:
        if not os.path.isfile(os.path.join(save_dir, basename)):
            continue
        with open(os.path.join(save_dir, basename), encoding="utf-8") as f:
            data = json.load(f)
        pred_sum = data["summary"]

        pred_list = re.findall(f'[{hanzi.characters}]', pred_sum)
        gt_list = re.findall(f'[{hanzi.characters}]', gt_sum)
        pred_sum = " ".join(pred_list)
        gt_sum = " ".join(gt_list)

        scores, = rouge_eval.get_scores(pred_sum, gt_sum)
        rouge1 = scores["rouge-1"]["f"]
        rouge2 = scores["rouge-2"]["f"]
        rougel = scores["rouge-l"]["f"]
        r1s.append(rouge1)
        r2s.append(rouge2)
        rls.append(rougel)
        print(f"{rouge1}, {rouge2}, {rougel}")

    print(f"Avg: R1 {np.mean(r1s)}, R2 {np.mean(r2s)}, RL {np.mean(rls)}")


if __name__ == "__main__":
    main()
