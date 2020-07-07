import glob
import json
import re


def main():
    data = []
    text_files = glob.glob("../data/chinese_abstractive_corpus/copus/*.txt")
    for text_file in text_files:
        with open(text_file, encoding="utf-8") as f:
            raw_sum, raw_text = f.read().split("\n")
            gt_sum, = re.findall(r"summary\{\{(.*)\}\}", raw_sum)
            text, = re.findall(r"text\{\{(.*)\}\}", raw_text)
            data.append({
                "summary": gt_sum,
                "text": text
            })

    with open("../data/chinese_abstractive_corpus/data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)


if __name__ == "__main__":
    main()
