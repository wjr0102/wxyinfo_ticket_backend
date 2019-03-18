#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-03-18 20:03:06
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-03-18 20:58:12
import click


from backend import app, db
from backend.model import User, Seat
from random import choice


@app.cli.command()
@click.option('--count', default=20, help='Quantity of messages, default is 20.')
def forge(count):
    """Generate fake messages."""
    from faker import Faker

    db.drop_all()
    db.create_all()

    fake = Faker(locale='zh_CN')
    fake.seed(0)

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
