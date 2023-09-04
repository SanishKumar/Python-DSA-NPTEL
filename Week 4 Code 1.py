def rainaverage(l):
    d=dict(l)
    for i in d.keys():
        for j in



def rainaverage(l):
  raindata = {}
  for (c,r) in l:
    if c in raindata.keys():
      raindata[c].append(r)
    else:
      raindata[c] = [r]
  outputlist = []
  for c in sorted(raindata.keys()):
    thisaverage = sum(raindata[c])/len(raindata[c])
    outputlist.append((c,thisaverage))
  return(outputlist)


def rainaverage(l):
    # Create a dictionary to store total rainfall and number of recordings for each city
    city_totals = {}
    city_counts = {}
    for city, rainfall in l:
        # Update the city's total rainfall and number of recordings
        city_totals[city] = city_totals.get(city, 0) + rainfall
        city_counts[city] = city_counts.get(city, 0) + 1
    # Compute the average rainfall for each city and store it in a list
    averages = []
    for city in sorted(city_totals.keys()):
        ar = city_totals[city] / city_counts[city]
        averages.append((city, ar))
    return averages
