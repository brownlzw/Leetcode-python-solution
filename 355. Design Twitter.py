from collections import defaultdict
class Twitter(object):
  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.tidGlobal = -1
    self.tweets = defaultdict(list)
    self.follows = defaultdict(set)

  def postTweet(self, userId, tweetId):
    """
    Compose a new tweet.
    :type userId: int
    :type tweetId: int
    :rtype: void
    """
    self.tidGlobal += 1
    self.tweets[userId].append((tweetId, self.tidGlobal))
    return

  def getNewsFeed(self, userId):
    """
    Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
    :type userId: int
    :rtype: List[int]
    """
    if userId not in self.follows[userId]:
      self.follows[userId].add(userId)
    tts = []
    for i in self.follows[userId]:
      if i in self.tweets:
        tts += self.tweets[i][-10:]
    tts.sort(key=lambda v: -v[1])
    return [v[0] for v in tts[: 10]]

  def follow(self, followerId, followeeId):
    """
    Follower follows a followee. If the operation is invalid, it should be a no-op.
    :type followerId: int
    :type followeeId: int
    :rtype: void
    """
    if followerId >= 0 and followeeId >= 0 and followeeId != followerId:
      self.follows[followerId].add(followeeId)
    return

  def unfollow(self, followerId, followeeId):
    """
    Follower unfollows a followee. If the operation is invalid, it should be a no-op.
    :type followerId: int
    :type followeeId: int
    :rtype: void
    """
    self.follows[followerId].discard(followeeId)
    return