'''What is the index of the first term in the Fibonacci sequence to contain 1000 digits?'''

f1 = 1
f2 = 1

def function(nDigits):
    fnminus2 = f1
    fnminus1 = f2
    found = False
    index = 3
    while found == False:
        fn = fnminus1 + fnminus2
        if len(str(fn)) >= nDigits:
            print(index)
            found = True
        else:
            fnminus2 = fnminus1
            fnminus1 = fn
            index += 1

if __name__ == '__main__':
    function(1000)