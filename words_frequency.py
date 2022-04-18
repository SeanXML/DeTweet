import holoviews as hv
import hvplot
hv.extension("bokeh")
import matplotlib.pyplot as plt
import nltk
#plt.figure(figsize=(15, 5))
#plt.xlabel('xlabel')
#plt.ylabel('ylabel')

def freq(tokens_list, filepath="/result.csv", plot = False):
    # You may split your text with .split() that allows the function to calculate the frequency
    freqlist = nltk.FreqDist(tokens_list)
    result = sorted(freqlist.items(),key=lambda item:item[1], reverse=True)

    with open(filepath,'w') as f:
        for i in result:
            f.write(str(i)+'\n')
    if plot:
        freqlist.plot(30,cumulative=False)
    
    return result