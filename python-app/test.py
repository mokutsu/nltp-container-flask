from textblob import TextBlob

if __name__ == '__main__':
    s = "Python is great"
    b = TextBlob(s)
    print(b.sentiment)
