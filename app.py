from flask import Flask
import argparse
import logging

app = Flask(__name__)
logging.basicConfig(filename="./log/logger.log", filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)

@app.route('/')
def home():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--account_no", default=None, type=str, help="AWS account_no")
    parser.add_argument("-s", "--start_date", default=(datetime.now() - timedelta(1)).strftime('%Y-%m-%d'), type=str, help="The starting date for billing")
    parser.add_argument("-e", "--end_date", default=(datetime.now()).strftime('%Y-%m-%d'), type=str, help="The ending date for billing")
    parser.add_argument("-g", "--granularity", default='DAILY', type=str, help="The granularity of the billing")
    parser.add_argument("-l", "--loggingn", default='logging', type=str, help="Set the log file name")
    parser.add_argument("-o", "--options", type=str, help="Options to change output")
    
    options = parser.parse_args()
    
    log.info("Hello")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
