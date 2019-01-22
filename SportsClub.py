class Club:
    def __init__(self, name):
        self.name = name
        self.players = []

    def __getitem__(self, item):
        return self.players[item]

    def __len__(self):
        return len(self.players)

    def __repr__(self):
        return f'{self.name}: {self.players}'

    def __str__(self):
        return f'{self.name} with {len(self)} players'


club1 = Club('ManUnited')
club1.players.append('Mata')
club1.players.append('Pogba')

for i in range(len(club1.players)):
    print(club1[i])

print(club1)
print(repr(club1))