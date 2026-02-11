from itertools import combinations, permutations

ROTOR_I   = [4,10,12,5,11,6,3,16,21,25,13,19,14,22,24,7,23,20,18,15,0,8,1,17,2,9]
ROTOR_II  = [0,9,3,10,18,8,17,20,23,1,11,7,22,19,12,2,16,6,25,13,15,24,5,21,14,4]
ROTOR_III = [1,3,5,7,9,11,2,15,17,19,23,21,25,13,24,4,8,22,6,0,10,12,20,18,16,14]
ROTOR_IV  = [4,18,14,21,15,25,9,0,24,16,20,8,17,7,23,11,13,5,19,6,10,3,2,12,22,1]
ROTOR_V   = [21,25,1,17,6,8,19,24,20,15,18,3,13,7,11,23,0,22,12,9,16,14,5,4,2,10]

ROTORS = [ROTOR_I, ROTOR_II, ROTOR_III, ROTOR_IV, ROTOR_V]

def info(position, rotor, fil):
    return (rotor[(fil + position) % 26] - position) % 26

print(info(15, ROTOR_I, 0))

def combi(entier):
    return list(combinations(range(5),3))[entier]

def combi_ord(entier, n):
    rotors = combi(n)
    return list(permutations(rotors, 3))[entier]

for entier in range(5):
    print(combi_ord(entier, 5))

def enigma(e1, e2, rot, n):
    r=
    for i in rot:
        if 
