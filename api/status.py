import pickle
from datetime import datetime


def post(ops_status):
    status = ops_status['ops_status']
    print(status)
    with open('ops_status.pickle', 'wb') as f:
        pickle.dump(status, f)


def search():
    with open('ops_status.pickle', 'rb') as f:
        status = pickle.load(f)
    return status
