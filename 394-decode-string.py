class Solution:
    def decodeString(self, s: str) -> str:
        lowercases='abcdefghijklmnopqrstuvwxyz'
        digits='0123456789'
        
        def helper(subs):
            #scan:
            #1. [ push into stack, store digits before it with [
            #2. ] pop stack, whatever in between repeat, append to letterstor
            #3. meet letter append to letterstor
            digitstor=""
            curr=""
            st = deque()
            for ch in s:
                
                if(ch=='['):
                    num = int(digitstor)
                    st.append((num,curr))
                    curr=""
                    digitstor=""
                    continue
                elif(ch==']'):
                    num = st[-1][0]
                    prev_item = st[-1][1]
                    st.pop()
                    #repeat num times
                    for i in range(num):
                        prev_item+=curr
                    curr=prev_item
                    digitstor=""
                    continue
                elif(ch in digits):
                    digitstor+=ch
                                 
                elif(ch in lowercases):
                    curr+=ch

            
            return curr
        rslt = helper(s)
        return rslt