# coding: utf-8

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from flask import Flask, request


def queryTicketInfoByName(name):
    """从数据库中根据姓名查找票务信息

    参数:
        name: 姓名(中文字符，utf-8编码)

    返回值:
        票务信息，如果没有则返回 None 示例：

        [{'name': '吴宣仪',
         'idNumber': '531531531531531531',
         'price': '1680',
         'num': 4,
         'status': 0    # 0 表示未抽票, 1 表示已抽票
         'seatsTime'
        }]
    """
    pass


def queryTicketInfoByIdNumber(idNumber):
    """从数据库中根据身份证号查找票务信息

        参数:
            idNumber: 身份证号, 18位字符串

        返回值:
            票务信息，如果没有则返回 None 示例：

            [{'name': '吴宣仪',
             'idNumber': '531531531531531531',
             'price': '1680',
             'num': 4
            }]
        """
    pass


def querySeatsByTimeSpan(start, end):
    """从数据库中根据时间段查询已抽票信息

        参数:
            start: 起始时间戳 (1970-01-01开始的毫秒数)
            end:   结束时间戳 (1970-01-01开始的毫秒数)

        返回值:
            在时间范围内的所有座位信息，如果没有则返回 None 示例：

            [{'name': '吴宣仪',
             'idNumber': '531531531531531531',
             'price': '1680',
             'area': '107A',
             'row': '19',
             'seat': '4'
            }, {'name': '吴宣仪',
             'idNumber': '531531531531531531',
             'price': '1680',
             'area': '107A',
             'row': '19',
             'seat': '5'
            }]
        """
    pass


def querySeatsByIdNumber(idNumber):
    """从数据库中根据身份证号查询已抽票信息

        参数:
            idNumber: 身份证号, 18位字符串

        返回值:
            在时间范围内的所有座位信息，如果没有则返回 None 示例：

            [{'name': '吴宣仪',
             'idNumber': '531531531531531531',
             'price': '1680',
             'area': '107A',
             'row': '19',
             'seat': '4'
            }, {'name': '吴宣仪',
             'idNumber': '531531531531531531',
             'price': '1680',
             'area': '107A',
             'row': '19',
             'seat': '5'
            }]
        """
    pass


def querySeatsByName(name):
    """从数据库中根据姓名查询已抽票信息

        参数:
            name: 姓名(中文字符，utf-8编码)

        返回值:
            在时间范围内的所有座位信息，如果没有则返回 None ，示例：

            [{'name': '吴宣仪',
             'idNumber': '531531531531531531',
             'price': '1680',
             'area': '107A',
             'row': '19',
             'seat': '4'
            }, {'name': '吴宣仪',
             'idNumber': '531531531531531531',
             'price': '1680',
             'area': '107A',
             'row': '19',
             'seat': '5'
            }]
        """
    pass


def queryTicketInfoBySeats(price, area, row, seat):
    """从数据库中根据座位号查询订票信息

        参数:
            price: 字符串 票价
            area: 字符串 会场区
            row: 字符串 排号
            seat: 字符串 座位号

        返回值:
            返回该座位对应的订票信息，如果没有被抽取则返回 None ，示例：

            [{'name': '吴宣仪',
             'idNumber': '531531531531531531',
             'price': '1680',
             'area': '107A',
             'row': '19',
             'seat': '4'
            }]
    """
    pass


def queryTicketInfoByStatus(status):
    """从数据库中根据抽票状态查询座位信息

        参数:
            status: 抽票状态

        返回值:
            在时间范围内的所有座位信息，如果没有则返回 None ，示例：

            [{'name': '吴宣仪',
             'idNumber': '531531531531531531',
             'price': '1680',
             'area': '107A',
             'row': '19',
             'seat': '4'
            }, {'name': '吴宣仪',
             'idNumber': '531531531531531531',
             'price': '1680',
             'area': '107A',
             'row': '19',
             'seat': '5'
            }]
        """
    pass