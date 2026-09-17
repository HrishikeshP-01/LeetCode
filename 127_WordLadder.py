"""
127. Word Ladder
Solved
Hard
Topics
premium lock icon
Companies
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
"""

class Solution:
    """
    BFS Search
    This is a Leetcode hard & the reason for this is it fails if the 
    Time complexity of the adjacent list exceeds O(n.m^2)

    Without that it'd have been straightforward:
    1. Create adjacency list where each word is mapped to the possible words
    i.e, words with only 1 character difference. Time Complexity = O(m.n^2)
    2. Run BFS on the start word till the end word is reached. Time Complexity = O(m.n^2)
    
    But how can we reduce the time complexity of Step 1?
    - Look at the constraints:
        Each word has the same length
        Word lengths are less than 10
        But word count is between 0-5000

    - If we were to use the words to create adjacency list
        We'll have to compare each word with every other word. 
        Let m-> word len & n-> word count
        Time complexity = m.n.n = O(m.n^2)

    - But what if we use the word length to our advantage?
        Every word has the same length
        There are words that differ by only 1 character
        Meaning If a word is AAAA
        There could be other words that fit the pattern:
        *AAA, A*AA, AA*A, AAA*
        All words that fit a pattern are connected to each other & can be traversed
        For a word with length m, there are m patterns & we have to check n words to 
        find if the word matches the pattern making T.C = m.m.n = O(n.m^2)

    - Then we use a BFS algorithm to find the path from begin word to end word
    Why not DFS? Because BFS is often more straighforward for unweighted path problems than DFS

    Lessons learned:
    1. Always look at the constraints & think about complexity before jumping into the problem
    2. Optimize beforehand, use reverse thinking approach

    REFER TO ADDITONAL QUESTIONS BELOW AFTER GOING THROUGH THE CODE
    """
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        hashmap = collections.defaultdict(list)
        wordLen = len(wordList[0])
        for w in wordList:
            for i in range(wordLen):
                pattern = w[0:i]+'*'+w[i+1:]
                hashmap[pattern].append(w)
        
        q = collections.deque()
        q.append(beginWord) # Important for 2 reasons: 
        # 1. We need a starting point for BFS
        # 2. Check constraints: begin might not be part of the list so add it to the queue
        hashset = set()
        hashset.add(beginWord)
        path=1 # Why is path 1 & not 0
        while q:
            for i in range(len(q)):
                w = q.popleft()
                if w==endWord:
                    return path
                for i in range(wordLen):
                    pattern = w[0:i]+'*'+w[i+1:]
                    if pattern in hashmap:
                        for x in hashmap[pattern]:
                            if x not in hashset:
                                q.append(x)
                                hashset.add(x)
            path+=1
            print(path)
        return 0
        
"""
Why is Path = 1?
The return value the question is expecting is not the path but the transitions required
to go from begin word to end word.
e.g:
Let begin = a, stop = a
Transitions = [a] 
Result = 1
Let begin = hit, stop = hot [hot, pot, dot]
Transitions = [hit, hot]
Result = 2
The path=0 in a BFS calculates the number of edges traversed. 
But what we want is the number of nodes, 
the number of nodes visited = total edges traversed + 1
So we initialize path=1 to get the number of nodes.
"""