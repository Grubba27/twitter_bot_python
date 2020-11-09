import tweepy
from time import sleep
from keys import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

a = 0

# onde q='#xxxxx', mude para o que vc quiser que fique dando rt.
for tweet in tweepy.Cursor(api.search, q='cachorro').items():
    try:
        print('\ncachorro Bot achou um tuite de @' + tweet.user.screen_name + '. ' + 'retuitando.')
        a = a+1
        print(f'Numero de rts {a}')
        tweet.retweet()

        print('Retweet com sucesso.')

        # pra nao ter spam
        sleep(2)

    # avisar quando da erro.
    except tweepy.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)

    except StopIteration:
        break
