'''追加前の確認'''
SELECT * FROM 家計簿;

'''inter into:追加⇒一番下の行から、内容を追加する'''
INSERT INTO 家計簿 VALUES ('2022-02-25','居住費','3月の家賃',0,85000);

'''追加後の確認'''
SELECT * FROM 家計簿;