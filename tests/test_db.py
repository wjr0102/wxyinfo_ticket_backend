#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-03-18 19:55:02
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-03-20 00:53:47

"""

用于数据库测试的单元测试文件（主要是model接口的测试）

已完成部分：
    queryTicketInfoByIdNumber
    queryTicketInfoByName

"""

"""添加待测试文件路径"""
import sys
import os
sys.path.append(os.path.realpath('../'))

import unittest

from backend import app, db
from backend.model import User, Seat
from backend.model import queryTicketInfoByIdNumber, queryTicketInfoByName, querySeatsByTimeSpan, querySeatsByName, querySeatsByIdNumber
from random import choice


class DbTestCase(unittest.TestCase):
    """数据库测试的Test Case

    主要测试两种情况下接口的返回值：
        1. 存在查询数据，返回数据
        2. 不存在查询数据，返回None"""

    def setUp(self):
        app.config.update(
            TESTING=True,
            WTF_CSRF_ENABLED=False,
            SQLALCHEMY_DATABASE_URI='mysql://root:Likeagod1@127.0.0.1:3306/wxy'
        )
        db.create_all()

    def test_ticket_by_name(self):
        """ 测试接口queryTicketInfoByName """

        users = User.query.all()
        user = choice(users)
        print(user.name)  # 供测试
        result = queryTicketInfoByName(user.name)
        print(result)  # 供测试
        self.assertIsNotNone(result)
        result = queryTicketInfoByName(u'无')
        self.assertIsNone(result)

    def test_ticket_by_idNumber(self):
        """ 测试接口queryTicketInfoByidNumber """

        users = User.query.all()
        user = choice(users)
        print(user.identity)
        result = queryTicketInfoByIdNumber(user.identity)
        print(result)
        self.assertIsNotNone(result)
        result = queryTicketInfoByName(u'无')
        self.assertIsNone(result)

    def test_seat_by_timespan(self):
        """ 测试接口querySeatsByTimeSpan """

        users = User.query.all()
        user = choice(users)
        print(user.seats_time)
        result = querySeatsByTimeSpan(user.seats_time, user.seats_time)
        print(result)
        self.assertIsNotNone(result)
        result = querySeatsByTimeSpan('199912120300', '199912121203')
        self.assertIsNone(result)

    def test_seat_by_idNumber(self):
        """ 测试接口querySeatsByIdNumber """

        result = querySeatsByIdNumber('110105194502177537')     # 存在抽票结果
        print(result)
        self.assertIsNotNone(result)
        result = querySeatsByIdNumber('440229199804084710')    # 不存在抽票结果
        self.assertIsNone(result)
        result = querySeatsByIdNumber('0')     # 不存在该用户
        self.assertIsNone(result)

    def test_seat_by_name(self):
        """ 测试接口querySeatsByName """

        result = querySeatsByName(u'宋桂芝')     # 存在抽票结果
        print(result)
        self.assertIsNotNone(result)
        result = querySeatsByName(u'黄峰')    # 不存在抽票结果
        self.assertIsNone(result)
        result = querySeatsByName(u'0')     # 不存在该用户
        self.assertIsNone(result)

    def tearDown(self):
        """ 为测试方便，暂时忽视tear down函数功能 """
        # db.session.remove()
        # db.drop_all()
        pass


if __name__ == '__main__':
    unittest.main()
