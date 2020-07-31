import sys

def func(nums) :
    f = 0
    i = 2
    while i <= nums / 2:
        if nums % i == 0:
            f=1
            break
        i=i+1
    
    if f==0:
        return nums;
    else:
        return "False";
def no4a(num):
    num = int(num)
    start = 2;
    count = 0;
    wrt = "";
    while True:
        if func(start) != "False":

            wrt = wrt + str(start);
            count = count+1;
            if(count >= num):
                break;
            else:
                wrt=wrt+",";
        start = start+1

    print(wrt)

if len(sys.argv) !=2:
    print('Needs one argument');
else:
    no4a(sys.argv[1])