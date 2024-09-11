import re
import pandas as pd
from collections import Counter

def extract_string(df):
    hashtags = re.compile("#\w+")
    users = re.compile("@\w+")
    urls = re.compile("(https?://(([a-zA-z]|[0-9]|[?]|#|=|-|&)+[.|/]?)+)")

    # Formatos de tiempo
    tttttt = re.compile("([0-1]?[0-9]|2[0-4]):([0-5][0-9]|60)(:[0-5][0-9]|60)?")
    am_pm = re.compile("(0?[0-9]|10|11|12)(:[0-5][0-9](:[0-5][0-9])?)? ?(AM|PM|am|pm)")
    hrs = re.compile("(\d+) ?(hrs|hr|hour|hours|horas|hora)")

    # Emoticones
    emoticones = re.compile("[^A-Za-z](>?[:;=xX][)|vDdPpOo(Ss]+)|([|VvDOo(][;:=xX]<?)$")

    # Emojis
    # https://www.compart.com/en/unicode/block
    emojis = re.compile("[\U00002600-\U000027BF\U0001F600-\U0001F64F\U0001F680-\U0001F6FF\U0001F900-\U0001F9FF]")

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
        if emojis.findall(tweet):
            todos_los_emojis.extend(emojis.findall(tweet))


    # cuenta la frecuencia de cada cadena
    conteo_hashtags = Counter(todos_los_hashtags)
    conteo_users = Counter(todos_los_usuarios)
    conteo_urls = Counter(todos_los_urls)
    conteo_tiempos = Counter(todas_los_tiempos)
    conteo_emoticones = Counter(todos_los_emoticones)
    conteo_emojis = Counter(todos_los_emojis)


    # imprime los 10 cadenas más comunes
    print("HASHTAGS")
    print(f'Numero total de matches: {len(todos_los_hashtags)}')
    print(conteo_hashtags.most_common(10))

    print("USUARIOS")
    print(f'Numero total de matches: {len(todos_los_usuarios)}')
    print(conteo_users.most_common(10))

    print("URLS")
    print(f'Numero total de matches: {len(todos_los_urls)}')
    print(conteo_urls.most_common(10))

    print("TIEMPOS")
    print(f'Numero total de matches: {len(todas_los_tiempos)}')
    print(conteo_tiempos.most_common(10))

    print("EMOTICONES")
    print(f'Numero total de matches: {len(todos_los_emoticones)}')
    print(conteo_emoticones.most_common(10))

    print("EMOJIS")
    print(f'Numero total de matches: {len(todos_los_emojis)}')
    print(conteo_emojis.most_common(10))

if __name__ == "__main__":
    archivo = pd.read_csv("tweets.csv")
    extract_string(archivo)