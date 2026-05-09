class Solution:

    def insertBottom(self, s, x):

        if not s:
            s.append(x)
            return

        temp = s.pop()

        self.insertBottom(s, x)

        s.append(temp)

    def reverse(self, s):

        if not s:
            return

        temp = s.pop()

        self.reverse(s)

        self.insertBottom(s, temp)
