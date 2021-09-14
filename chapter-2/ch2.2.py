import numpy as np

def main():
    fr = open("example2.1.csv", 'r')
    y=list()
    x=list()
    for line in fr.readlines():
        curLine = line.strip().split(',')
        x.append(curLine[:-1])
        y.append(curLine[-1])
    x=np.array(x,dtype=np.float64)
    y=np.array(y,dtype=np.float64)
    Gram=np.dot(x,x.T)
    alpha = np.zeros(len(x), np.float64)
    b=0
    lr=1
    iter_count=0
    while True:
        loop=False
        for i in range(len(x)):
            if y[i] * (sum([y[j]*alpha[j]*Gram[j][i] for j in range(len(x))]) + b) <= 0:
                alpha[i] += lr
                b += y[i]*lr
                loop=True
                print(i+1,alpha,b)
        iter_count+=1
        if loop==False :
            break
if __name__ == '__main__':
    main()