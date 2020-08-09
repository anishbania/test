for x in range(1000):
    ax=x
    an=x
    i=0
    sume=0
    while x!=0:
        r=x%10
        i+=1
        x=x//10
    while ax!=0:
        r=ax%10
        sume=sume+pow(r,i)
        ax=ax//10
    if sume==an:
        print(an)
