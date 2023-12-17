# 4.0 繰り返し

# while 文
# whileの後ろに処理を繰り返す条件式を書く
# 条件が成立している間は、直後のブロックが繰り返し実行される
# 条件が成立していなかったら、繰り返しが終わる

'''
while 条件式:  *while文は、無限ループを起こしやすい
    条件が成立したときの処理(whileブロック)
'''

# ひつじを数えて眠る
print('さあ、寝ようかな') 
count = 0    # ひつじの数  --->  count という変数は、カウンタ変数 または ループ変数(ループカウンタ)　といいます。
count += 1    
print('ひつじの数は{}匹。'.format(count))
count += 1
print('ひつじの数は{}匹。'.format(count))
count += 1
print('ひつじの数は{}匹。'.format(count))
count += 1
print('ひつじの数は{}匹。'.format(count))
print('おやすみなさい')

# 10回を数えると？
count = 0 # ひつじの数
while count < 10:                                # この条件に満たさない限り、下のブロック文を実行する。
    count += 1
    print('ひつじの数は{}匹。'.format(count))
print('おやすみなさい')


# 無限ループにならないように注意します。
'''
count = 0 # ひつじの数
while count < 10:                                # この条件に満たさない限り、下のブロック文を実行する。
    print('ひつじの数は{}匹。'.format(count))
'''

# while文 状態による繰り返す
drowsiness = False  
count = 1
while drowsiness == False:
    print('ひつじの数は{}匹。'.format(count))
    ask = input('眠気ありますか？(y/n) >>')
    if ask == 'y': 
        drowsiness = True 
    else:
        count += 1

print('おやすみなさい。')

# while文 繰り返しによるリストの作成
count = 1
student_num = int(input('学生の数を入力 >>'))
score_list = list()
while count < student_num :
    score = int(input('{}番目の試験の得点を入力 >>'.fromat(count)))
    score_list.append(score)
    count += 1
print(score_list)
total = sum(score_list)
print('学生{}名の平均点は、{}点です。'.fromat(count,total/count))

# while文 繰り返しによるリスト要素の利用
scores = [10,20,30,40,50,60,70,80,90,100]
count = 0
num_pass = 0
num_fail = 0
while count < len(score):
    if scores[count] >= 60:
        print("{}番目学生は合格です。成績は{}点です。".format(count + 1,scores[count]))
        num_pass += 1
        count += 1
    else :
        print("{}番目学生は不合格です。成績は{}点です。".format(count + 1,scores[count]))
        num_fail += 1
        count += 1
print("確認完了。")

'''

while文 でリストの要素を参照する。
カウンタ変数 = 0
while カウンタ変数 < len(リスト):
      リスト[カウンタ変数]を使った処理
      カウンタ変数 += 1

'''

# for文 による繰り返し　
scores = [10,20,30,40,50,60,70,80,90,100]
num_pass = 0
num_fail = 0
for data in scores:
    if data >= 60:
        num_pass += 1
        print("{}番目学生は合格です。成績は{}点です。".format(num_pass + num_fail,data))
    else:
        num_fail += 1
        print("{}番目学生は合格です。成績は{}点です。".format(num_pass + num_fail,data))
print('確認完了。合格人数：{}、不合格人数：{}'.format(num_pass,num_fail))


'''

For 文の紹介
for文は、while文と同様に、直後のブロックを繰り返し実行します。実行されるものforブロックといいます。for block
for文による繰り返す回数は、リストの要素数(Index)で決まります。
       ←←←←←←←←
      ↓        ↑ 
for data in scores :

for 文でリストの全要素を参照する
for 変数 in リスト:
     繰り返し処理

'''

# for 文で決まった回数を繰り返す
for num in range(3) :
    print('{}回目実行'.format(num + 1))

'''

range() 関数
range(3) ---> [0,1,2]という、ゼロから、整数のリストを作成する

仕様：
range(n)

for文 できまった回数を繰り返し
for 変数 in range(n):
     繰り返し処理

'''

# for文 と while文 の使い分け
'''
while文:  繰り返す回数の目処が立たないときに使う
for文:    繰り返す回数の目処が立つときに使う
'''

# 繰り返しの制御
## 繰り返しの強制終了

# データのまとまりからサンプルを抽出する 
ages = [20,25,75,64,45,15,34,35,22,27,61,55,59]
num = 5                     # サンプルの抽出を制御するため、五つと設定する
samples = list()
for age in ages:
    if 22 < age < 65:
        if len(samples) < num:
            samples.append(age)
print("サンプル取得成功。サンプル数:{}。\n{}".format(num,samples))


## break文 目標数に達した繰り返しを終了する
ages = [20,25,75,64,45,15,34,35,22,27,61,55,59]
num = 5                     
samples = list()
for age in ages:
    if 22 < age < 65:
        samples.append(age)
        if len(samples) == num: # 抽出目標は達したため、break文で中止
            break      
print("サンプル取得成功。サンプル数:{}。\n{}".format(num,samples))

## continue文 不要な回のループをスキップする
ages = [20,25,75,'秘密',64,45,15,34,35,'無回答',22,27,61,55,59]
samples = list()
for data in ages:
    if not isinstance(data,int):  # isinstance(データ,データ型)
        continue
    if data < 22 or data > 65:
        continue
    samples.append(data)
print(samples)


'''

isinstance(deta,deta type)
* データがデータ型と一致したらTrueに置き換わる
* データ型にはint,str,boolなどが使用できる

'''


# break文 と continue文

## break文 繰り返し自体を中断
data_list = [1,2,3]
for num in data_list:
    if num == 2:
        break
    print(num)

## continue文 今回だけを中断し、次の回へ
data_list = [1,2,3]
for num in data_list:
    if num == 2:
        continue
    print(num)

## 改行しないこと
print("hello",end="")
print(end)
# helloPython