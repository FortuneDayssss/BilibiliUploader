import hashlib
import rsa
import base64
import subprocess
import platform
import os.path


def md5(data: str):
    """
    generate md5 hash of utf-8 encoded string.
    """
    return hashlib.md5(data.encode("utf-8")).hexdigest()


def md5_bytes(data: bytes):
    """
    generate md5 hash of binary.
    """
    return hashlib.md5(data).hexdigest()


def sign_str(data: str, app_secret: str):
    """
    sign a string of request parameters
    Args:
        data: string of request parameters, must be sorted by key before input.
        app_secret: a secret string coupled with app_key.

    Returns:
        A hash string. len=32
    """
    return md5(data + app_secret)


def sign_dict(data: dict, app_secret: str):
    """
    sign a dictionary of request parameters
    Args:
        data: dictionary of request parameters.
        app_secret: a secret string coupled with app_key.

    Returns:
        A hash string. len=32
    """
    data_str = []
    keys = list(data.keys())
    keys.sort()
    for key in keys:
        data_str.append("{}={}".format(key, data[key]))
    data_str = "&".join(data_str)
    data_str = data_str + app_secret
    return md5(data_str)


def login_sign_dict_bin(data: dict):
    data_str = []
    keys = list(data.keys())
    keys.sort()
    for key in keys:
        data_str.append("{}={}".format(key, data[key]))
    data_str = "&".join(data_str)
    package_directory = os.path.dirname(os.path.abspath(__file__))
    if platform.system().lower() == 'windows':
        print(data_str)
        print(subprocess.Popen([os.path.join(package_directory, "sign.exe"), data_str], stdout=subprocess.PIPE).communicate()[0].decode().strip())

        return subprocess.Popen([os.path.join(package_directory, "sign.exe"), data_str], stdout=subprocess.PIPE).communicate()[0].decode().strip()
    if platform.system().lower() == 'linux':
        return subprocess.Popen([os.path.join(package_directory, "sign.out"), data_str], stdout=subprocess.PIPE).communicate()[0].decode().strip()
    raise Exception("Operating System is not supported.")


def encrypt_login_password(password, hash, pubkey):
    """
    encrypt password for login api.
    Args:
        password: plain text of user password.
        hash: hash provided by /api/oauth2/getKey.
        pubkey: public key provided by /api/oauth2/getKey.

    Returns:
        An encrypted cipher of password.
    """
    return base64.b64encode(rsa.encrypt(
        (hash + password).encode('utf-8'),
        rsa.PublicKey.load_pkcs1_openssl_pem(pubkey.encode()),
    ))


def av2bv(av: int):
    table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
    tr = {}
    for i in range(58):
        tr[table[i]] = i
    s = [11, 10, 3, 8, 4, 6]
    xor = 177451812
    add = 8728348608

    av = (av ^ xor) + add
    r = list('BV1  4 1 7  ')
    for i in range(6):
        r[s[i]] = table[av // 58 ** i % 58]
    return ''.join(r)


def bv2av(bv: str):
    table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
    tr = {}
    for i in range(58):
        tr[table[i]] = i
    s = [11, 10, 3, 8, 4, 6]
    xor = 177451812
    add = 8728348608

    r = 0
    for i in range(6):
        r += tr[bv[s[i]]] * 58 ** i
    return (r - add) ^ xor
