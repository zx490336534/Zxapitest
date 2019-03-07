import json

from django.shortcuts import render
from django.views import View
from . import models
from django.db.models import Count
from utils.json_fun import to_json_data
from utils.res_code import Code, error_map


class IndexView(View):
    def get(self, request):
        return render(request, 'index/index.html')


class CallectionsView(View):
    def get(self, request):
        tags = models.Callections.objects.values('id', 'name')
        return render(request, 'index/callections.html', locals())

    def post(self, request):
        json_data = request.body
        if not json_data:
            return to_json_data(errno=Code.PARAMERR, errmsg=error_map[Code.PARAMERR])
        # 将json转化为dict
        dict_data = json.loads(json_data.decode('utf8'))
        tag_name = dict_data.get('name')
        if tag_name and tag_name.strip():
            tag_tuple = models.Callections.objects.get_or_create(name=tag_name)
            tag_instance, tag_created_bolean = tag_tuple
            new_tag_dict = {
                "id": tag_instance.id,
                "name": tag_instance.name
            }
            return to_json_data(errmsg="接口集创建成功", data=new_tag_dict) if tag_created_bolean else \
                to_json_data(errno=Code.DATAEXIST, errmsg="接口集名已存在")
        else:
            return to_json_data(errno=Code.PARAMERR, errmsg="接口集名为空")


class CallectionsEditView(View):
    def put(self, request, callections_id):
        json_data = request.body
        if not json_data:
            return to_json_data(errno=Code.PARAMERR, errmsg=error_map[Code.PARAMERR])
        # 将json转化为dict
        dict_data = json.loads(json_data.decode('utf8'))
        tag_name = dict_data.get('name')
        tag = models.Callections.objects.only('id').filter(id=callections_id).first()
        if tag:
            if tag_name and tag_name.strip():
                if not models.Callections.objects.only('id').filter(name=tag_name).exists():
                    tag.name = tag_name
                    tag.save(update_fields=['name'])
                    return to_json_data(errmsg="接口集更新成功")
                else:
                    return to_json_data(errno=Code.DATAEXIST, errmsg="接口集已存在")
            else:
                return to_json_data(errno=Code.PARAMERR, errmsg="接口集为空")

        else:
            return to_json_data(errno=Code.PARAMERR, errmsg="需要更新的接口集不存在")
