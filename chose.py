a = [1,18,17,23,15,16]

def chose_sort(a,issmalltobig=True,debug=False):
    if debug:
        print('原始列表：',a)
    count = len(a)
    times = 0
    for i in range(count-1):
        k = i
        for j in range(i,count):
            if issmalltobig:
                if a[k] > a[j]:
                    k = j
            else:
                if a[k] < a[j]:
                    k = j
        iisk = i != k
        if iisk:
            a[k],a[i] = a[i],a[k]
            times += 1
        if debug:
            if iisk:
                needswap = '需要'
            else:
                needswap = '不需要'
            
            print('第{}次，{}交换，比较了{}次，结果为{}。'.format(i+1,needswap,count-i-1,a))
            
    return a,times,' '
print(chose_sort(a,False,False)[0])