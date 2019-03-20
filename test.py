#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-03-20 00:45:41
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-03-20 14:24:11

from backend import model as M

if __name__ == "__main__":
    users = M.User.query.all()
    for user in users:
        print(user)
        print(M.querySeatsByTimeSpan(
            (int)(user.seats_time) - 10, (int)(user.seats_time) + 10))
        print(M.querySeatsByTimeSpan(
            (int)(user.seats_time) + 10, (int)(user.seats_time) + 100))
        print(M.querySeatsByTimeSpan(
            (int)(user.seats_time) - 10, (int)(user.seats_time) - 1))
