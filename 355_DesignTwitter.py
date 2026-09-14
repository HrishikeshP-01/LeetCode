"""
355. Design Twitter
Solved
Medium
Topics
premium lock icon
Companies
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
 

Example 1:

Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
 

Constraints:

1 <= userId, followerId, followeeId <= 500
0 <= tweetId <= 104
All the tweets have unique IDs.
At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
A user cannot follow himself.
"""

class Twitter:
    """
    This problem is about going through the requirements & deciding what data structures to use

    Let's start with the least complicated problem:
    How to keep track of the followers?
    1. We can use a map to keep track of the people the user is following
    2. What if we use a list to store the people the user is following?
        Easy to implement but unfollowing people becomes complicated
        What if a user tries to follow the same person twice?
    It's a lot more easier to use a Set. Insertion & Deletion is O(1) & no duplicates
    So for follwoing: Just add an id to a set
    For unfollowing: Remove an id from a set if it's present in the set

    How to post tweets?
    We could map each person's tweet to their id
    But we also need to know which is the latest tweet not just w.r.t the user
    but also w.r.t the entire app
    We can use a Count variable to denote at which point in time the tweet was posted
    So for post tweet we map userID -> [count, tweetId]

    How to get news feed?
    There are 2 approaches we can use:
    1. Intuitive - Merge K sorted lists
    We have the list of tweets by all the people a user is following
    In these lists we also store the 'count' that denotes which tweet was the most frequent
    Say we have k such lists, we just have to populate result such that the 10 most recent tweets
    are pushed into it & returned

    2. Max Heap approach
        Since we want the latest tweet we either store the -count to the list
        or it's easier to just decrement the count with each post
        so the lowest negative value signifies the latest tweet (as python only provides a min heap implementation we do this)

        Now for each person a user follows we store:
            count - signifies at what time the tweet was posted
            tweetId
            followeeId - will be used in the next step to find the next most recent tweet by this user
            index - 1 : The tweet of this user that will be considered in the next step
        into the minHeap

        Heapify this so that the most latest tweet is in the 0th position

        While the heap is not empty and len(res) < 10:
            (Edge case: If total tweets are < 10 heap can be empty so we must catch this)
            1. Pop an element from the heap
            this signifies the latest tweet
            2. Insert it into res
            3. Now if the person who posted this tweet has other tweets, they could 
            be more recent that what's present in heap at this moment, they need to be considered
            So:
                we use the index value (this signifies the next tweet to be considered)
                and followee id to fetch that tweet
            Edge case here:
                Do step 3 only if index >= 0. If index < 0 it means there are no more tweets 
                for a poster left to be considered 
            4. Push it into the heap along with the count, followee ID & the next tweet to be 
            considered (index -1)
            5. Return res  
    """
    def __init__(self):
        self.following = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        self.tweetMap[userId].append([self.count, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        self.following[userId].add(userId)

        res = []
        minHeap = []

        for followeeId in self.following[userId]:
            if self.tweetMap[followeeId]:
                index = len(self.tweetMap[followeeId])-1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index-1])
        
        heapq.heapify(minHeap)
        #print(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index-1])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)