class Flower:

    def __init__(self, name, average_lifetime, price, freshness, color, stem_length):
        self.name = name
        self.average_lifetime = average_lifetime
        self.price = price
        self.freshness = freshness
        self.color = color
        self.stem_length = stem_length

    def __repr__(self):
        return f'{self.name}'


class Rose(Flower):
    def __init__(self, name, average_lifetime, price, freshness, color, stem_length, has_spikes):
        super().__init__(name, average_lifetime, price, freshness, color, stem_length)
        self.has_spikes = has_spikes


class Popy(Flower):
    def __init__(self, name, average_lifetime, price, freshness, color, stem_length, psychoactive):
        super().__init__(name, average_lifetime, price, freshness, color, stem_length)
        self.psychoactive = psychoactive


class Lily(Flower):
    def __init__(self, name, average_lifetime, price, freshness, color, stem_length, smell_type):
        super().__init__(name, average_lifetime, price, freshness, color, stem_length)
        self.smell_type = smell_type


class Bouquet:
    def __init__(self, flowers_list):
        self.flowers_list = flowers_list

    def __repr__(self):
        return f'{self.flowers_list}'

    def bouquet_price(self):
        return sum([flower.price for flower in self.flowers_list])

    def average_ttl(self):
        return sum([flower.average_lifetime for flower in self.flowers_list]) // len(self.flowers_list)

    def sorting_bouquet(self, sorting_parameter):
        if sorting_parameter == 'freshness':
            self.flowers_list.sort(key=lambda x: x.freshness)
        elif sorting_parameter == 'color':
            self.flowers_list.sort(key=lambda x: x.color)
        elif sorting_parameter == 'stem_length':
            self.flowers_list.sort(key=lambda x: x.stem_length)
        elif sorting_parameter == 'price':
            self.flowers_list.sort(key=lambda x: x.price)
        return self.flowers_list

    def search_flower(self, searching_parameter, value):
        if searching_parameter == 'average_lifetime':
            for i in self.flowers_list:
                if i.color == value:
                    return i
        elif searching_parameter == 'price':
            for i in self.flowers_list:
                if i.color == value:
                    return i
        elif searching_parameter == 'freshness':
            for i in self.flowers_list:
                if i.color == value:
                    return i
        elif searching_parameter == 'color':
            for i in self.flowers_list:
                if i.color == value:
                    return i
        elif searching_parameter == 'stem_length':
            for i in self.flowers_list:
                if i.color == value:
                    return i


rose1 = Rose(
    'King Rose',
    10,
    300,
    'fresh',
    'red',
    10,
    True
)

rose2 = Rose(
    'Wild Rose',
    15,
    140,
    'not fresh',
    'bright red',
    11,
    False
)

lily1 = Lily(
    'Japan Lily',
    20,
    200,
    'fresh',
    'white',
    18,
    'very good'
)

bouquet1 = Bouquet([rose1, rose2, lily1])
print(f'The price of bouquet is {bouquet1.bouquet_price()}$.')
print(f'The average lifetime of the bouqeut is {bouquet1.average_ttl()} hours.')
print(f'The bouquet is sorte by price: {bouquet1.sorting_bouquet("price")}')
print(f"Searching white color flower in the bouquet: {bouquet1.search_flower('color', 'white')}")