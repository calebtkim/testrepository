import os
import datetime
from flask import Flask
import logging.config

if not os.path.isdir(os.environ.get('LOG_PATH', 'log')):
  os.mkdir(os.environ.get('LOG_PATH', 'log'))


app = Flask(__name__)

log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logging.ini')
logging.config.fileConfig(log_file_path, disable_existing_loggers=False)
logger = logging.getLogger(__name__)


@app.route("/")
def index():
  return "Your Flask App Works!"  

@app.route("/hello")
def hello():
  app.logger.debug('The hello path was called')
  return "Hello World!"

@app.route("/other")
def other():
  app.logger.debug('The other path was called')
  return "You're viewing the other path!"


@app.route("/health")
def health():
  selected_date = datetime.datetime.now()
  app.logger.debug('The health path was called')
  return f'HealthCheck performed at: {selected_date}'


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000, debug=False)
