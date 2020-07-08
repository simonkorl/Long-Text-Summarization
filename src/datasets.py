import glob
import os
import re
import json
import pandas as pd
import json


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


class TextSumDataset(object):
    def __init__(self, root_dir):
        self.paths = glob.glob(f"{root_dir}/*.json")

    def __getitem__(self, index):
        path = self.paths[index]
        basename = os.path.basename(path)
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
            gt_sum = data["summary"]
            text = data["text"]
        return basename, text, gt_sum

    def __len__(self):
        return len(self.paths)


chinese_abstractive_corpus = TextSumDataset("../inputs/chinese_abstractive_corpus/")
nlpcc2017 = TextSumDataset("../inputs/nlpcc2017/")
voice_recorder = TextSumDataset("../inputs/voice_recorder/")
