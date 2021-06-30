from datetime import datetime

def gen(seed:float=None):
    """
    Returns a random number between 0 and 1.
    """
    if seed != None:
        generated_num = 0
        seed = seed/(10**len(str(seed)))
        count = 0
        for i in range(49, 100):
            num = seed/i
            generated_num += num/(10**count)
            count+=1
        return generated_num*10
    else:
        d = datetime.now()
        return d.microsecond/1000000+d.second/100000000+d.hour/10000000000