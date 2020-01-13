# -*- coding:utf-8 -*-

# import types


def dicts(dump_self):
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
    return result
