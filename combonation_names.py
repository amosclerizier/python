cloud = ['aws', 'gcp', 'azr', 'oci']
region = ['use1', 'use2', 'usw1', 'usw2']
enviro = ['p', 'n']
operatingsys = ['w', 'l', 'a']
servertype = ['a', 'd', 'w']



for i in cloud:
       for s in enviro:
           for o in operatingsys:
               for b in servertype:
                   print(i + s + o + b)
