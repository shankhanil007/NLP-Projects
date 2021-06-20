# https://youtu.be/tFPSWkqJU6g

from textblob import TextBlob

text = "My name is Shankhanil"
text = "You scored very well in this exam"
text = "Your clothes are very dirty"

edu = TextBlob(text)
x = edu.sentiment.polarity
if x<0:
    print("Negative")
elif x==0:
    print("Neutral")
elif x>0 and x<=1:
    print("Positive")

