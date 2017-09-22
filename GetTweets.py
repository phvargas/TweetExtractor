import sys
from time import strftime, localtime, time
import twitter

"""
This Python program
  1. takes as a command line argument twitter handle
  2. extract tweets associated with handle
"""
__author__ = 'Plinio H. Vargas'
__date__ = 'Thu,  Sep 14, 2017 at 13:52:33'
__email__ = 'pvargas@cs.odu.edu'


def tweets(handler):   # handler is twitter user name without @ example phone_dude for @phone_dude
    api = twitter.Api(consumer_key='w11PMTOUlj5sGIKjnSII7AcT9',
                      consumer_secret='4if8m3WWrWvHFZ4wHKRXAgrb7mBuRBRboHKUDwoT4AfuoL97hB',
                      access_token_key='3348219965-FBcGASapNIvNxFNGbaIZw1XuE7s4NUIWBwEMN9i',
                      access_token_secret='v2SD9GCRNqr6GTSntP3HgCg14ijw9zMwA0NJ4cPym82TC')

    user = api.GetUser(screen_name=handler)

    """
    Parameters used in GetHomeTimeline twitter API:
       max_id: initialized to 'None' - Returns results with an ID less than (that is, older than) or
               equal to the specified ID.
       count: Specifies the number of statuses to retrieve. May not be greater than 200.
              Variable max_count is initialized to 200 to get max number of tweets allowed.
    """
    current_id = None
    max_count = 200
    counter = 1
    no_exception = True
    while no_exception:
        max_id = current_id

        try:
            #timeline_block = api.GetUserTimeline(user_id=user.id,  count=max_count, max_id=max_id)
            timeline_block = api.GetHomeTimeline(user_id=user.id, count=max_count, max_id=max_id)
            for all_tweets in timeline_block:
                if current_id != all_tweets.id:
                    current_id = all_tweets.id
                    print(counter, all_tweets.text, all_tweets.created_at, all_tweets.id, '\n')
                    counter += 1
                if len(timeline_block) == 1 and current_id == all_tweets.id:
                    print('First ever tweet')
                    no_exception = False

        except twitter.error.TwitterError as e:
            print('We have to wait 15 mins.')
            no_exception = False

    print(handler)

    return

if __name__ == '__main__':
    # checks for argument
    if len(sys.argv) != 2:
        print('Usage: python3 GetTweets.py <twitter-handle>')
        sys.exit(-1)

    # record running time
    start = time()
    print('Starting Time: %s' % strftime("%a,  %b %d, %Y at %H:%M:%S", localtime()))

    # call extract_tweets
    crawled_pages = {}
    tweets(sys.argv[1])
    print('\nEnd Time:  %s' % strftime("%a,  %b %d, %Y at %H:%M:%S", localtime()))
    print('Execution Time: %.2f seconds' % (time()-start))
    sys.exit(0)
