import numpy as np

Nprueb= '311B'

denb = 'deb'

for k in range(1,25):#for k in listaRep:#25
    #nameimg = 'kodim18.png'#'image_Lena512rgb.png' #
    nameimg = 'kodim' + str(k) + '_small.png'
    
    ruta  = './txt'+ Nprueb +'org/'
    name1 = nameimg.replace('.png','.csv')
    fname1 = ruta + 'P'+ Nprueb  + denb +'PNSR' + name1 
    name2 = nameimg.replace('.png','2.csv')
    fname2 = ruta + 'P'+ Nprueb  + denb +'PNSR' + name2 
    filenames = [fname1,fname2]
    
    plotY1 = np.genfromtxt(fname1, delimiter=',')
    plotY2 = np.genfromtxt(fname2, delimiter=',')
    plotY3 = np.concatenate((plotY1, plotY2), axis = 1)
    #print(plotY1.shape)
    #print(plotY2.shape)
    #print(plotY3.shape)

    #Guardar datos de gráfica
    Y = np.array(plotY3)
    #ruta = './txt290/'
    ruta = './txt'+ Nprueb +'/'
    name = nameimg.replace('.png','.csv')
    #fname = ruta + 'P290denPNSR' + name
    fname = ruta + 'P'+ Nprueb + denb +'PNSR' + name
    np.savetxt(fname, Y, delimiter =",",fmt ='% s')    
    
