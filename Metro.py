import networkx as nx
import matplotlib.pyplot as pyplot

line1 = ['Helwan', 'Ain Helwan', 'Helwan University', 'Wadi Hof', 'Hadayek Helwan', 'El-Maasara', 'Tora El-Asmant', 'Kozzika', 'Tora El-Balad', 'Sakanat El-Maadi', 'Maadi', 'Hadayek El-Maadi', 'Dar El-Salam', "El-Zahraa'", 'Mar Girgis', 'El-Malek El-Saleh', 'Al-Sayeda Zeinab', 'Saad Zaghloul', 'Sadat', 'Nasser', 'Orabi', 'Al-Shohadaa', 'Ghamra', 'El-Demerdash', 'Manshiet El-Sadr', 'Kobri El-Qobba', 'Hammamat El-Qobba', 'Saray El-Qobba', 'Hadayeq El-Zaitoun', 'Helmeyet El-Zaitoun', 'El-Matareyya', 'Ain Shams', 'Ezbet El-Nakhl', 'El-Marg', 'New El-Marg']
line2 = ['El-Mounib', 'Sakiat Mekky', 'Omm El-Masryeen', 'Giza', 'Faisal', 'Cairo University', 'El Bohoth', 'Dokki', 'Opera', 'Mohamed Naguib', 'Attaba', 'Masarra', 'Rod El-Farag', 'St. Teresa', 'Khalafawy', 'Mezallat', 'Kolleyyet El-Zeraa', 'Shubra El-Kheima']
line3 = ['Al-Ahram', 'Koleyet El-Banat', 'Stadium', 'Fair Zone', 'Abbassiya', 'Abdou Pasha', 'El-Geish', 'Bab El-Shaaria']


pos = {}
for i, station in enumerate(line1):
    if station in ['Al-Shohadaa', 'Sadat']:
        pos[station] = (2.5, i * 10)
    else:
        pos[station] = (3, i * 10)

for i, station in enumerate(line2):
    if station == 'Attaba':
        pos[station] = (1.5, (i * 10) + 100)
    else:
        pos[station] = (2, (i * 10) + 100)
    
for i, station in enumerate(line3):
    pos[station] = (1, 270 - (i * 10))

metro = nx.Graph()
metro.add_nodes_from(line1)
metro.add_nodes_from(line2)
metro.add_nodes_from(line3)
for edge in zip(line1, line1[1:]):
    metro.add_edge(*edge)
for edge in zip(line2, line2[1:]):
    metro.add_edge(*edge)
for edge in zip(line3, line3[1:]):
    metro.add_edge(*edge)



metro.add_edge('Masarra', 'Al-Shohadaa')
metro.add_edge('Al-Shohadaa', 'Attaba')
metro.add_edge('Attaba', 'Bab El-Shaaria')
metro.add_edge('Mohamed Naguib', 'Sadat')
metro.add_edge('Sadat', 'Opera')

metro.remove_edge('Mohamed Naguib', 'Opera')
metro.remove_edge('Masarra', 'Attaba')


nx.draw(metro, pos, with_labels=True, font_size=8)
# pyplot.show()
# pyplot.savefig(r'D:\Programming\Metro\fig.png')

def shortestPath(source, destination, metro=metro):
    # return nx.all_shortest_paths(metro, source, destination)
    return nx.shortest_path_length(metro, source, destination)
def main():
    source = input('Enter source: ')
    destination = input('Enter destination: ')
    print(shortestPath(source, destination))
    print('\n\n')
    # print([p for p in nx.all_shortest_paths(metro, source, destination)])
    again = input('Again?\n')
    if again == 'y':
        print('\n\n')
        main()
    else:
        SystemExit
if __name__ == '__main__':
    main()