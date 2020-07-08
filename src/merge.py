import csv
import json
import os

def main():
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


if __name__ == "__main__":
    main()
