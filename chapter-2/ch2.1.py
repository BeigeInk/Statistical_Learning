import numpy as np

def main():
    #np.loadtxt("example2.1.csv",dtype=np.int,delimiter=',')

    fr = open("example2.1.csv", 'r')
    y=list()
    x=list()
    for line in fr.readlines():
        curLine = line.strip().split(',')
        x.append(curLine[:-1])
        y.append(curLine[-1])
    x=np.array(x,dtype=np.float64)
    y=np.array(y,dtype=np.float64)
    w=np.zeros((1,len(x[0])))
    b=0
    iter_count=0
    print(iter_count, " ", w, b)
    while True:
        loop=False
        wrong_tag=0
        for j in range(len(x)):
            if y[j]*(np.dot(w, x[j].T)+b)<=0:
                w=w+y[j]*x[j]
                b=b+y[j]
                loop=True
                wrong_tag=j+1
                break
        iter_count+=1
        print(iter_count,wrong_tag,w,b)
        if loop==False:
            break

if __name__ == '__main__':
    main()