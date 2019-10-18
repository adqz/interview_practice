# @author: adnan
# Problem No. 535. Encode and Decode TinyURL (Medium)
'''
Runtime: 20 ms, faster than 71.01% of Python online submissions for Encode and Decode TinyURL.
Memory Usage: 11.8 MB, less than 64.29% of Python online submissions for Encode and Decode TinyURL.
'''
class Codec:
    def __init__(self):
      self.store = dict()
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        tinyURL = 'http://tinyurl.com/' + str(hash(longUrl))
        self.store[tinyURL] = longUrl
        return tinyURL
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.store[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

if __name__ == '__main__':
  # ------ Test Cases ------
  codec = Codec()
  url1 = 'https://leetcode.com/problems/design-tinyurl'
  tiny = codec.encode(url1)
  print(tiny)
  longURL = codec.decode(tiny)
  print(longURL == url1)