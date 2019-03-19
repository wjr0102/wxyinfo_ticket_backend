# coding: utf-8

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from flask import Flask, request
from backend import db
import json

"""

数据库相关对象和操作的定义

"""


class User(db.Model):
    """定义user表对象和相关函数"""

    __tablename__ = 'user'
    uid = db.Column(db.Integer, autoincrement=True,
                    nullable=False, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    identity = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String(255), nullable=False)
    num = db.Column(db.String(45), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    seats_time = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<User %r,%r,%r>' % (self.uid, self.name, self.identity)

    def get_info(self):
        """ 返回某一条记录的相关信息，用于查询票务信息 """
        dic = {}
        dic['name'] = self.name
        dic['identity'] = self.identity
        dic['price'] = self.price
        dic['num'] = self.num
        dic['status'] = self.status
        dic['seatsTime'] = self.seats_time

        return dic


class Seat(db.Model):
    """ 定义了seat表对象和相关函数 """

    __tablename__ = 'seat'
    sid = db.Column(db.Integer, autoincrement=True,
                    nullable=False, primary_key=True)
    price = db.Column(db.String(255), nullable=False)
    area = db.Column(db.String(255), nullable=False)
    row = db.Column(db.String(255), nullable=False)
    seat = db.Column(db.String(255), nullable=False)
    occupied = db.Column(db.Integer, nullable=False)
    uid = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Seat %r,%r,%r>' % (self.area, self.row, self.seat)

    def get_info(self):
        """ 返回某一条记录的相关信息，用于查询抽票结果信息 """
        dic = {}
        user = User.query.filter_by(uid=self.uid).first()
        dic['name'] = user.name
        dic['idNumber'] = user.identity
        dic['price'] = self.price
        dic['area'] = self.area
        dic['row'] = self.row
        dic['seat'] = self.seat

        return dic


def getTicketInfo(users):
    """ 从查询结果中返回所需票务信息 """

    if users:
        infos = []
        for user in users:
            infos.append(user.get_info())
        return json.dumps(infos, ensure_ascii=False)
    else:
        return None


def getSeatInfoFromUser(users):
    """ 从用户查询结果中返回所需抽票结果信息 """

    """ 如果用户信息存在则继续查询座位信息，否则返回None """
    if users:
        infos = []  # 用于记录抽票结果的列表

        """ 对用户信息查询结果进行遍历，在表seat中查询相关信息 """
        for user in users:
            uid = user.uid
            """ 注：考虑seat只有被抽取后才会改变uid的值，所以未加入occupied列值查询 """
            seats = Seat.query.filter_by(uid=uid).all()
            for seat in seats:
                infos.append(seat.get_info())
    else:
        return None

    """ 如果用户存在相关已抽票座位信息则返回对应值，否则返回None """
    if infos:
        return json.dumps(infos, ensure_ascii=False)
    else:
        return None


def queryTicketInfoByName(name):
    """从数据库中根据姓名查找票务信息

    参数:
        name: 姓名(中文字符，utf-8编码)

    返回值:
        票务信息，如果没有则返回 None 示例：

        [{'name': '吴宣仪',
         'identity': '531531531531531531',
         'price': '1680',
         'num': 4,
         'status': 0    # 0 表示未抽票, 1 表示已抽票
         'seatsTime'
        }]
    """
    users = User.query.filter_by(name=name).all()   # 根据姓名查询用户信息
    return getTicketInfo(users)


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
    users = User.query.filter_by(identity=idNumber).all()   # 根据身份证号查询用户信息
    return getTicketInfo(users)


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
    users = User.query.filter(User.seats_time >= start,
                              User.seats_time <= end).all()  # 根据抽票时间段查询用户信息
    return getSeatInfoFromUser(users)


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

    users = User.query.filter_by(identity=idNumber).all()  # 根据身份证号查询用户信息
    return getSeatInfoFromUser(users)


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
    users = User.query.filter_by(name=name).all()  # 根据姓名查询用户信息
    return getSeatInfoFromUser(users)


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


if __name__ == '__main__':
    print(User.query.all())
