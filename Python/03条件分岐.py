# 3.1 条件分岐

# 文と制御構造
# 1行に処理を1つ書く
# 1行 = 1つの実行単位 = 文(statement)

# 文の代表的な構造
#         ①順次                 ②分岐                    ③繰り返し　　　　　　
#          文                    文                        文
#          ↓↓                    ↓↓                        ↓↓  ←←
#          ↓↓             Yes ←←　　→→ No                  文   ↑↑ 
#          ↓↓             ↓↓           ↓↓                  ↓↓   ↑↑
#          文             文            文                  →→  →→

# 補充:
# 1行 ではない 1つの文とならない書き方
name = '松田' ; print('私の名前は:{}です。'.format(name))

n = 1 + 2 \
+ 3

print(f'答えは:{n}\
改行しても足り算できていますね')

# 良さ:ボリュウームが下がる。
# 悪さ:bug の温床になります。推薦はしないです。

# if文
name = input('あなたの名前を教えてください。\n>>')
print('{}さん、こんにちは！'.format(name))
drink = input('あなたの好きな飲み物を教えてください。\n>>')
print('{}ですか？私も大好きです。'.format(drink))

# いつも同じような会話です。if文を使い、別の感じの会話にチェンジしましょう
name = input('あなたの名前を教えてください。\n>>')
print('{}さん、こんにちは！'.format(name))
drink = input('あなたの好きな飲み物を教えてください。\n>>')

# ifの後ろに処理が分岐する条件を書く
if drink == 'cola':  # 「==」は判断です。 「=」は代入です。 「:」はブロックです。(if block or code block) 改行して、code blockに入ります。
    print('{}ですか？私も大好きです！'.format(drink))

# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
# 条件が成立していたら、ifからelseの前までの文が実行される。

# 条件が成立していなかったら、else以降の文が実行される。
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓

else : # : 忘れないように、ご注意ください。
    print(f'{drink}ですね、美味しいでしょうか？')

# if ブロック
# 基本構文
# if条件式:
#     条件が成立したときの処理(if ブロック)
# else条件式:
#     条件式成立しなかったときの処理(else ブロック)

score = int(input('数字を入力してください。')) # input関数でもらえたデータは、str(文字列)です。比較する前、必ずデータ型を変換してください。
bool = score

if score > 59 : # 「>=」は大なり、「<=」小なりなどなど
    print('合格')                 # print の前の インデント(indent,空)は必要です。
    print('良かったですね。')      # ブロックの範囲をインデントで示す必要があります。

else :
    print('不合格')               # Pythonの標準コーディング規約である「PEP8」で推奨されている4個にすることを勧めします。  
    print('追試を受けてください。')  # VSCODE、JupyterLabなどIDEは、自動に4個分入れて自動でインデントがおこなわれます。
    # print('省略')    ⇒    揃っていないのであれば、エラーになります。


# 比較演算子 (関係演算子)
#  ==  左辺と右辺は等しい (さへん と うへん は ひとしい)
score = input('数字を入力して、当ててみて:')
intscore = int(score)    #データ型を変換 
if score == 100 :
    print('おめでとうございます！正解は{}です。'.format(score))

else :
    print(f'残念ながら、正解は{score}です。')

#  !=  左辺と右辺は等しくない
oldPD = 123456
newPD = int(input('New Passwordを入力してください。\nNew PassWord:'))    #データ型を変換

if newPD != oldPD :
    print('おめでとうございます!パスワード変更できました。\nNew PassWord:{}'.format(newPD))

else :
    print(f'旧パスワードを再入力しないでください。\nOld PassWord:{oldPD}。')

#  >        左辺は右辺より大きい
score = input('点数を入力してください。>>:')
floatscore = float(score)    #データ型を変換
if floatscore > 100 or floatscore < 0 :  # or の ifブロック中での使い方
    print('入力エラー！！')

if floatscore > 59 :
    print('おめでとうございます！合格です。')

else :
    print('残念です、不合格です。')

#  <        左辺は右辺より小さい
score = input('点数を入力してください。>>:')
floatscore = float(score)    #データ型を変換

if floatscore < 0 or floatscore >100 :
    print('入力エラー！！')

if floatscore < 60 :
    print('残念です、不合格です。')

else :
    print('おめでとうございます！合格です。')

