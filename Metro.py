def count(start, end):
    # Defining line 1
    line1 = {}
    list1 = ['Shohada', 'Oraby', 'Gamal Abdel Nasser', 'Sadat', 'Saad Zaghlol', 'Zeynab']
    for i, station in enumerate(list1):
        line1[station] = i

    # Defining line 2
    line2 = {}
    list2 = ['Shohada', 'Ataba', 'Mohammad Naguib', 'Sadat', 'Opera', 'Dokki']
    for i, station in enumerate(list2):
        line2[station] = i

    if start in line1 and end in line1:
        return abs(line1[start] - line1[end])
    elif start in line2 and end in line2:
        return abs(line2[start] - line2[end])
    elif start in line1 and end in line2:
        shohadaDist = abs(line1[start] - line1['Shohada'])
        sadatDist = abs(line1[start] - line1['Sadat'])
        if shohadaDist < sadatDist:
            nearestTransDist = (shohadaDist, 'Shohada')
        else:
            nearestTransDist = (sadatDist, 'Sadat')

        return nearestTransDist[0] + abs(line2[nearestTransDist[1]] - line2[end])

    



print(count('Shohada', 'Zeynab'))