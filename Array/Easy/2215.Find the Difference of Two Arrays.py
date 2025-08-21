def encrypt(txt):
    binary=''.join(format(ord(char), '08b') for char in txt)
    mp={'0':'\u200C', '1': '\u200D'}
    
    ans=[]
    for i in binary:
        ans.append(mp[i])
    f=open("dummy.txt","w")
    f.write(binary)
    f.close()
    
    hidden_txt=''.join(mp[bit] for bit in binary)
    return hidden_txt , ans

def decrypt(hidden):
    mp={'\u200C':'0', '\u200D':'1'}
    binary=''.join(mp[char] for char in hidden if char in mp)
    
    return ''.join(chr(int(binary [i:i+8],2)) for i in range (0,len(binary),8))

def main():
    text=input("Enter plain text :")
    
    hidden,ans=encrypt(text)
    print("\nhidden:", hidden,"it is hidden the cipher text is below\n","\nhidden_value",ans)
    
    decoded=decrypt(hidden)
    print("\ndecoded:", decoded)

if __name__=="__main__":
    main()