import datetime

bangnokay_raw = None

def set_bangnokay(value):
    global bangnokay_raw
    bangnokay_raw = value

def check():
    if bangnokay_raw is None:
        now = datetime.datetime.now()
        set_bangnokay(now.month == 4 and now.day < 2)

    return bangnokay_raw