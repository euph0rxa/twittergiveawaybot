import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("SFTCxXNHNWPHXGGUZCLRkVQkPgxcBMWIBIwjgEOm69KZaSPrTS", 
    "g9p5z87Fo2XoUQOHDvsC3VRNU8iOdFEcQifHOJvYXwIUwFZmZT")
auth.set_access_token("1412106496154931202-m4WAWgsxme2V8QaJAmZ0GqKRHOi67x", 
    "zqDo1ywGaCvyg4OTKHsg8oyxy7v4Eem6hwMoyWvv2z6SJ")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

for tweet in api.search(q="NBA Topshot Giveaway", lang="en", rpp=10):
    print(f"{tweet.user.name}:{tweet.text}")
        tweet = tweets[0]
print(f"Liking tweet {tweet.id} of {tweet.author.name}")
api.create_favorite(tweet.id)
