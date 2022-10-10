import os
import pandas as pd
import random

# フォルダ内のファイル名を取得
files = os.listdir()

# exceptionsに含まれるファイル名を、filesから除外
exceptions = ['rename.ipynb', 'rename.py', 'words.csv', '.ipynb_checkpoints'] 
for exception in exceptions:
    if exception in files:
        files.remove(exception)

# words.csvのリストを取得
words = pd.read_csv("words.csv", header=None).values.tolist()

# フォルダ内のファイル数に合わせて、words.csvから変更後ファイル名をランダムで取得
change_to = []
for file in files:
    word = random.choice(words)[0]
    # 変更後ファイル名の重複を避けるため、重複した場合はファイル名にversionを付与
    i = 2
    while word in change_to:
        if i == 2:
            word = word + "_v2"
        else:
            word = word.split('_v')[-2] + "_v" + str(i)
        i += 1
    change_to.append(word)

# ファイル名の変更を実施
i = 0
for file in files:
    # 拡張子を現状維持するために変更前ファイル名の拡張子を取得して、後続の変更処理に利用する。
    if len(file.split('.')) == 1:
        extension = ""
    else:
        extension = file.split('.')[-1]
    os.rename(file, change_to[i] + "." + extension) 
    i +=1