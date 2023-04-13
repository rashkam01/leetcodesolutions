#!/bin/python3


from datetime import datetime

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if (s[:2] == '12' and s[-2:] == 'AM'):
        return('00' + s[2:-2])
    elif (s[:2] == '12' and s[-2:] == 'PM'):
        return(s[:8])
    elif(s[:2] >= '01' and s[:2] <= '11' and s[-2:] == 'AM'):
        return(s[:8])
    else:
        #in3 = s[:2]
        #intfirst = int(in3) + 12
        #add12 = str(int(s[:2]) + 12)
        return(str(int(s[:2]) + 12) + s[2:8])


if __name__ == '__main__':
    #Sample Test Case 1 
    stdinp1 = '11:05:45AM'
    result = timeConversion(stdinp1)
    print(result)


    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #s = input()

    #result = timeConversion(s)

    #fptr.write(result + '\n')

    #fptr.close()