set_list = list(s) 
freq = {} 
  for item in set_list: 
    if (item in freq): 
      freq[item] += 1
    else: 
      req[item] = 1
  freq_of_freq = list(freq.values())
  freq_of_freq_counts = set(freq_of_freq)
  if(len(freq_of_freq_counts)==1):
    return "YES"
  else:
    my_freq = {} 
    for item in freq_of_freq: 
      if (item in freq): 
        freq[item] += 1
      else: 
        freq[item] = 1
    theValues = list(freq.values())
    theKeys = list(freq.keys())
    if(len(theValues) == 2):
      if( (theKeys[1] - theKeys[0] <= 1) and (theValues[1] == 1)):
        return "YES"
      else:
        return "NO"
    else:
      return "NO"
