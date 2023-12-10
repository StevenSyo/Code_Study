# 関数内で準備された変数は、その関数の中でしか読み書き出来ない！
name = "Cafe"
def input_scores():
    name = ''
    print('{}の試験結果を入力してください。'.format(name))
input_scores()

## 修正　Paramaterを関数に入れる場合
def input_scores():
    name = "Cafe"
    print('{}の試験結果を入力してください。'.format(name))
input_scores()

## 修正後 Paramaterを関数に入れない場合
def input_scores(name):
    print('{}の試験結果を入力してください。'.format(name))
name = "Cafe"
input_scores(name)
