# coding: utf-8

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from backend import app, db
from backend.model import User, Seat


@app.route('/chooseSeats', methods=['GET'])
def choose_seats():
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=53101)
