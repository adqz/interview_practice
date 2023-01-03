from typing import List
import logging


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """Hard
        https://leetcode.com/problems/text-justification/description/
        """
        ans, current_list = [], []
        len_words = 0

        for word in words:
            if len_words + len(word) + len(current_list) > maxWidth:
                # do work
                num_spaces_to_add = maxWidth - len_words
                size = max(1, len(current_list) - 1)  # num gaps between words
                logger.debug(
                    f"current_list={current_list},\
                    num_spaces={num_spaces_to_add},\
                    size={size}")

                # Round robin to add spaces giving left priority over right
                for i in range(num_spaces_to_add):
                    index = i%size
                    current_list[index] += ' '
                
                sentence = "".join(current_list)
                ans.append(sentence)
                logger.debug(f"ans = {ans}")

                # Reset temp variables
                current_list, len_words = [], 0
            
            current_list.append(word)
            len_words += len(word)

        last_sentence = " ".join(current_list).ljust(maxWidth)
        ans.append(last_sentence)

        return ans


s = Solution()
print(s.fullJustify(words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16))

