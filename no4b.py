import sys



def set_var(value,limit):
    if len(value) > limit:
        return value[limit]
    else:
        return "NULL"

def no4b(Input1,Input2):

    array1 = Input1.split(',')
    array2 = Input2.split(',')
    array2 = sorted(array2)
    array1 = sorted(array1)
    limit =0;

    if len(array1) > len(array2):
        limit = len(array1);
    else:
        limit = len(array2);

    wrt = "";
    for i in range(0,limit,1):
        #print("[",'NULL' if len(array1) <= i-1 else array1[i], ':', 'NULL' if len(array2) <= i else array2[i],"]", end = "," )
        wrt = wrt + "[" + set_var(array1,i) + ':' + set_var(array2,i) + "]"
        if(i<limit-1):
            wrt = wrt + ","
        #print("[",'NULL' if len(array1) <= i-1 else array1[i], ':',"]", end = "," )
    print(wrt)

if len(sys.argv) !=3:
    print('Needs two argument');
else:
    no4b(sys.argv[1], sys.argv[2])