#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:zhongxin
# datetime:2019/3/3 10:42 AM
import json
import re

import jsonschema


class JsonSchemaOperator():
    def __init__(self, json_data):
        self.json_data = json_data
        self.limit = []
        # limit: [["对象","类型","最大值/最大长度","最小值/最小长度","允许输入的内容","正则表达式/格式/某个整数的倍数"],[]]

    def to_jsonschema(self, json_data, result):
        '''
        递归生成jsonschema
        '''
        if isinstance(json_data, dict):
            is_null = True
            result.append('{')
            result.append("'type': 'object',")
            result.append("'additionalProperties': 'false',")  # 不允许添加任何其他属性。
            result.append("'required':[],")  # 必需属性,先留空
            result.append("'properties': {")
            for k, v in json_data.items():
                is_null = False
                result.append("'%s':" % k)
                self.to_jsonschema(v, result)
                result.append(',')
            if not is_null:
                result.pop()
            result.append('}')
            result.append('}')
        elif isinstance(json_data, list):
            result.append('{')
            result.append("'type': 'array',")
            result.append("'items': ")
            self.to_jsonschema(json_data[0], result)
            result.append('}')
        elif isinstance(json_data, float):
            result.append("{")
            result.append("'type': 'number'")
            result.append('}')
        elif isinstance(json_data, int):
            result.append("{")
            result.append("'type': 'integer'")
            result.append('}')
        elif isinstance(json_data, str):
            result.append("{")
            # if json_data.upper() in ("TRUE", "FALSE"):
            #     result.append("'type': 'boolean'")
            # else:
            result.append("'type': 'string'")
            result.append('}')
        return "".join(result)

    def complement_required(self, jsonschema_dict):
        """
        补全必需属性
        """
        if isinstance(jsonschema_dict, dict):
            for item, value in jsonschema_dict.items():
                if value == 'object':
                    properties = jsonschema_dict.get("properties")
                    if isinstance(properties, dict):
                        for i, j in properties.items():
                            if j.get("type") in ("integer", "number", "string"):
                                self.complement_limit(i, j)
                            jsonschema_dict['required'].append(i)
                            if isinstance(j, dict) and j.get('type') == "object":
                                self.complement_required(j)
        elif isinstance(jsonschema_dict, list):
            for i in jsonschema_dict:
                self.complement_required(i)

    def complement_limit(self, name, limit_dict):
        """

        :return:
        """
        for i in self.limit:
            if name == i[0]:
                limit_type = i[1]
                if limit_type == 'integer' or limit_type == 'number':
                    if i[2]:
                        limit_dict["maximum"] = i[2]
                    if i[3]:
                        limit_dict["minimum"] = i[3]
                    if i[4]:
                        limit_dict["enum"] = i[4]
                    if i[5]:
                        limit_dict["multipleOf"] = i[5]
                elif limit_type == 'string':
                    if i[2]:
                        limit_dict["maxLength"] = i[2]
                    if i[3]:
                        limit_dict["minLength"] = i[3]
                    if i[4]:
                        limit_dict["enum"] = i[4]
                    if i[5]:
                        limit_dict["pattern"] = i[5]

    def to_json(self):
        result = []
        try:
            self.testdata = self.to_jsonschema(self.json_data, result)
            self.testdata = json.loads(re.sub('\'', '\"', self.testdata))
            self.complement_required(self.testdata)
            # print(self.testdata)
            # print(json.dumps(self.testdata, indent=4))
            return self.testdata
        except Exception as e:
            print(f'输入的JSON数据有问题, 请检查:{e}')


if __name__ == '__main__':
    a = {
        "checked": "False",
        "dimensions": {
            "width": 5,
            "height": 10
        },
        "id": 1,
        "name": "A green door",
        "price": 12.5,
        "tags": [
            "home",
            "green"
        ]
    }
    j = JsonSchemaOperator(a)
    j.limit.append(['price', "number", 200, 100, [200, 150, 100], 50])
    j.to_json()
    v = jsonschema.Draft7Validator(j.testdata)
    errors = sorted(v.iter_errors(a), key=lambda e: e.path)
    for e in errors:
        print(e)
