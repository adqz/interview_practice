'''
@author: adnan
Problem 151. Reverse Words in a String

Runtime: 268 ms, faster than 12.75% of Python3 online submissions for Design Twitter.
Memory Usage: 18.1 MB, less than 52.63% of Python3 online submissions for Design Twitter.
'''
from typing import List
from collections import defaultdict
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.all_tweets = []
        self.following = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet. Saves from least recent at index 0 to most recent at index n
        """
        self.all_tweets.append((userId, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        tweet_count = 0
        most_recent_tweets = []
        for tweet_of_userId, tweetId in reversed(self.all_tweets):
            # If the tweet posted is someone the user follows or is the user itself
            if tweet_of_userId in self.following[userId] or tweet_of_userId == userId:
                most_recent_tweets.append(tweetId)
                tweet_count += 1
            if tweet_count >= 10:
                break
        
        return most_recent_tweets
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId not in self.following[followerId]:
            self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        

if __name__ == "__main__":
    twitter = Twitter()

    # User 1 posts a new tweet (id = 5).
    twitter.postTweet(1, 5)

    # User 1's news feed should return a list with 1 tweet id -> [5].
    twitter.getNewsFeed(1)

    # User 1 follows user 2.
    twitter.follow(1, 2)

    # User 2 posts a new tweet (id = 6).
    twitter.postTweet(2, 6)

    # User 1's news feed should return a list with 2 tweet ids -> [6, 5].
    # Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
    print(twitter.getNewsFeed(1))

    # User 1 unfollows user 2.
    twitter.unfollow(1, 2)

    # User 1's news feed should return a list with 1 tweet id -> [5],
    # since user 1 is no longer following user 2.
    print(twitter.getNewsFeed(1))