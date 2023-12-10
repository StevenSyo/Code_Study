'''変更前の確認'''
SELECT * FROM 家計簿;

'''DELETEの実施⇒ある条件を満たす行を削除する'''
DELETE FROM 家計簿 WHERE 日付 = '2022-02-25';

'''変更前の確認'''
SELECT * FROM 家計簿 WHERE 出金額 = 90000;