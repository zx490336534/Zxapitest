from django.db import models

from utils.models import ModelBase


class User(ModelBase):
    id = models.AutoField(primary_key=True)
    username = models.CharField(
        max_length=30,
        unique=True,
    )
    password = models.CharField(
        max_length=30,
    )
    email = models.EmailField()

    class Meta:
        ordering = ['-update_time', '-id']
        db_table = "tb_user"  # 指明数据库表名

    def __str__(self):  # 这个__str__方法的作用将在查询时看到
        return f'User<id={self.id},username={self.username},email={self.email}'
