import pandas as pd


ACCOUNTS_FILE_PATH = "src/data/accounts.json"
MSGHISTORY_FILE_PATH = "src/data/msghistory.json"


def get_accounts():
    return pd.read_json(ACCOUNTS_FILE_PATH, typ="series")


def get_messages():
    return pd.read_json(MSGHISTORY_FILE_PATH, typ="series")


def save_to_file(messages):
    messages.to_json(MSGHISTORY_FILE_PATH)


def save_accounts(accounts):
    accounts.to_json(ACCOUNTS_FILE_PATH)
