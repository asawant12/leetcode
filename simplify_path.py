
# https://leetcode.com/problems/simplify-path/
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        tokens = path.split('/')
        final_path = []
        for index in range(len(tokens)):
            token = tokens[index]
            if token not in ("", "."):
                if token == "..":
                    if len(final_path) > 0:
                        final_path.pop()
                else:
                    final_path.append(token)
        return "/"+"/".join(final_path)
