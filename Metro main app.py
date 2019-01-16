import networkx as nx
import json
from os import system
from colorama import init, Fore, Back, Style
init()
# import matplotlib.pyplot as pyplot


line1 = json.loads(open('Line1.json').read())
line2 = json.loads(open('Line2.json').read())
line3 = json.loads(open('Line3.json').read())

# pos = {}
# for i, station in enumerate(line1):
#     if station in ['Al-Shohadaa', 'Sadat']:
#         pos[station] = (2.5, i * 10)
#     else:
#         pos[station] = (3, i * 10)

# for i, station in enumerate(line2):
#     if station == 'Attaba':
#         pos[station] = (1.5, (i * 10) + 100)
#     else:
#         pos[station] = (2, (i * 10) + 100)
    
# for i, station in enumerate(line3):
#     pos[station] = (1, 270 - (i * 10))

metroStationsNetwork = nx.Graph()

metroStationsNetwork.add_nodes_from(line1, line=1)
metroStationsNetwork.add_nodes_from(line2, line=2)
metroStationsNetwork.add_nodes_from(line3, line=3)

for edge in zip(line1, line1[1:]):
    metroStationsNetwork.add_edge(*edge)

for edge in zip(line2, line2[1:]):
    metroStationsNetwork.add_edge(*edge)

for edge in zip(line3, line3[1:]):
    metroStationsNetwork.add_edge(*edge)

# nx.draw(metroStationsNetwork, pos, with_labels=True, font_size=8)
# pyplot.show()
# pyplot.savefig(r'D:\Programming\MetroStationsNetwork\fig.png')


def shortestPath(source, destination):

    return nx.shortest_path_length(metroStationsNetwork, source, destination)

def getPath(source, destination):

    paths =  [x for x in nx.all_shortest_paths(metroStationsNetwork, source, destination)]

    if len(paths) > 1:
        scores = [0 for i in paths]

        for i, path in enumerate(paths):
            prevLine = metroStationsNetwork.node[path[0]]['line'] if path[0] not in ['Al-Shohadaa', 'Attaba', 'Sadat'] else None

            for station in path[1:]:
                if station in ['Al-Shohadaa', 'Attaba', 'Sadat']:
                    continue

                currentLine = metroStationsNetwork.node[station]['line']
                if currentLine != prevLine and not prevLine is None:
                    scores[i] += 1

                prevLine = currentLine

        if min(scores) == max(scores):
            return tuple(path for path in paths)
        
        else:
            return paths[scores.index(min(scores))]

    else:
        return paths[0]

def printPath(stationsList):
    for i, station in enumerate(stationsList):

        if i == 0:
            print(Fore.MAGENTA + station, end='')

        else:
            print(Fore.RESET + Back.MAGENTA + ' >> ', end='')
            print(Fore.MAGENTA + Back.RESET + station, end='')

def main():
    while True:

        while True:
            print(Fore.MAGENTA + Style.BRIGHT + 'Line 1: ', end='')

            print(Fore.RESET + Back.MAGENTA + line1[0], end='')
            for station in line1[1:]:
                print(' >> ' + station, end='')


            print(Back.RESET + Fore.YELLOW + '\n\nLine 2: ', end='')

            print(Fore.RESET + Back.YELLOW + line2[0], end='')
            for station in line2[1:]:
                print(' >> ' + station, end='')


            print(Back.RESET + Fore.GREEN + '\n\nLine 3: ', end='')

            print(Fore.RESET + Back.GREEN + line3[0], end='')
            for station in line3[1:]:
                print(' >> ' + station, end='')

            print('\n\n' + Back.RESET)

            print(Fore.CYAN, end='')
            print('Enter source: ', end='')
            print(Fore.RESET, end='')
            source = input().strip()

            print(Fore.CYAN, end='')
            print('Enter destination: ', end='')
            print(Fore.RESET, end='')
            destination = input().strip()

            try:
                numberStations = shortestPath(source, destination)

            except nx.exception.NodeNotFound:
                print(Fore.RED, end='')
                print('Please review your input and spelling, either {0} or {1} is not correctly spelled.\n'.format(source, destination))
                input('Press ENTER to retype your input.')
                system('cls')


            else:
                break

        print(Fore.CYAN + '\nNumber of stations: ', end='')
        print(Fore.RESET + Back.CYAN + str(numberStations), end='')
        print(Back.RESET, end='\n\n')

        if numberStations <= 9:
            print(Fore.YELLOW + 'Yellow ticket')

        elif numberStations <= 16:
            print(Fore.GREEN + 'Green ticket')

        else:
            print(Fore.RED + 'Red ticket')

        print(Fore.CYAN)
        print('Your path will be:\n')

        paths = getPath(source, destination)

        if isinstance(paths, tuple):

            for i, path in enumerate(paths):

                printPath(path)

                if i != len(paths) - 1:
                    print(Fore.CYAN + '\n\nOr:\n')

        else:
            printPath(paths)

        print('\n' + Fore.CYAN)
        print('Again?\n("y" or "n")\n\n')
        print(Fore.RESET, end='')
        again = input()

        if again == 'y':
            system('cls')
            continue

        else:
            break

    SystemExit

if __name__ == '__main__':
    main()
