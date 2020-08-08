import configparser
import os

# config file
FILE_CONFIG = "./config.conf"
FILE_ENCODING = "utf-8"
SECTION_LOGIN = "login"
OPTION_LOGIN_TOKEN = "token"
OPTION_LOGIN_REFRESH_TOKEN = "refresh_token"
OPTION_LOGIN_SID = "sid"
OPTION_LOGIN_MID = "mid"

def load_login_info():
    """

    Returns:
        token
        refresh_token
        mid
        sid
    """
    if not os.path.exists(FILE_CONFIG) :
        init_config(FILE_CONFIG)
    config = configparser.ConfigParser()
    config.read(FILE_CONFIG, FILE_ENCODING)
    token = config.get(SECTION_LOGIN, OPTION_LOGIN_TOKEN, fallback="")
    r_token = config.get(SECTION_LOGIN, OPTION_LOGIN_REFRESH_TOKEN, fallback="")
    mid = config.get(SECTION_LOGIN, OPTION_LOGIN_MID, fallback="")
    sid = config.get(SECTION_LOGIN, OPTION_LOGIN_SID, fallback="")
    return token, r_token, mid, sid

def init_config(filename):
    with open(FILE_CONFIG, "w+") as f:
        c = configparser.ConfigParser()
        c.add_section(SECTION_LOGIN)
        c.write(f)

def save_login_info(token, r_token, mid, sid):
    """

    Args:
        token
        r_token
        mid
        sid

    Returns:

    """
    config = configparser.ConfigParser();
    config.read(FILE_CONFIG, FILE_ENCODING)
    config.set(SECTION_LOGIN, OPTION_LOGIN_TOKEN, token)
    config.set(SECTION_LOGIN, OPTION_LOGIN_REFRESH_TOKEN, r_token)
    config.set(SECTION_LOGIN, OPTION_LOGIN_MID, mid)
    config.set(SECTION_LOGIN, OPTION_LOGIN_SID, str(sid))
    with open(file=FILE_CONFIG, encoding=FILE_ENCODING, mode= "w+") as f:
        config.write(f)
