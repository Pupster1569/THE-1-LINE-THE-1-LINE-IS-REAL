# https://www.codewars.com/kata/526989a41034285187000de4/train/python
def ips_between(start, end): return sum(part * (256 ** (3 - i)) for i, part in enumerate(map(int, end.split('.')))) - sum(part * (256 ** (3 - i)) for i, part in enumerate(map(int, start.split('.'))))

print(ips_between("58.123.169.0","71.46.35.137"))