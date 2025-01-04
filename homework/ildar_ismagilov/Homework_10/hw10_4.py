PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

rows = PRICE_LIST.split('\n')
pairs = [row.split(' ') for row in rows]
price_dict = {key: int(value[:-1]) for key, value in pairs}
