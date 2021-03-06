import csv
import json
import os
import glob
import pandas as pd
import numpy as np


def merge_csv():
    result_dirs = ["../inputs/voice_recorder", "../outputs/voice_recorder_lead1",
                   "../outputs/voice_recorder_tfidf", "../outputs/voice_recorder_textrank"]

    filenames = os.listdir(result_dirs[0])

    cols = ['text', 'gt', 'lead', 'tfidf', 'textrank']
    with open("merge.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(cols)
        for filename in filenames:
            row = []
            summaries = []
            for result_dir in result_dirs:
                path = os.path.join(result_dir, filename)
                if "inputs" in path:
                    with open(path, encoding="utf-8") as f:
                        text = json.load(f)['text']

                with open(path, encoding="utf-8") as f:
                    summary = json.load(f)["summary"]
                    summaries.append(summary)
            row = [text] + summaries
            writer.writerow(row)


def merge_json():
    result_dirs = ["../inputs/voice_recorder", "../outputs/voice_recorder_lead1",
                   "../outputs/voice_recorder_tfidf", "../outputs/voice_recorder_textrank"]

    filenames = os.listdir(result_dirs[0])

    tags = ['gt', 'lead', 'tfidf', 'textrank']
    os.makedirs("../outputs/merge/", exist_ok=True)

    for filename in filenames:
        summaries = {}
        for tag, result_dir in zip(tags, result_dirs):
            path = os.path.join(result_dir, filename)
            if "inputs" in path:
                with open(path, encoding="utf-8") as f:
                    summaries["text"] = json.load(f)['text']

            with open(path, encoding="utf-8") as f:
                summary = json.load(f)["summary"]
                summaries[tag] = summary

        with open(f"../outputs/merge/{filename}", "w", encoding="utf-8") as f:
            json.dump(summaries, f, ensure_ascii=False, indent=4)


def merge_excel():
    paths = glob.glob("../outputs/merge/*.json")
    with pd.ExcelWriter('merge.xlsx', engine='xlsxwriter') as writer:
        for idx, path in enumerate(paths):
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
            text = data['text'].split('\n')
            num_sections = len(text)
            gt = [data['gt']] + [""] * (num_sections - 1)
            textrank = [data['textrank']] + [""] * (num_sections - 1)
            lead = [data['lead']] + [""] * (num_sections - 1)
            tfidf = [data['tfidf']] + [""] * (num_sections - 1)
            arr = np.array([text, gt, lead, tfidf, textrank], dtype=object).T
            df = pd.DataFrame(arr, columns=['Text', 'Abs. GT', 'Lead1', 'TF-IDF', 'TextRank'])
            df.to_excel(writer, sheet_name=f'Sheet{idx}', index=False)


def main():
    merge_json()
    merge_excel()


if __name__ == "__main__":
    main()
