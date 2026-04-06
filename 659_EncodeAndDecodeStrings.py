"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
    // ... your code
    return encoded_string;
}
Machine 2 (receiver) has the function:

vector<string> decode(string s) {
    //... your code
    return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

Example 1:

Input: dummy_input = ["Hello","World"]

Output: ["Hello","World"]

Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
Example 2:

Input: dummy_input = [""]

Output: [""]

Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains any possible characters out of 256 valid ASCII characters.
"""


class Solution:
    """
    This is  a design problem
    We need to represent several strings as a single string & decode them back
    How do we know when a string starts & when it ends?
    Trial 1:
    Seperate strings using a delimeter
    Problem: What if the delimeter is part of the string
    Trial 2:
    Store the word length at the beginning of the string
    Then extract that number of characters
    Problem: What if number is part of a string
    Correct Approach:
    Store the word length first, then a delimeter
    Then extract that number of characters no matter what they are
    E.g: 4#bird6#Co#4de
    = [bird, Co#4de]
    """

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for s in strs:
            encoded_str = len(s) + '#' + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i<len(s): # Pointer i represents beginning of the lenght of the word
            j = i
            while s[j] != '#': # Extract numbers until the delimeter is hit
                j+=1
            word_length = int(s[i:j]) # j points to '#'  so all characters till j
            word = s[j+1 : j+1+word_length] # j points to '#' so start from j+1
            res.append(word)
            i = j+1+word_length # new word length 