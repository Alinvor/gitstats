# -*- coding:utf-8 -*-

# import types
import collections
import json


def dicts(dump_self):
    ''' the custom dictionary printing and formatting tool '''
    result = {}
    if dump_self is not None:
        for item in dir(dump_self):
            # filter inner field by fieldname
            if item.startswith('_') or item == 'metadata':
                continue
            value = getattr(dump_self, item)
            # filter inner field by value type
            if callable(value):
                continue
            # if type(value) not in (types.NoneType, types.IntType,
            #                        types.LongType, types.StringType,
            #                        types.UnicodeType, types.DictType):
            #     continue
            result[item] = getattr(dump_self, item)

        keys = result.keys()
        keys.sort()
        results = collections.OrderedDict()  # 有序字典
        for key in keys:
            results[key] = result[key]
        result.clear()
        result = results
        json_list = json.dumps(result, indent=4, cls=SetEncoder)
        # print(json_list)
        return json_list
    return result


class SetEncoder(json.JSONEncoder):
    '''
    python set encoder and then refer to\n
    - https://stackoverflow.com/questions/8230315/how-to-json-serialize-sets
    - https://docs.python.org/2.7/library/json.html#json.JSONEncoder
    - https://docs.python.org/3/library/json.html#json.JSONEncoder
    '''
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)
