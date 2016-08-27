#from twitter_feed import twitterData,tweetData,saveTweets#not need
#from mysql.connector import connect, Error# not need
from files.db_query import saveTweets

twitter_id = "@trafficjamjen"
numbr_of_tweets = 200

saveTweets(twitter_id,numbr_of_tweets)