import json
import pandas as pd
import os

file_list = os.listdir("./json_folder")
kr_list, en_list = [], []

for file in file_list:
    file_name = os.getcwd() + '/json_folder/' + file
    with open(file_name, 'r') as f:
        json_data = json.load(f)
    for data in json_data:
        kr_list.append(data["kr"])
        en_list.append(data["en"])

train_kr, train_en = kr_list[:13500], en_list[:13500]
test_kr, test_en = kr_list[13500:], en_list[13500:]

train_df = pd.DataFrame({"kr": train_kr, "en": train_en})
test_df = pd.DataFrame({"kr": test_kr, "en": test_en})

train_df.to_csv("train.tsv", sep='\t', encoding="utf-8", index=False)
test_df.to_csv("test.tsv", sep='\t', encoding="utf-8", index=False)

