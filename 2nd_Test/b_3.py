import operator

data = {"Anton":70, "Pande": 100, "Malik": 83, "Roni": 99}

highest_score = max(data.items(), key=operator.itemgetter(1))[0]
lowest_score = min(data.items(), key=operator.itemgetter(1))[0]

print('Highest score is  : ' +highest_score)
print('Lowest score is   : '+lowest_score)
