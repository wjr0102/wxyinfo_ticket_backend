#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-03-18 20:03:06
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-03-19 18:13:08

"""

定义自定义flask命令行命令，包括：
    1. forge-user
    2. forge-seat

"""

import click


from backend import app, db
from backend.model import User, Seat
import random
from random import choice


@app.cli.command()
@click.option('--count', default=20, help='Quantity of messages, default is 20.')
def forge_user(count):
    """为表user生成一些假数据"""
    from faker import Faker

    db.drop_all()
    db.create_all()

    fake = Faker(locale='zh_CN')
    fake.seed(0)
    random.seed(0)

    click.echo('Working...')

    for i in range(count):
        user = User(
            name=fake.name(),
            identity=fake.ssn(),
            phone=fake.phone_number(),
            price=choice([380, 480, 680, 980, 1380, 1680]),
            num=choice(list(range(1, 10))),
            status=choice([0, 1]),
            seats_time=fake.date_time_this_year()
        )
        db.session.add(user)

    db.session.commit()
    click.echo('Created %d fake users.' % count)


@app.cli.command()
@click.option('--count', default=20, help='Quantity of messages, default is 20.')
def forge_seat(count):
    """为表seat生成一些假数据"""
    from faker import Faker

    db.drop_all()
    db.create_all()

    fake = Faker(locale='zh_CN')
    fake.seed(0)
    random.seed(0)

    click.echo('Working...')

    for i in range(count):
        seat = Seat(
            price=choice([380, 480, 680, 980, 1380, 1680]),
            area=fake.locale(),
            row=choice(list(range(1, 50))),
            seat=choice(list(range(1, 50))),
            occupied=choice([0, 1]),
            uid=choice(list(range(0, 20)))
        )
        db.session.add(seat)

    db.session.commit()
    click.echo('Created %d fake seats.' % count)
