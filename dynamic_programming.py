

def edit_string_dist(X,Y,δ, α):
    m = len(X)
    n = len(Y)
    Opt = [[] for x in range(m) for y in range(n)]
    for x in range(0, m):
        Opt[x][0]= x*δ
    for y in range(0, n):
        Opt[0][y]= y*δ
    for i in range(1,m):
        for j in range(1,n):
            Opt[i][j] = min(α + Opt[i-1][j-1], δ + Opt[i-1][j],  δ + Opt[i][j-1])
            #first argument is if they are both in M, the cost of mismatch plus cost to align prefix strings before them
            #second is if i isnt in M, gap cost plus cost to align the prefix string before i with j
            #third is if j isnt in M, gap cost plus cost to align the prefix string before j with i 
    return Opt[m,n]


def log_cutting(n, prices):
    cut = []
    choices= [0 for x in range(n)]
    cut.append(0) # cut[0]=0
    for x in range(1,n):
        best = 0
        for y in range(1, x):
            best = max(best, cut[x-y] + prices[y])
            choices[x]=y
        cut[x]= best
    return cut[n]

def print_choices(choices, n):
    i = n
    while i > 0:
        print(choices[i])
        i -= choices[i]

    
def discrete_knapsack(v,w,c,n):
    #input --> n is number u are checking
    # w is changing capacity, C is overall capacity 
    # v is value
    V = [[]for x in range(k) for y in range(w)]
    for w in range(0,c):
        V[0,w]= 0
    for k in range(0,n):
        V[k,0] = 0
    for k in range(1,n): # loop over all rows 
        for w in range(1,c): # loop over all columns
            if (w-w[k] < 0): # not room for item k
                V[k,w] = v[k-1,w]
            else:
                val_with_kth = v[k] + V[k-1, w-w[k]] #case 1
                val_for_k_1 = V[k-1][w] #case 2
                V[k,w]= max(val_with_kth, val_for_k_1)
    return V[n,c]


def dynamic_coin_change(denom,A,C, used):
    #used is for backtracking
    n = denom[-1]
    for x in range(0,A):
        C[n][x]=x
        used[n][x]= True
    #down loop
    for x in range(n-1, 1, -1):
        for y in range(0,A):
            if denom[y]> y or C[x+1][y]< 1+ C[x][y-denom[x]]:
                C[x][y] = C[x+1][y]
                used[x][y]=False
            else:
                C[x][y] = C[x][y-denom[x]]
                used[x][y]= True 


        
    










