import array
import numpy as np
import matplotlib.pyplot as plt


binfpath="/fs/lustre/cita/hqchen/data/z-ifrit-a=0.1401.bin"
with open(binfpath,'rb') as f:
    binarydata=f.read()
lllen=8; flen=4; ilen=4 

firstfield=lllen*2+3*ilen

nextfield=firstfield

N=1024

xHI=array.array('f',binarydata[nextfield+lllen:nextfield+lllen+N**3*flen])
xHI=np.reshape(xHI,(N,N,N),order='F')

nextfield+=lllen+N**3*flen
god=array.array('f',binarydata[nextfield+lllen:nextfield+lllen+N**3*flen])
god=np.reshape(god,(N,N,N),order='F')

nextfield+=lllen+N**3*flen
T=array.array('f',binarydata[nextfield+lllen:nextfield+lllen+N**3*flen])
T=np.reshape(T,(N,N,N),order='F')
