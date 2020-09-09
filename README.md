# Tweet_Sentiment_Analysis
# Sentiment Analysis Of Donald Trump's Tweets from 2019
## Out-of-Core Learning Implementation

Sentiment analysis uses natural language processing to analyze affective states and subjective information. In recent years considerable concern has arisen over the Sentiment analysis of a political issue.For example, Josemar A. Caetano uses sentiment analysis to define twitter political users’ classes and their homophily during the 2016 American presidential election. Also, Haselmayer use the sentiment analysis in political communication topic. A number of studies have been conducted on political issues in using Sentiment analysis.

While others have done sentiment analysis on the tweets of our current president, Donald Trump, a more difficult task than just predicting positive or negative tweets, is capturing a 'neutral' sentiment as well. That is our aim here. We expect that capturing neurtral sentiments for Trump will be difficult as many of his tweets seem neutral but are embedded with back-handed comments that tend to lean negative. Thus, we expect that our model will need feedback to improve and therefore is a great choice for a project with a database that allows feedback from users and then partial fits to the model with that feeback.

Hence, in this project we collect Donald J. Trump's tweets from http://www.trumptwitterarchive.com/ as text. Since the data is unlabeled, first, we analyze Donald Trump 2019's tweets to determine sentiment labels with TextBlob and then build a model to predict sentiment for tweets not in our training set using sklearn and nltk. We then use out-of-core learning to deploy our model to the web using flask and SQLite.

To see our model in action and help contribute data to improve it visit: http://overrunmunn.pythonanywhere.com/
