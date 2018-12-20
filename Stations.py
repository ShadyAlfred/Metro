# # Defining line 1
# line1 = ['Shohada', 'Oraby', 'Gamal Abdel Nasser', 'Sadat', 'Saad Zaghlol', 'Zeynab']

# # Defining line 2
# line2 = ['Shohada', 'Ataba', 'Mohammad Naguib', 'Sadat', 'Opera', 'Dokki']

# # Defining a set
# stationsSet = set(line1 + line2)



# <tr>
# <td>Helwan</td>
# <td>حلوان</td>
# <td>Line 1</td>





import re 
html = open('List of Cairo Metro stations.html', 'r', encoding='utf-8')
text = html.read()
# line1 = re.findall(r'<tr>\s<td>([\w\s-]*)</td>\s<td>[\w\s]*</td>\s<td>Line 1</td>\s', text)
# print(line1)
line1 = re.findall(r'<tr>\s<td>([\w\s\'-]*)</td>\s<td>[\w\s]*</td>\s<td>Line 1(?:</td>\s|\s&amp;\s.*\s\d</td>\s)', text)
line1 = line1[:-3]
print(line1)
line2 = re.findall(r'<tr>\s<td>([\w\s\.\'-]*)</td>\s<td>[\w\s]*</td>\s<td>Line 2(?:</td>\s|\s&amp;\s.*\s\d</td>\s)', text)
line2 = line2[:-1]
print(line2)
line3 = re.findall(r'<tr>\s<td>([\w\s\.\'-]*)</td>\s<td>[\w\s]*</td>\s<td>Line 3(?:</td>\s|\s&amp;\s.*\s\d</td>\s)', text)
line3 = line3[line3.index('Al-Ahram'):line3.index('Bab El-Shaaria') + 1]
print(line3)
html.close()
input()