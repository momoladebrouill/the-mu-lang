##converti une liste de tokens créé par le tokenizer.py, en en arbre AST facile a interpreter
##un truc genre  https://www.researchgate.net/profile/Thang-Huynh-Quyet/publication/300802898/figure/fig1/AS:723808830894081@1549580881995/Abstract-syntax-tree-of-Euclide-function.png

from nodes import newnode,Ind

class Brick:
	def __init__(self,v):
		self.v=v
		self.down=None
		
	def history(self):
		if self.down==None:
			return [self]
		else:
			return [self]+self.down.history()
		
class Pile:
	def __init__(self,t='FIRST'):
		self.tete=Brick(t)
		
	@property
	def top(self):
		return self.tete.v
		
	def add(self,zarma):
		new=Brick(zarma)
		new.down=self.tete
		self.tete=new
		
	def pop(self):
		self.tete=self.tete.down
		
	def __repr__(self):
		return ','.join(str(s) for s in self.tete.history())
		

def parse(tokens:list):
	ouverts=Pile(newnode(tokens[0]))
	for token in tokens:
		if token.type=="balise":
			if token.value[0]=="/":
				ouverts.pop()
				# Pour enlever les indiciums du tronc (il est aussi attaché dans l'objet itéré dans l'attribut "consult")
				if ouverts.top.childs[-1]==Ind:
					ouverts.top.childs.pop()
			else:
				
				if token.value[-1]=="/":
					# Balise autofermante
					token.value=token.value[:-1]
					new=newnode(token)
					ouverts.top.childs.append(new)
				else:
					new=newnode(token)
					ouverts.top.childs.append(new)
					# Enregistrer l'indice dans l'objet itéré
					if new.REPR=="Indicium":ouverts.top.childs[-1].consult=new
					ouverts.add(new)
		else:
			ouverts.top.childs.append(newnode(token))
	return ouverts.top
