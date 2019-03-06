from django.db import models

from utils.models import ModelBase


class Callections(ModelBase):
    name = models.CharField(max_length=64, verbose_name="接口集名称", help_text="接口集名称")

    class Meta:
        ordering = ['-update_time', '-id']
        db_table = "tb_tag"  # 指明数据库表名

    def __str__(self):
        return self.name
