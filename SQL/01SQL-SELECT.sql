'''Selectの実施⇒ある条件を満たす行を取得する'''
SELECT 日付,費目,メモ,入金額,出金額 FROM 家計簿;

SELECT * FROM 家計簿;

SELECT * FROM 家計簿 WHERE 出金額 > 3000;