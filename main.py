import tokenizer
import parser


hw=open("./muPrograms/fibonacci.µ","r")

tokens = tokenizer.tokenize(hw.read())
print(tokens)
node=parser.parse(tokens)
print("# Execution dµ script !!! :")
node.action({})
