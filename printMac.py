#!/usr/bin/env python
import pika
import sys
import base64
import zlib
import gzip

import StringIO
import json

array =[u'7823AE8B8C8D', u'7823AEA32C4D', u'CC75E2D5109D', u'7823AEA32761', u'109397FB8AC9', u'109397FB8A69', u'7823AE992EC1', u'7823AE9B5361', u'CC75E2D51089', u'109397FB8AD5', u'909D7D9457AD', u'CC75E2D5108D', u'909D7D94578D', u'909D7D94579D', u'5095515077CD', u'5095515077F1', u'7823AE992C69', u'109397FB8A25', u'909D7D9457D1', u'7823AE9B5325', u'5095515077ED', u'109397FB8AAD', u'D43FCBF70639', u'109397FB8AA1', u'7823AE8DA699', u'109397FB8A75', u'109397FB8A9D', u'7823AE9B4DE9', u'20F19E54006D', u'7823AEA32D81', u'7823AE992EC9', u'909D7D9457C9', u'7823AEA32C9D', u'20F19E540079', u'909D7D64F161', u'20F19E5400A5', u'7823AE9B53A5', u'7823AE9B50D5', u'109397FB8AD1', u'7823AE9B53DD', u'109397FB8ACD', u'109397FB8AB9', u'5095515077E9', u'20F19E54004D', u'CC75E2D51091', u'2C7E8156923F', u'BCCAB5FF6717', u'7823AE992C91', u'7823AE93C5A5', u'7823AE98E031', u'7823AEA32BE9', u'7823AEA32CC5', u'7823AE961281', u'7823AE8FED05', u'909D7D7F245D', u'20F19E53FEC1', u'CC75E2D51099', u'7823AE992D1D', u'7823AE98E035', u'20F19E53FEB5', u'7823AEA69459', u'7823AE992BE9', u'7823AE992C79', u'909D7D697535', u'909D7D8497A5', u'7823AE93C635', u'7823AE98E021', u'20F19E53FEA5', u'20F19E53FEB9', u'7823AE91BF21', u'7823AE992BDD', u'7823AE992BD1', u'7823AE992CA5', u'7823AE9B5395', u'5095515077BD', u'7823AE9B539D', u'7823AEA32D0D', u'7823AEA32D79', u'7823AE992DA1', u'7823AE992CC1', u'7823AE992BFD', u'7823AE992D69', u'7823AE992DBD']
print(array[2])
index=1
for mac in range(len(array)):
	print(array[mac])
        
cmts = "colon-Ts-1"
cmts = cmts + '.txt'
with open(cmts,'w') as f:
     for item in array:
      f.write("%s\n" % item)

