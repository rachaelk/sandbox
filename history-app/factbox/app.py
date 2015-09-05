from flask import Flask, request, session, g, redirect, url_for, Response, \
	abort, render_template, flash, jsonify, send_from_directory
from sqlalchemy import create_engine, func
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from numpy import isclose
from datetime import datetime, timedelta
from math import ceil
import json
import re
from subprocess import Popen, PIPE


DEBUG = True
SECRET_KEY = 'develop'
USERNAME = 'admin'
PASSWORD = 'password'


name_of_database = 'factbox'
engine = create_engine('postgresql://localhost/' + name_of_database, convert_unicode=True)
db_session = scoped_session(sessionmaker(
	autocommit=False,
	autoflush=False,
	bind=engine
))

app = Flask(__name__)
app.config.from_object(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/', methods=['GET', 'POST'])
def main():
	return send_from_directory('static/html', 'index.html')

if __name__ == '__main__':
	app.run()
