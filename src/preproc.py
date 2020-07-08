import glob
import json
import re
import os
import pandas as pd


def save_data(path, text, gt_sum):
    data = {
        "summary": gt_sum,
        "text": text
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)


def process_chinese_abstractive_corpus():
    save_dir = "../inputs/chinese_abstractive_corpus/"
    os.makedirs(save_dir, exist_ok=True)

    paths = glob.glob("../data/chinese_abstractive_corpus/copus/*.txt")
    for path in paths:
        with open(path, encoding="utf-8") as f:
            raw_sum, raw_text = f.read().split("\n")
            gt_sum, = re.findall(r"summary\{\{(.*)\}\}", raw_sum)
            text, = re.findall(r"text\{\{(.*)\}\}", raw_text)
            basename, _ = os.path.splitext(os.path.basename(path))
            save_data(os.path.join(save_dir, f"{basename}.json"), text, gt_sum)


def process_nlpcc2017():
    save_dir = "../inputs/nlpcc2017/"
    os.makedirs(save_dir, exist_ok=True)

    data_file = "../data/nlpcc2017textsummarization/train_with_summ.txt"
    with open(data_file, encoding="utf-8") as f:
        lines = f.readlines()

    for line_idx, line in enumerate(lines):
        data = json.loads(line)
        text = data["article"]
        gt_sum = data["summarization"]
        save_data(os.path.join(save_dir, f"{line_idx}.json"), text, gt_sum)


def process_voice_recorder():
    save_dir = "../inputs/voice_recorder/"
    os.makedirs(save_dir, exist_ok=True)

    paths = glob.glob("../data/voice_recoder/*.xlsx")
    for path in paths:
        df = pd.read_excel(path)
        table = df.values
        text = '\n'.join([x[0] for x in table])
        ext_sum = '\n'.join([x[-2] for x in table]) # extractive summary
        abs_sum = '\n'.join([x[-1] for x in table]) # abstractive summary
        gt_sum = abs_sum
        basename, _ = os.path.splitext(os.path.basename(path))
        save_data(os.path.join(save_dir, f"{basename}.json"), text, gt_sum)


def main():
    # process_chinese_abstractive_corpus()
    # process_nlpcc2017()
    process_voice_recorder()


if __name__ == "__main__":
    main()
