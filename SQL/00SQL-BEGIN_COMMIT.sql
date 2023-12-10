--仮の書き換え
BEGIN;
begin;

--BEGINの前に戻る(エラーの時)
ROLLBACK;
rollback;

--書き換えの実施
COMMIT;
commit;