#  >=       左辺は右辺より大きいか等しい
score = input('点数を入力してください。>>:')
floatscore = float(score)    #データ型を変換

if floatscore < 0 or floatscore >100 :
    print('入力エラー！！')

if floatscore >= 60 :
    print('おめでとうございます！合格です。')

else :
    print('残念です、不合格です。')

#  <=       左辺は右辺より小さいか等しい
score = input('点数を入力してください。>>:')
floatscore = float(score)    #データ型を変換

if floatscore < 0 or floatscore >100 :
    print('入力エラー！！')

if floatscore <= 59.99999 :
    print('残念です、不合格です。')

else :
    print('おめでとうございます！合格です。')

# in 演算子 (比較演算子)
# 右辺に左辺の値が含まれているかを判定することができます。
favoritefood = input('好きなお菓子を入力してください。(参考:cake,chocolate,chips,cheese)')
food = ['cake','chocolate','chips']
dislikefood = 'cheese'

if favoritefood in food :
    print(f'私も{favoritefood}が好きです。')

if favoritefood in dislikefood :
    print('ええええ、{}は下手です。すみません。'.format(favoritefood))

else :
    print('{}ですか？食べてみたいなぁ！'.format(favoritefood))

# 整数の例はここで省略。
# キー in ディクショナリ
# ディクショナリのキーをチェックする

score = {'network':60,'database':80,'security':100}

key = input('追加する科目名を入力してください。(既存科目:network,database,security)\n>>')

if key in score :
    print(f'該当科目({key})は既に登録済です。')

else :
    data = input('該当科目{}の点数を入力してください。\n>>'.format(key))
    score[key] = data

print(score)

##### 文字列の大小比較 ##### まだ理解しておりません。
name = '松田'
if name < '浅木' :
    print('条件が成立')

else :
    print('条件が成立しない')

# if と 真偽値(bool値)
# True or False 

score = int(input('点数を入力ください。\n>>'))
# score >= 60 という条件が成立した場合 ---> Ture 、じゃないと ---> Flase
print(score >= 60)

score = 60
print(score >= 60)
# 結果は、Tureです。

score = 59
print(score >= 60)
# 結果は、Falseです。

'''
結論として、if文は条件式の評価結果は:
Tureなればifブロックを実行します。
Falseならば、elseブロックを実行します。

if 条件式:
    if ブロック ---> Tureの場合実行

else :
    else ブロック ---> Falseの場合実行
'''

# 論理演算子とその意味
#  演算子　　意味
#   and     かつ
#    or    または
#   not   でなければ

# and ---> すべての条件は、同時に成立すれば、Ture。ではないと、False。
score = int(input('試験点数を入力 \n>>'))
if score < 100 and score > 0 :                
    if score >= 60 :                    # if の下に、もう一度 if 条件式ができます。
        print('おめでとうございます！')
    else :
        print('残念、不合格です。')
else :
    print('正しい点数を入力してください。')

# or ---> 条件のどちらかと一方が成立すれば、Ture。両方不成立であれば、False。
score = int(input('試験点数を入力 \n>>'))
if score > 100 or score < 0 :
    print('正しい点数を入力してください。')
else :
    if score >= 60 :
        print('合格、おめでとうございます！')
    else :
        print('不合格で、再試験参加してください。')

# not ---> not 条件式　もし条件式が成立しなければ
# 一般的に使わないが、何かを排除したいならば使ってください。
score = int(input('試験点数を入力 \n>>'))
if not (score <= 100 and score >= 0) :
    print('正しい点数を入力してください。')
else :
    if not score < 60 :
        print('合格')
    else :
        print('不合格')

# not 文字列の利用
shoppingCart = ['banana','milk','chocolate']
print(shoppingCart)
if not 'ice cream' in shoppingCart :
    print('ice cream is saling!')
# else を省略しても大丈夫です。

# 補充:範囲指定の条件式
score = int(input('点数を入力ください。\n>>'))
if not 100 >= score >= 0 :    # 100 > 値 > 0 のような範囲を指定する条件式ができます。
    print('点数入力錯誤！')
else :
    if score >= 60 : 
        print('合格！')
    else :
        print('不合格。')

# 補充:真偽値に評価されない条件式
'''
score = 0
if score :
    # 処理
else :
    # 処理
'''

