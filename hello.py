#!/usr/bin/env python
# coding: utf-8

import sys
from flask import Flask
from flask import abort, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "Top Page"

@app.route('/hello')
def hello_workd():
    return "Hellow World!"

@app.route('/str/<arg_str>')
def show_arg(arg_str):
    app.logger.info('this is str %s' % arg_str)
    return '%s'%arg_str

@app.route('/int/<int:arg_int>')
def show_post(arg_int):
      return '%s'%arg_int

@app.route('/redir')
def redir():
    return redirect(url_for('index'))

if __name__ == '__main__':
    if 'debug' in sys.argv:
        app.debug = True
    app.run()
