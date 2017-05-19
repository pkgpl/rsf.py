import numpy as np
import context
import rsf

# write
fname='test.rsf'
n1=10
n2=3
d1=0.02
d2=0.1
data_format='native_float'

ax1=rsf.Axis(n=n1,o=0.,d=d1,label='Axis 1',unit='s')
ax2=rsf.Axis(n=n2,d=d2)

so=rsf.output(fname,ax1=ax1,ax2=ax2,data_format=data_format)
for itr in range(n2):
    so.write(np.ones(n1))
so.close()

# read
with rsf.input(fname) as sf:
    print('in="%s"'%sf['in'])
    print('data_format="%s"'%sf.data_format)
    print('esize=%d'%sf.esize)
    n1=sf.get('n1')
    d1=sf['d1']
    n2,d2,data=sf.gets(['n2','d2','data'])
    print(sf.dimension)
    print(sf.shape)
    print(sf.size())
    print(sf.dtype)

print('n1=%d n2=%d d1=%f d2=%f'%(n1,n2,d1,d2))
print(data)

with rsf.input(fname) as sf:
    ax1=sf['ax1']
    print('label1="%s" unit1="%s"'%(ax1.label,ax1.unit))
    for trc in sf.traces():
        print(trc)
