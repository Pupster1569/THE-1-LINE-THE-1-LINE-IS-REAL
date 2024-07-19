# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python
def make_readable(seconds): return f"{0 if int((seconds/60)/60) < 10 else ''}{int(seconds/3600)}:{0 if int((seconds/3600-int(seconds/3600))*60) < 10 else ''}{int((seconds/3600-int(seconds/3600))*60)}:{0 if seconds-(60*int(seconds/60)) < 10 else ''}{seconds-(60*int(seconds/60))}"

print(make_readable(3599))