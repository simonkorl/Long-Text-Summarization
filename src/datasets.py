import glob
import os
import re
import json


class ChineseAbstractiveCorpus(object):
    def __init__(self):
        self.text_files = glob.glob("../data/chinese_abstractive_corpus/copus/*.txt")

    def __getitem__(self, index):
        text_file = self.text_files[index]
        with open(text_file, encoding="utf-8") as f:
            raw_sum, raw_text = f.read().split("\n")
            gt_sum, = re.findall(r"summary\{\{(.*)\}\}", raw_sum)
            text, = re.findall(r"text\{\{(.*)\}\}", raw_text)
        return text, gt_sum

    def __len__(self):
        return len(self.text_files)


class NLPCC2017(object):
    def __init__(self):
        data_file = "../data/nlpcc2017textsummarization/train_with_summ.txt"
        with open(data_file, encoding="utf-8") as f:
            self.data = f.readlines()

    def __getitem__(self, index):
        data = json.loads(self.data[index])
        text = data["article"]
        gt_sum = data["summarization"]
        return text, gt_sum

    def __len__(self):
        return len(self.data)


class DataLoader(object):
    def __init__(self, dataset):
        self.dataset = dataset

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index == len(self.dataset):
            raise StopIteration
        data = self.dataset[self.index]
        self.index += 1
        return data
