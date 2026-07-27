import collections
import heapq

class Twitter:

    def __init__(self):
        # Global tracker to maintain chronological ordering of tweets
        self.timestamp = 0
        
        # Maps userId to a list of pairs: (timestamp, tweetId)
        self.tweets = collections.defaultdict(list)
        
        # Maps userId to a set of followeeIds
        self.followees = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Decrement timestamp so smaller values represent more recent tweets (for min-heap)
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        min_heap = []
        
        # A user always sees their own tweets, so temporarily add self to followees
        user_list = list(self.followees[userId]) + [userId]
        
        for f_id in user_list:
            if f_id in self.tweets:
                # Get the absolute index of the most recent tweet
                index = len(self.tweets[f_id]) - 1
                time, tweet_id = self.tweets[f_id][index]
                # Store (timestamp, tweetId, followeeId, index_of_next_tweet)
                min_heap.append((time, tweet_id, f_id, index - 1))
                
        # Turn list into a heap structure
        heapq.heapify(min_heap)
        
        while min_heap and len(res) < 10:
            time, tweet_id, f_id, idx = heapq.heappop(min_heap)
            res.append(tweet_id)
            
            # If the same user has more tweets left, push the next recent one into the heap
            if idx >= 0:
                next_time, next_tweet_id = self.tweets[f_id][idx]
                heapq.heappush(min_heap, (next_time, next_tweet_id, f_id, idx - 1))
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)