# int and float 
num = int(input('数字を入力して:\n>>'))
if num :                                # <--- 0,0.0ではない場合 if を実行 
    print('if has been executed')
else :                                  # <--- 0,0.0の場合 else を実行
    print('else has been executed')

# str and list and set and dir and tuple
message = input('str の内容を入力して: \n>>')
messageStr = message
messageList = [message,]
messageSet = {message}
messageDir = {'':message}
messageTuple =(message,)
if message :                                # <--- False,None,0,0.0,'',"",[],{},() ではない場合 if を実行 
    print('if has been executed')
else :                                  # <--- False,None,0,0.0,'',"",[],{},() の場合 else を実行
    print('else has been executed')

# 分岐構文のバリエーション
# if 構文 ---> 3種類があります
# if-else構文 基本型
# if構文 ifのみの型
# if-elif構文

# if-else構文
#                  ---> Ture ---> ifブロック ---> 終了   
# start ---> 条件式                        
#                  ---> Flase ---> elseブロック ---> 終了
# if 条件式:
# 　　条件式が成立したときの処理
# else:
#     条件式が成立しなかったときの処理

# if のみの構文
#                 ---> Ture ---> ifブロック ---> 終了
# start ---> 条件式                        
#                 ---> Flase ---> 終了
# if 条件式:
#      条件式が成立したときの処理

# esleブロックのない分岐
name = input('お客様のお名前を伺ってもよろしいでしょうか？>>')
if name == 'xiao' : # == は一致するしないの判断です。　= は値を入れるの符号
    print(f'{name}様、大変お待たせしました。では、お席ご案内させていただきます。')

menu = {'チーズケーキ','バナナシープ','ティナミス','塩キャラメルクッキー','アップルパイ'}
food = input('{}様、いらっしゃいませ！本日、お勧めは{}です。お好きなデザートを伺います。'.format(name,menu))

if food in menu:
    print(f'かしこまりました。{food}でよろしいでしょうか。')
else :
    pass  # elseを書かれた以上、空白なのでエラーになります。　この場合、pass で表明すれば OK。　---> 空ブロックの作り方

# if-elif 構文
# ifブロックの後にelifブロックを追加する
# start ---> if条件式 ---> Ture ---> ifブロック -------------------------------> 終了
#                    ---> Flase ---> elif条件式 ---> Ture ---> elifブロック ---> 終了
#                                              ---> Flase ---> elseブロック ---> 終了

# if 条件式1:
#       ifブロック
# elif 条件式2:
#       elifブロック 条件式1が成立せず、条件式2が成立したときの処理
# .
# .
# .
# elif 条件式n:
#       elifブロック ---> 上記の条件式がすべて成立しせず、条件式nが成立したときの処理
# else :
#       elseブロック ---> すべての条件式が成立しなかったときの処理

# 数字当ててゲーム
num_player = int(input('数学当たてゲームやりましょう!0~6の数学を入力してください。'))
num_list = [0,1,2,3,4,5,6]

if num_player == 0:
    print('あなた入力した数学は0です。')
elif num_player == 1:
    print('あなた入力した数学は1です。')
elif num_player == 2:
    print('あなた入力した数学は2です。')
elif num_player == 3:
    print('あなた入力した数学は3です。')
elif num_player == 4:
    print('あなた入力した数学は4です。')
elif num_player == 5:
    print('あなた入力した数学は5です。')
elif num_player == 6:
    print('あなた入力した数学は6です。')
else:
    print('0~6範囲の数学を入力してください。')

# if文のネスト（nest嵌套）
print('夕食について回答してください。\'y\'or\'n\'で入力してください。')
answer = input('お金に余裕はありますか？')
if answer == 'y' :
    abura_answer = input('お腹すごく空いてますか？')
    drink_answer = input('喉乾いていますか？')
    if abura_answer == 'y' and drink_answer == 'y':
        print('焼肉はいかがでしょう？')
    elif abura_answer == 'y':
        print('マクドナルドはいかがでしょう？')
    elif drink_answer == 'y':
        print('ラーメンはいかがでしょう？')
    else:
        print('パスタはいかがでしょう？')
    yasyoku_answer = input('夜食は要りますか？')
    if yasyoku_answer == 'y' :
        print('スーパーマーケットのお菓子を買いましょう。')
    else:
        print('帰りましょう。')
else :
    print('家で自炊しましょう。')