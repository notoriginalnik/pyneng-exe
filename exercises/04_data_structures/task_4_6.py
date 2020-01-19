# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ospf_route = "O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

#1 try
ospf1=ospf_route.split()

print('''
Protocol:           OSPF
Prefix:             {}
AD/Metric:          {}
Next-Hop:           {}
Last update:        {}
Outbound Interface: {}
'''
.format(ospf1[1], ospf1[2].strip('[]'), ospf1[4].strip(','), ospf1[5].strip(','), ospf1[6]))

# #for me

# template1 = '''
# Protocol:           OSPF
# Prefix:             {}
# AD/Metric:          {}
# Next-Hop:           {}
# Last update:        {}
# Outbound Interface: {}
# '''

# print(template1.format(ospf1[1], ospf1[2].strip('[]'), ospf1[4].strip(','), ospf1[5].strip(','), ospf1[6]))

# #2 try
# slovo={
#     'Protocol':ospf1[0],
#     'Prefix':ospf1[1],
#     'AD/Metric':ospf1[2],
#     'Next-Hop':ospf1[4].strip(','),
#     'Last update':ospf1[5].strip(','),
#     'Outbound Interface':ospf1[6]
# }

# print(slovo)

# print("Protocol:{:15} Prefix:{:15} AD/Metric:{:15} Next-Hop:{:15} Last update:{:15} Outbound Interface:{:15}"
# .format(ospf1[0],ospf1[1],ospf1[2],ospf1[4],ospf1[5],ospf1[6]))

# #3 try
# ospf0=('Protocol:','Prefix:','AD/Metric:','Next-Hop:','Last update:','Outbound Interface:')
# if ospf1[0] == 'O':
#     ospf1[0]='OSPF'
# ospf1[2]=ospf1[2].strip('[]')
# ospf1[2]=ospf1[2].strip('[]')
# ospf1[4]=ospf1[4].strip(',')
# ospf1[5]=ospf1[5].strip(',')

# print(ospf1)

# print("{:23} {:23}".format(ospf0[0],ospf1[0]),"{:23} {:23}".format(ospf0[0],ospf1[0]))
# print("{:23} {:23}".format(ospf0[1],ospf1[1]))
# print("{:23} {:23}".format(ospf0[2],ospf1[2]))
# print("{:23} {:23}".format(ospf0[3],ospf1[4]))
# print("{:23} {:23}".format(ospf0[4],ospf1[5]))
# print("{:23} {:23}".format(ospf0[5],ospf1[6]))