# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 22:30:00 2022

@author: KumarSaurabh
"""

from flask import Flask, jsonify, render_template, request
import socket

app = Flask(__name__)


@app.route('/')
def home():
    s = f'Hostname: {socket.gethostname()}'
    return render_template("index.html", result = {})

@app.route('/table')
def table():
    n = request.args.get('num', type = int)
    res = {}
    s = f'Table of {n}'
    for i in range(10):
        #res.append( f'<tr><td>{n} x {i+1} = </td>  <td>{n*(i+1)}</td></tr>')
        res[f'{n} x {i+1} =']  = f'{n*(i+1)}'
    return render_template("index.html", description = s, result = res)


if __name__== "__main__":
    app.run(host = '0.0.0.0', port = 5000)