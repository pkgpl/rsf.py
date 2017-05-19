from unittest import TestCase, main
import os
import numpy as np
import context
import rsf

class TraceTestCase(TestCase):
    def setUp(self):
        self.fname="test.rsf"
        self.n=100
        self.d=0.001
        self.data_format='native_float'
        self.at=rsf.Axis(n=self.n,d=self.d,label='Time',unit='s')
        self.a2=rsf.Axis(n=2)
        with rsf.output(self.fname,ax1=self.at,ax2=self.a2,data_format=self.data_format) as f:
            f.write(np.ones(self.n,dtype=np.float64))
            f.write(2.*np.ones(self.n,dtype=np.float64))

    def test_header(self):
        f=rsf.input(self.fname)
        self.assertEqual(os.path.abspath(self.fname+'@'),f.get('in'))
        self.assertEqual(os.path.abspath(self.fname+'@'),f['in'])
        self.assertEqual(self.data_format,f.get('data_format'))
        self.assertEqual(self.data_format,f['data_format'])
        self.assertEqual(self.data_format.split('_')[0],f.get('form'))
        self.assertEqual(self.data_format.split('_')[0],f['form'])
        self.assertEqual(self.data_format.split('_')[1],f.get('type'))
        self.assertEqual(self.data_format.split('_')[1],f['type'])
        self.assertEqual(np.float32,f.dtype)
        self.assertEqual('float',f.type)
        self.assertEqual('native',f.form)

        self.assertEqual(self.n,f.get('n1'))
        self.assertEqual(self.n,f['n1'])
        self.assertEqual(self.d,f.get('d1'))
        self.assertEqual(self.d,f['d1'])
        self.assertEqual(self.at.label,f.get('label1'))
        self.assertEqual(self.at.label,f['label1'])
        self.assertEqual(self.at.unit,f.get('unit1'))
        self.assertEqual(self.at.unit,f['unit1'])
        self.assertEqual(2,f.get('n2'))
        self.assertEqual(2,f['n2'])
        self.assertEqual(0.0,f.get('d2'))
        self.assertEqual(0.0,f['d2'])
        self.assertEqual(2,f.dimension)
        self.assertEqual((2,self.n),f.shape)
        self.assertEqual((2,self.n),f['data'].shape)
        self.assertEqual(0,f.get('n3'))
        self.assertEqual(0,f['n3'])
        self.assertEqual(0,f['n5'])
        f.close()

    def test_read(self):
        with rsf.input(self.fname) as f:
            for itrc,trc in enumerate(f.traces()):
                print("//",itrc)
                if itrc==0:
                    self.assertEqual(1.0,trc[0])
                elif itrc==1:
                    self.assertEqual(2.0,trc[0])

    def tearDown(self):
        os.remove(self.fname)
        os.remove(self.fname+'@')

if __name__ == '__main__':
    main()
