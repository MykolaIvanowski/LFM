# make a class like twitter
# it should have a methods:
#   void postTweet(int userId, int tweetId) -  Publish a new tweet with ID tweetId by the user userId.
#   List<Integer> getNewsFeed(int userId) - Fetches at most the 10 most recent tweet IDs in the user's news feed.
#   void follow(int followerId, int followeeId) - The user with ID followerId follows the user with ID followeeId.
#   void unfollow(int followerId, int followeeId) - The user with ID followerId unfollows the user with ID followeeId.
#
# Input:
# ["Twitter", "postTweet", [1, 10], "postTweet", [2, 20], "getNewsFeed", [1], "getNewsFeed", [2], "follow", [1, 2], "getNewsFeed", [1], "getNewsFeed", [2], "unfollow", [1, 2], "getNewsFeed", [1]]
#
# Output:
# [null, null, null, [10], [20], null, [20, 10], [20], null, [10]]
#
# Explanation:
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 10); // User 1 posts a new tweet with id = 10.
# twitter.postTweet(2, 20); // User 2 posts a new tweet with id = 20.
# twitter.getNewsFeed(1);   // User 1's news feed should only contain their own tweets -> [10].
# twitter.getNewsFeed(2);   // User 2's news feed should only contain their own tweets -> [20].
# twitter.follow(1, 2);     // User 1 follows user 2.
# twitter.getNewsFeed(1);   // User 1's news feed should contain both tweets from user 1 and user 2 -> [20, 10].
# twitter.getNewsFeed(2);   // User 2's news feed should still only contain their own tweets -> [20].
# twitter.unfollow(1, 2);   // User 1 follows user 2.
# twitter.getNewsFeed(1);   // User 1's news feed should only contain their own tweets -> [10].
#
import heapq
from collections import defaultdict
from typing import List



class Twitter:
    def __init___(self):
        self.count = 0
        self.tweet_map = defaultdict(list) #
        self.follow_map = defaultdict(set) #

    def post_tweet(self, user_id: int, tweet_id: int)-> None:
        # every tweet in tweet map have his onw uniq id and count (simply time_tweet)
        self.tweet_map[user_id].append([self.count, tweet_id])

        self.count -= 1 # use for prioritise queue, as we can use only min heap then we use decrement

    def get_news_feed(self, user_id: int)-> List[int]:
        result = []
        min_heap = []

        self.follow_map[user_id].add(user_id) # for tracking youself, feeed news include you feeds

        # iterate thoug follower, check if followers have a tweeet
        # and then push tweets into the heap in most resent order
        for followee_id in self.follow_map[user_id]:
            if followee_id in self.tweet_map:
                index = len(self.tweet_map[followee_id]) - 1
                count, tweet_id  = self.tweet_map[followee_id][index]
                # push tweet into the heap with foolowee_id and the index of the next order tweet
                heapq.heappush(min_heap, [count, tweet_id,followee_id, index-1])

        # take 10 tweets and extract them from heap to result
        while min_heap and len(result) < 10:
            # cutial heap will pop set with min count, this is the chronological marker
            count, tweet_id, followee_id, index = heapq.heappop(min_heap)
            result.append(tweet_id)
            if index >= 0:
                # push the next tweet from follower (if available) in chronological order for tweets
                # count and heap help do it in chronological order
                count,tweet_id = self.tweet_map[followee_id][index]
                heapq.heappush(min_heap, [count,tweet_id, followee_id,index-1])

        return result

    def follow(self, follower_id: int, followee_id: int)-> None:
        # follow somebody
        self.follow_map[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int)-> None:
        # check if  followee_id in follow map or in other case should manage key error
        if followee_id in self.follow_map[follower_id]:
            self.follow_map[follower_id].remove(followee_id)

