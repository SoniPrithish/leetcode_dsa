class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1:
            return 1
        n=len(chars)
        read=0
        write=0
        while(read<n):
            
            ch=chars[read]
            count=0
            while(read<n and chars[read]==ch):
                count+=1
                read+=1
            chars[write]=ch
            write+=1

            if count>1:
                s=str(count)
                for digit in s:
                    chars[write]=digit
                    write+=1
            
        return write
