# programa que extrae los hashtags de un texto en un archivo .csv

import re
import pandas as pd
from collections import Counter
import emoji

def extract_string(df):
    hashtags = re.compile("#\w+")
    users = re.compile("@\w+")
    #urls = re.compile("https?://(([a-zA-z]|[0-9]|[?]|#|=|-|&)+[.|/]?)+")
    urls = re.compile("https?://[a-zA-z0-9./?=&#-]+")

    # Formatos de tiempo
    tttttt = re.compile("([0-1]?[0-9]|2[0-4]):([0-5][0-9]|60)(:[0-5][0-9]|60)?")
    am_pm = re.compile("(0?[0-9]|10|11|12)(:[0-5][0-9](:[0-5][0-9])?)? ?(AM|PM|am|pm)")
    hrs = re.compile("(\d+) ?(hrs|hr|hour|hours|horas|hora)")

    # Emoticones
    emoticones = re.compile("([:;=][)|vDdPpOo(Ss]+)|([|VvDOo(][;:=])")

    todos_los_hashtags = []
    todos_los_usuarios = []
    todos_los_urls = []
    todas_los_tiempos = []
    todos_los_emoticones = []
    todos_los_emojis = []

    for tweet in df["text"]:
        # si encuentra hashtags en el tweet, los añade a la lista
        if hashtags.findall(tweet):
            todos_los_hashtags.extend(hashtags.findall(tweet))
        if users.findall(tweet):
            todos_los_usuarios.extend(users.findall(tweet))
        if urls.findall(tweet):
            todos_los_urls.extend(urls.findall(tweet))
        if tttttt.findall(tweet):
            todas_los_tiempos.extend(tttttt.findall(tweet))
        if am_pm.findall(tweet):
            todas_los_tiempos.extend(am_pm.findall(tweet))
        if hrs.findall(tweet):
            todas_los_tiempos.extend(hrs.findall(tweet))
        if emoticones.findall(tweet):
            todos_los_emoticones.extend(emoticones.findall(tweet))
        if emoji.emoji_list(tweet):
            for objeto in emoji.emoji_list(tweet):
                todos_los_emojis.append(objeto["emoji"])

    # cuenta la frecuencia de cada cadena
    conteo_hashtags = Counter(todos_los_hashtags)
    conteo_users = Counter(todos_los_usuarios)
    conteo_urls = Counter(todos_los_urls)
    conteo_tiempos = Counter(todas_los_tiempos)
    conteo_emoticones = Counter(todos_los_emoticones)
    conteo_emojis = Counter(todos_los_emojis)


    # imprime los 10 cadenas más comunes
    print(conteo_hashtags.most_common(10))
    print(conteo_users.most_common(10))
    print(conteo_urls.most_common(10))
    print(conteo_tiempos.most_common(10))
    print(conteo_emoticones.most_common(10))
    print(conteo_emojis.most_common(10))

if __name__ == "__main__":
    archivo = pd.read_csv("tweets.csv")
    extract_string(archivo)