import cv2
import numpy as np
import matplotlib.pyplot as plt

Nprueb= '311B'

denb = 'deb'

# In[6]:


ruta2 = './restoration/P'+ Nprueb +'/BestPnsrDEB_P'+ Nprueb +'_'
namesIMGE = np.array(['image_House256_greylevel.png', 'image_Lena512_greylevel.png', 'image_Peppers512_greylevel.png' , 'F16_GT_greylevel.png','image_Baboon512_greylevel.png'])
ls = []
lsgraf = []
resData = []

for k in range(1,25):#for k in listaRep:#25
    #nameimg = 'kodim18.png'#'image_Lena512rgb.png' #
    nameimg = 'kodim' + str(k) + '_small.png'
    
#for k in range(len(namesIMGE)):
#    nameimg =  namesIMGE[k]
    maxPnsr = []
    listY = []

    ruta  = './txt'+ Nprueb +'/'
    name = nameimg.replace('.png','.csv')

    fname = ruta + 'P' + Nprueb + denb +'MAXval' + name
    #'/txt/1denMAXvalimage_Lena512rgb.csv'

    data = np.genfromtxt(fname, delimiter=',')
    maxPnsr.append(data)

    #print(data)

    pns = np.array(maxPnsr)

    valMX,q = (np.max(pns.T[1]), np.argmax(pns.T[1]))#(np.nanmax(pns.T[1]), np.nanargmax(pns.T[1]))
    #print(valMX,q)
    
    lamA = pns.T[0][q]

    lam = lamA[0]

    fila = pns.T[:,q]

    dif = np.max(pns.T[1]) - pns.T[1,0]
    
    fila = np.append(fila,dif)
    
    resData.append(fila)
    name = nameimg.replace('.png','.csv')
    fname = ruta + 'P'+ Nprueb  + denb +'PNSR' + name 
    plotY = np.genfromtxt(fname, delimiter=',')
    print('here2')
    Y = np.array(plotY).T