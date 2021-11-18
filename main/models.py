from django.db import models
from django.db.models.fields import DateField
from django.utils import timezone  # djangoでは、datetime.now のかわりに、timezone.now で現在日付・時刻を取得する

# グループリスト
class groop_list(models.Model):

    groop_id = models.CharField('グループID', max_length=20)
    groop_name = models.CharField('グループ名', max_length=50)
    target = models.CharField('目標', max_length=50)
    start_date = models.DateField('開始日')
    insert_date = models.DateTimeField('挿入日付', default=timezone.now)
    insert_people_ID = models.CharField('挿入者ID', max_length=20)
    update_date = models.DateTimeField('更新日付', default=timezone.now)
    update_people_ID = models.CharField('更新者ID', max_length=20)

# グループ活動履歴
class groop_action_history(models.Model):
    
    groop_id = models.CharField('グループID', max_length=20)
    action_date = models.DateTimeField('更新日付', default=timezone.now)
    history = models.CharField('結果', max_length=1)
    insert_date = models.DateTimeField('更新日付', default=timezone.now)
    insert_people_ID = models.CharField('グループ名', max_length=20)

# グループメンバー一覧
class groop_member_list(models.Model):

    groop_id = models.CharField('グループid', max_length=20)
    member_id = models.CharField('メンバーid', max_length=20)
    member_name = models.CharField('メンバー名', max_length=20)
    insert_date = models.DateTimeField('挿入日付', default=timezone.now)
    insert_people_id = models.CharField('挿入者ID', max_length=20)
    update_date = models.DateTimeField('更新日付', default=timezone.now)
    update_people_id = models.CharField('更新者ID', max_length=20)