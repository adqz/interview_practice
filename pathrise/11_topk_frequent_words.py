### ------------------------------------- Top k frequent words problem ------------------------------------- 
from collections import Counter, defaultdict
def top_k_words(words, k):
    '''
    Brute Force Solution (partially working)
    Time: O(nlog(k))
    Space: O(n + n + k) = O(n)
    Here n = number of words, k = max number of unique words
    
    Smarter Solution: Min Time has to be O(n) for us to see the frequency of each word
    Min Space has to be O(n) too to store the count of each word
    '''
    count = Counter(words)
    all_counts = sorted(list(set(count.values())), reverse=True)
    inverse_map = defaultdict(list)
    ans = []
    
    for word in words:
        frequency = count[word]
        if word not in inverse_map[frequency]: 
            inverse_map[frequency].append(word)

    counter = 0
    for freq in all_counts:
        words_temp = sorted(inverse_map[freq])
        for w in words_temp:
            if counter < k:
                ans.append(w)
                counter += 1
            else:
                return ans

    
if __name__ == '__main__':
    # print(top_k_words(["hello", "i", "love", "pathrise", "i", "love", "coding"], k = 2))
    print(top_k_words(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4)) #not working### ------------------------------------- Top k frequent words problem ------------------------------------- 

from collections import Counter, defaultdict
def top_k_words(words, k):
    '''
    Brute Force Solution (partially working)
    Time: O(nlog(k))
    Space: O(n + n + k) = O(n)
    Here n = number of words, k = max number of unique words
    
    Smarter Solution: Min Time has to be O(n) for us to see the frequency of each word
    Min Space has to be O(n) too to store the count of each word
    '''
    count = Counter(words)
    all_counts = sorted(list(set(count.values())), reverse=True)
    inverse_map = defaultdict(list)
    ans = []
    
    for word in words:
        frequency = count[word]
        if word not in inverse_map[frequency]: 
            inverse_map[frequency].append(word)

    counter = 0
    for freq in all_counts:
        words_temp = sorted(inverse_map[freq])
        for w in words_temp:
            if counter < k:
                ans.append(w)
                counter += 1
            else:
                return ans

    
if __name__ == '__main__':
    # print(top_k_words(["hello", "i", "love", "pathrise", "i", "love", "coding"], k = 2))
    print(top_k_words(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4)) #not working