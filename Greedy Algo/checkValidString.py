#Recursion

class Solution:
    def checkValidString(self, s: str) -> bool:
        def f(s,ind,cnt):
            if cnt<0:
                return False
            if ind==len(s):
                return cnt==0
            if s[ind]=='(':
                return f(s,ind+1,cnt+1)
            elif s[ind]==')':
                return f(s,ind+1,cnt-1)
            else:
                return f(s,ind+1,cnt+1) or f(s,ind+1,cnt-1) or f(s,ind+1,cnt)
        return f(s,0,0)

  class Solution:
    def checkValidString(self, s: str) -> bool:
        mini=maxi=0
        for i in range(len(s)):
            if s[i]=="(":
                mini+=1
                maxi+=1
            elif s[i]==")":
                mini-=1
                maxi-=1
            else:
                mini-=1
                maxi+=1
            if mini<0:
                mini=0
            if maxi<0:
                return False
        return mini == 0
