#Michael Malus
#4-27-17

#basic frequency distribution calculator and index of coincidence calculator for alphabets

def freqDist(alpha):
    '''
    simple freq distribution calculator, gets letter counts
    only for lowercase letters, no spaces, periods, etc
    only keeps nonzero letters in final dictionary
    '''
    import string
    alphabet = dict.fromkeys(string.ascii_lowercase, 0)
    alpha = alpha.lower()
    for x in range(len(alpha)):
        if alpha[x] in alphabet:
            alphabet[alpha[x]] += 1
    alphabet = {i:j for i,j in alphabet.items() if j > 0}
    return alphabet
    
def indexCoin(alphabet):
    '''
    the index of coincidence is defined as:
    IC = sum(f_i*(f_i - 1))/(N(N-1))
    where f_i is the count of a given letter, and N is the total number of letters
    '''
    N = sum([alphabet[x] for x in alphabet])
    num = sum([alphabet[x]*(alphabet[x]-1) for x in alphabet])
    ic = num / (N*(N-1))
    return ic
    
if __name__ == "__main__":
    #example strings attached from some crypto problem set I found
    alist = 'UW ZTWITJDD N UVRTP ONEE OJNTRHI HJJPD UW OJ TJEJNDJP'
    blist = 'ZWT EAUKJ OUY JPHDNCJ FENSAYT O UOSAKOZANUOC ETVTETUGT FNAUZ'
    clist = 'GF QFIDOAX GWU AUPULBU FD GWU GWOAV TLPP TULAOIN GRAI RCBOVU VFJI AFGLGU LIV POBGUI QLAUDRPPH'
    print(freqDist(clist))
    print(indexCoin(freqDist(clist)))