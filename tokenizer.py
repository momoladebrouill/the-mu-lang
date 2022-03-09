##converti le programe mu en une liste de tokens, en gros juste pour separer les "mots"


isletter=lambda s:0x61<=ord(s)<=0x7a or 0x41<=ord(s)<=0x7a
isnumber=lambda s:0x30<=ord(s)<=0x39 or s=="."

def tokenize(fil):
    tokens = []
    index = 0
    while index < len(fil):
        car = fil[index]
        #print("Parseig",car,index)
        if car == " ":
            index += 1
            
        if car=="|" and index+1<len(fil):
        	if fil[index+1]=="|":
        		index+=2
        		while not fil[index]==fil[index+1]=="|":
        			index+=1
        		index+=2
        elif car == "<":
            name = ""
            index += 1
            while index < len(fil) and fil[index] != ">":
                name += fil[index]
                index += 1
            index += 1
            tokens.append(Token("balise", name))
        elif isnumber(car):
            text = ""
            while index < len(fil) and isnumber(fil[index]):
                text += fil[index]
                index += 1
            tokens.append(Token("literal", text))
        elif isletter(car):
            text = ""
            while index < len(fil) and (isletter(fil[index]) or isnumber(fil[index])):
                text += fil[index]
                index += 1
            tokens.append(Token("identifier", text))
        else:
        	index+=1
    return tokens

class Token:
    def __init__(self, t, value):
        self.type = t
        self.value = value

    def __repr__(self):
        return f"{self.type}:{self.value}"

if __name__=="__main__":
	print(tokenize("""
<oh>
</br>
3
5
<add>
3 a
</add>
</oh>"""))
