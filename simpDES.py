# Simplified DES algorithm
# From Trappe and Washington, chapter 4.2
# Michael Malus 5-30-17

class simpleDES(object):
    
    """
    The simplified message is 12 bits written in the form L_0 R_0, split down the middle.
    The key, K, is 9 bits.  The ith round of the algorithm transforms an input
    L_i-1 R_i-1 to the output L_i R_i using an 8 bit key K_i derived from K.
    
    This code specifically works for 1 round only.
    """
    
    def __init__(self, message, key, iteration):
        self.message = message
        self.key = key
        self.iteration = iteration
    
    def messageSplit(self):
        return self.message[0:6]
    
    def expander(inp):
        return inp[0]+inp[1]+inp[3]+inp[2]+inp[3]+inp[2]+inp[4]+inp[5]
    
    def keyshift(self):
        return self.key[self.iteration-1:] + self.key[:self.iteration-2]
    
    def sBox(box, inp):
        S1=[['101','010','001','110','011','100','111','000'],['001','100','110','010','000','111','101','011']]
        S2=[['100','000','110','101','111','001','011','010'],['101','011','000','111','110','010','001','100']]
        colsel = int(inp[1:],2)
        if box==1:
            return S1[int(inp[0])][colsel]
        elif box==2:
            return S2[int(inp[0])][colsel]
            
    def xOR(a, b):
        return bin(int(a,2)^int(b,2))[2:]
        
    def retfnc(a, b):
        return a + b
        

#an example round, taking place with iteration 4
        
rd1 = simpleDES('011100100110','010011001',4)

simpleDES.retfnc(simpleDES.sBox(1, str(simpleDES.xOR(simpleDES.expander(rd1.messageSplit()), rd1.keyshift())[0:4])), simpleDES.sBox(2, str(simpleDES.xOR(simpleDES.expander(rd1.messageSplit()), rd1.keyshift())[4:]).zfill(4)))