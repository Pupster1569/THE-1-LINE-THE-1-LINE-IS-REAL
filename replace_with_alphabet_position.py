# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

# def alphabet_position(text): return "".join([(str(ord(i)-96)+" " if ord(i)-96 > 0 else "") for i in [*text.lower()]]).strip()
def alphabet_position(text): return " ".join([str(ord(i)-96) for i in text.lower() if i.isalpha()])

print(alphabet_position("The sunset sets at twelve o' clock."))