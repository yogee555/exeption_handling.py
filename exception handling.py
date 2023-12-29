try:
    a=10
    b="10"
    c=a+b
    print(8/0)
#except zerodivisionerror as err:
    #print("please don't provide 0 in the denomenator")
except TypeError as err:
    print("error occours while execution because you are providing str instead of int")
    print(err)
except exception as err:
    print("exception occours please check the code")
    print(err)