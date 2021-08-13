import re
import pytz
import requests
from datetime import datetime
from urllib import parse

def sintilde(x):  # Not a command
    eq = (
            ('á', 'a'),
            ('é', 'e'),
            ('í', 'i'),
            ('ó', 'o'),
            ('ú', 'u')
        )
    for a,b in eq:
        x = x.replace(a, b).replace(a.upper(), b.upper())
    return x

def clock(opt, arg):
    if opt == 'search':
        rtz = arg.replace(' ', '_')
        s = ""
        for i in pytz.all_timezones:
            if re.match(f"(.+)?/?{rtz.lower()}(.+)?/?", i.lower()):
                s += f"{i}\n"
        return s

#    if opt == 'capital':
#        q = f"capital de {arg}"
#        r = requests.get(f"https://google.com/search?q={parse.quote(q)}")
#        s = re.search('<div class="BNeawe deIvCb AP7Wnd">[^<>]+</div>', r.text)
#        s = s.group().replace('<div class="BNeawe deIvCb AP7Wnd">', "").replace("</div>", "")
#        return s

    if opt == 'get':
        rtz = sintilde(arg.replace(' ', '_'))
        tz = ""
        for i in pytz.all_timezones:
            if rtz.lower() in i.lower():
                tz = i
                break
        if not tz:
            return "Zona horaria desconocida"
        format = "%H:%M:%S"
        utc = datetime.now(pytz.timezone('UTC'))
        rtz = utc.astimezone(pytz.timezone(tz))
        return rtz.strftime(format)

if __name__ == "__main__":
    print(clock('get', 'bajasur'))
