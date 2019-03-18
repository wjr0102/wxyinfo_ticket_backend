#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-03-18 16:07:58
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-03-18 20:57:40
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from flask import Flask, request

from backend.choose_seats import choose_seats as choose_seats_impl
from flask_sqlalchemy import SQLAlchemy


import pymysql
pymysql.install_as_MySQLdb()

app = Flask('app')

'''
mysql server
'''
DATABASE_URI = 'mysql://root:Likeagod1@127.0.0.1:3306/wxy'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

'''
Object Relational Mapping
'''
db = SQLAlchemy(app)

from backend import commands
