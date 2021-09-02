#print("Hello World")
#print("\n")
import nltk, scipy, numpy, matplotlib, pandas
from nltk.corpus import twitter_samples
import matplotlib.pyplot as plt
import random

nltk.download("twitter_samples")
pos_tweets= twitter_samples.strings("positive_tweets.json")
neg_tweets= twitter_samples.strings("negative_tweets.json")

print("Total # of positive tweets: ",len(pos_tweets))
print("Total # of negative tweets: ",len(neg_tweets))
print("\nThe type of positive/negative tweets is: ",type(pos_tweets),type(neg_tweets))
print("The type of tweet entry is: ",type(pos_tweets[0]))

"""fig= plt.figure(figsize= (5,5)) #figure with random_size
labels= 'ML-BSB-Lec', 'ML-HAP-Lec', 'ML-HAP-Lab' #class labels
sizes= [50,25,25] #size for each slide

# declare pie chart, where slices will be ordered & plotted counter-clockwise
# autopct print slices in %2f% string format, like 25.00%
plt.pie(sizes, labels=labels, autopct= '%.2f%%', shadow=True, startangle=90) 
plt.axis('equal')
plt.show() """

""" plot data of +ve and -ve tweets """
fig= plt.figure(figsize= (5,5))
labels= 'positive', 'negative'
sizes= [len(pos_tweets), len(neg_tweets)]
plt.pie(sizes, labels=labels, autopct="%1.1f%%", shadow=False, startangle=0)
plt.axis('equal')
plt.show()

print('\n\033[92m' + pos_tweets[random.randint(0,5000)]) #print +ve tweet in green color
print('\033[91m' + neg_tweets[random.randint(0,5000)]) #print -ve tweets in red color
# \033 is escape char in python followed by special code like, 93m=>yellow, 94m=>blue, 96m=>cyan, 97m=>white <<ASCII_COLOR_CODE>>



