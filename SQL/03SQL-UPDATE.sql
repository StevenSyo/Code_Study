'''変更前の確認'''
SELECT 出金額 FROM 家計簿 WHERE 日付 = '2022-02-25';

'''UPDATE変更実施⇒ある条件を満たす行を書き換え'''
UPDATE 家計簿 SET 出金額 = 90000 WHERE 日付 = '2022-02-25';

'''変更後の確認'''
SELECT 出金額 FROM 家計簿 WHERE 日付 = '2022-02-25';
