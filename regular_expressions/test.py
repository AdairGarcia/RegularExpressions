import re
import pandas as pd
from collections import Counter

archivo = pd.read_csv("tweets.csv")

# Formatos de tiempo
tttttt = re.compile(r"([0-1]?[0-9]|2[0-4]):([0-5][0-9]|60)(:[0-5][0-9]|60)?")
am_pm = re.compile("(0?[0-9]|(10)|(11)|(12))(:[0-5][0-9](:[0-5][0-9])?)?( )?(AM|PM|am|pm)")
hrs = re.compile("\d+( )?(hrs|hr|hour|hours|horas|hora)")

todas_los_tiempos = []

for tweet in archivo["text"]:
    if tttttt.findall(tweet) or am_pm.findall(tweet) or hrs.findall(tweet):
        todas_los_tiempos.extend(tttttt.findall(tweet))
        todas_los_tiempos.extend(am_pm.findall(tweet))
        todas_los_tiempos.extend(hrs.findall(tweet))

conteo_tiempos = Counter(todas_los_tiempos)
print(conteo_tiempos.most_common(10))
