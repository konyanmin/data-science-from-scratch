def double(x):
    return x * 2

def apply_to_one(f):
    return f(1)

my_double = double
x = apply_to_one(my_double)

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(x[1:6])

def sum_and_deduct(x, y):
    return (x + y), (x - y)

y = sum_and_deduct(44, 37)

# print(y)

tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet_keys   = tweet.keys()     # iterable for the keys
tweet_values = tweet.values()   # iterable for the values
tweet_items  = tweet.items()    # iterable for the (key, value) tuples

print(tweet_keys)
print(tweet_values)
print(tweet_items)
print("user" in tweet)