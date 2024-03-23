
Nprueb= '311B'

denb = 'deb'

for k in range(1,25):#for k in listaRep:#25
    #nameimg = 'kodim18.png'#'image_Lena512rgb.png' #
    nameimg = 'kodim' + str(k) + '_small.png'
    
    ruta  = './txt'+ Nprueb +'org/'
    name1 = nameimg.replace('.png','.csv')
    fname1 = ruta + 'P' + Nprueb + denb +'MAXval' + name1
    name2 = nameimg.replace('.png','2.csv')
    fname2 = ruta + 'P' + Nprueb + denb +'MAXval' + name2
    filenames = [fname1,fname2]

    fname3 = './txt'+ Nprueb +'/' + 'P' + Nprueb + denb +'MAXval' + name1
    with open(fname3, "w") as new_file:
        for name in filenames:
            with open(name) as f:
                for line in f:
                    new_file.write(line)
                
                #new_file.write("\n")