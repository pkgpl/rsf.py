import re
import sys


def errexit(msg, errno=1):
    warn(msg)
    sys.exit(errno)


def warn(msg):
    sys.stderr.write(msg + "\n")


def quote(st):
    return '"' + st + '"'


def unquote(st):
    if st.startswith("'") or st.startswith('"'):
        return st[1:-1]
    else:
        return st


def fromstring(key, text, un_quote=True):
    try:
        val = re.findall(key + "\s*=\s*(\S+)", text)[-1]
        for q in ["'", '"']:
            if val.startswith(q) and not val.endswith(q):
                val = re.findall(key + "=" + q + "(.+?)" + q, text)[-1]
        if un_quote:
            val = unquote(val)
        return val, True
    except:
        return 0, False


def file2str(filename=''):
    if filename and filename.lower() != 'stdin':
        with open(filename, 'r') as fh:
            string = fh.read()
    else:
        string = sys.stdin.read()
    return string


def str2file(string, filename=''):
    if filename and filename.lower() != 'stdout':
        with open(filename, 'w') as fh:
            fh.write(string)
    else:
        sys.stdout.write(string)
