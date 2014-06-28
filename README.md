# twitterbot

A Python framework for creating interactive Twitter bots! CURRENTLY SUPER BETA.

## Installation

Due to dependencies on [Tweepy](https://github.com/tweepy/tweepy), twitterbot only supports Python 2.7 and *not*
Python 3. Sorry :(

I recommend setting it up in a virtualenv, because, well, yeah.

``` bash
mkdir bots && cd bots
virtualenv-2.7 venv && source venv/bin/activate
pip install tweepy
git clone https://github.com/thricedotted/twitterbot.git
cd twitterbot && python setup.py install && cd ..
```

Cool! you're ready to start using twitterbot!


## Getting Started

1. Follow Steps 3-5 of [this bot
   tutorial](http://blog.boodoo.co/how-to-make-an-_ebooks/) to create an
   account and obtain credentials for your bot.

2. Copy the template folder from `twitterbot/examples/template` to wherever
   you'd like to make your bot, e.g. `cp -r twitterbot/examples/template
   my_awesome_bot`.

3. Open the template file in `my_awesome_bot` in your favorite text editor.
   Many default values are filled in, but you MUST provide your API/access
   keys/secrets in the configuration in this part. There are also several
   other options which you can change or delete if you're okay with the
   defaults.

4. The methods `on_scheduled_tweet`, `on_mention`, and `on_timeline` are what
   define the behavior of your bot, and deal with making public tweets to your
   timeline, handling mentions, and handling tweets on your home timeline
   (e.g., from accounts your bot follows) respectively.

   Some methods that are useful here:
   ```
   self.post_tweet(text)                    # post some tweet
   self.post_tweet(text, reply_to=tweet)    # respond to a tweet

   self.favorite(tweet)                     # favorite a tweet

   self.log(message)                        # write something to the log file
   ```

   Remember to remove the `NotImplementedError` exceptions once you've
   implemented these! (I hope this line saves you as much grief as it would
   have saved me, ha.)

5. Once you've written your bot's behavior, run the bot using `python
   mytwitterbot.py &` (or whatever you're calling the file) in this directory.
   A log file corresponding to the bot's Twitter handle should be created; you
   can watch it with `tail -f <bot's name>.log`.

Check the `examples` folder for some silly simple examples.
