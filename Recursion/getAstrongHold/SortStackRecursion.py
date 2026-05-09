class Solution:

    def sortedInsert(self, s, x):

        if not s or s[-1] <= x:
            s.append(x)
            return

        temp = s.pop()

        self.sortedInsert(s, x)

        s.append(temp)

    def sortStack(self, s):

        if not s:
            return

        temp = s.pop()

        self.sortStack(s)

        self.sortedInsert(s, temp)
