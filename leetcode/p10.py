# ----------------------- UNSOLVED -----------------------
# @author: adnan
# Problem 71. Simplify Path (Medium)

class Solution(object):
    def simplifyPath(self, path):
        """
        Given an absolute path for a file (Unix-style), 
        simplify it. Or in other words, convert it to the canonical path.

        In a UNIX-style file system, a period . refers to the current directory. 
        Furthermore, a double period .. moves the directory up a level. 
        For more information, see: https://www.linuxnix.com/abslute-path-vs-relative-path-in-linuxunix/
        
        Note that the returned canonical path must always begin with a slash /, 
        and there must be only a single slash / between two directory names. 
        The last directory name (if it exists) must not end with a trailing /. 
        Also, the canonical path must be the shortest string representing the absolute path

        Input: "/home/"
        Output: "/home"
        Explanation: Note that there is no trailing slash after the last directory name.

        Example 1:

        Input: "/home/"
        Output: "/home"
        Explanation: Note that there is no trailing slash after the last directory name.
        
        Example 2:

        Input: "/../"
        Output: "/"
        Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
        
        Example 3:

        Input: "/home//foo/"
        Output: "/home/foo"
        Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
        
        Example 4:

        Input: "/a/./b/../../c/"
        Output: "/c"
        
        Example 5:

        Input: "/a/../../b/../c//.//"
        Output: "/c"
        
        Example 6:

        Input: "/a//b////c/d//././/.."
        Output: "/a/b/c"
        
        :type path: str
        :rtype: str
        """
        assert isinstance(path, str)
        stack = ['/']
        newDir = ''
        for char in path:
          if char in ['.', '/']:
            instructionFlag = True
          else:

              newDir += stack.pop()

        
  
if __name__ == '__main__':
  # ------ Test Cases ------
  s = Solution()
  print(s.simplifyPath('/home/'))
        