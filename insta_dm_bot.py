from instabot import Bot
from time import sleep

my_bot = Bot()


# login
my_bot.login(username="", password="")
# Method 1
# DM the followers of the user
followers_ids = ["maaxteiger"]

for count, each_follower in enumerate(followers_ids):

    #my_bot.follow(each_follower)
    #sleep(5)
    message_text = "Message test"
    my_bot.send_message(message_text, [each_follower])
    sleep(20)

    my_bot.logout()
