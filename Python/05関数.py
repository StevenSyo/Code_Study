# 関数はPythonも準備してくれているが、自分たちでも作れる。

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

'''
関数名の衝突による上書き
すでに定義されている関数と同じく名前を付けると、以前の関数はよびだせなくなる

ローカル
関数の中で定義された変数は、その関数の中でしか使えない。
その関数の外やほかの関数の中に偶然同じ名前の変数があったとしても、まったく無関係な別の存在として扱われる。
'''

# 実引数と仮引数
def profile (name,age,hobby):  # name,age,hobbyは仮引数 中文叫做形式参数，形参
    print("私の名前は{}".format(name))
    print("私の年齢は{}".format(age))
    print("私の好みは{}".format(hobby))
profile("Steven","30","Cafe")  # "Steven","30","Cafe"は実引数 中文叫做实际参数，实参

'''
引数を利用する関数の定義
def 関数名(引数1,引数2,...):
    処理

引数を利用する関数の呼び出し
関数名(引数1,引数2,...)
'''

# 平均点の計算
def calc_average(scores):
    avg = sum(scores) / len(scores)
    print('平均点は{}'.format(avg))
calc_average([10,20,30,40,50,60,70,80,90])


# 点数を入力して、平均点の計算
def input_scores(name):
    print('{}さんの試験結果を入力してください。'.format(name))
    network = int(input('network point?'))
    database = int(input('database point?'))
    security = int(input('ssecurity point?'))
    scores = [network,database,security]

def calc_average(scores):
    avg = sum(scores) / len(scores)
    print('平均点は{}'.format(avg))

# 点数を入力して、平均点の計算
def input_scores(name):
    print('{}さんの試験結果を入力してください。'.format(name))
    network = int(input('network point?'))
    database = int(input('database point?'))
    security = int(input('security point?'))
    scores = [network, database, security]
    return scores #　ローカル変数scoresは、この関数以外のところいけないただし、関数の実行結果になる

def calc_average(scores):
    avg = sum(scores) / len(scores)
    print('平均点は{}'.format(avg))

scores = input_scores("Steven") #　input_scores()関数の計算結果を、次の関数の仮引数に代入
calc_average(scores)

'''
戻り値 return value

def 関数名(引数1,引数2,...):
    処理
    return 値

変数 = 関数名(引数1,引数2,...)
↓  ↓  ↓ イコール ↓ ↓ ↓
変数 = 関数名のreturn 値

戻り値を受け取る変数名 = 関数名(引数1,引数2,...)

*もしreturn文がない場合、returnは「None」、空っぽのけっかです。
'''

# どんどん代入して計算します。
def puls(x,y):                # puls関数を定義
    answer = x + y
    return answer             # puls関数の計算結果を戻し　puls(x,y)

answer = puls(100,50)            
# 引数を代入して、puls(100,50)計算して、「puls(100,50)」が「150」になる。そして、「150」はanswerに代入
print("足し算の答えは{}です".format(answer))   # answerの結果をprint関数に出し


# 二つの戻り値を返す
def plus_and_minus(a,b):
    return a + b , a - b

next,prev = plus_and_minus(2023,1)
print("この二つの数で足し算の答えは{}であり、引き算の答えは{}です。".format(next,prev))

# 