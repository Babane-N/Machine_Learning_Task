#!/usr/bin/env python3

def main():
    import nltk
    from textblob import TextBlob
    from newspaper import Article

    nltk.download('punkt')

    url = 'https://www.bbc.com/news/technology-65855333'
    article = Article(url)

    article.download()
    article.parse()
    article.nlp()

    text = article.text
    print(text)

    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity  # -1 to 1
    print()
    print("The sentiment of thi article is:", sentiment)


if __name__ == '__main__':
    main()