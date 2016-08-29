# This file will contain all database configuration, also the key for twitter api

class Configurations:
	#db configuration
	userName = 'root'#user name for database
	password = 'XXXXXXX' # password for database
	hostIP ='127.0.0.1' #IP in my case its locally hosted
	databaseName = 'twitterdata'
	raise_on_warnings = True

	dbconfig = {
		'user': userName,
		'password': password,
		'host': hostIP,
		'database': databaseName,
		'raise_on_warnings': True,
	}
	def dbApiConfig(self):
		# return db configuration
		return self.dbconfig

	# to get api key you first need to set your app
	# for more https://apps.twitter.com/app/new
	#twitter api configuration
	consumer_key = "XXXXXXXX"
	consumer_secret = "XXXXXXXXXXXXXXXXXXX"
	access_token = "2XXXXXXXXXXXXXXXxO"
	access_token_secret = "qXXXXXXXXXXXXXXXXXXXYl"
	twitter_config = consumer_key,consumer_secret,access_token,access_token_secret

	def twitterApiConfig(self):
		# return twitter api configuration
		return self.twitter_config

if __name__ == "__main__":
	config = Configuration()
	print config.twitterApiConfig()
