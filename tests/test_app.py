#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-03-18 19:45:54
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-03-18 21:43:59

"""

用于app常规测试的单元测试文件


"""

import unittest

from backend import app, db
from backend.model import User, Seat
from backend.model import queryTicketInfoByIdNumber, queryTicketInfoByName


class AppTestCase(unittest.TestCase):
    """docstring for AppTestCase"""

    def setUp(self):
        app.config.update(
            TESTING=True,
            WTF_CSRF_ENABLED=False,
            SQLALCHEMY_DATABASE_URI='mysql://root:Likeagod1@127.0.0.1:3306/wxy'
        )
        db.create_all()
        self.client = app.test_client()
        self.runner = app.test_cli_runner()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_app_exist(self):
        self.assertFalse(app is None)

    def test_app_is_testing(self):
        self.assertTrue(app.config['TESTING'])
