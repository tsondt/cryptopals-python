#!/usr/bin/env python

#Challenge 1
import base64
s = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
o = base64.b64encode(s.decode('hex'))
print 's = ', s
print 'o = ', o
assert o == 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

#Challenge 2
s = '1c0111001f010100061a024b53535009181c'
k = '686974207468652062756c6c277320657965'
o = ''.join([chr(ord(x[0])^ord(x[1])) for x in zip(s.decode('hex'),k.decode('hex'))]).encode('hex')
print 's = ', s
print 'k = ', k
print 'o = ', o
assert o == '746865206b696420646f6e277420706c6179'

#Challenge 3
import operator
#expect d1, (en_le_freq) d2 (le_freq)  to have the same keys
def chi_squared(d1, d2, l):
    xx = 0.0
    for i in d1.keys():
        print d1[i]/100*l
        xx += (d2[i]-d1[i]/100*l)**2/(d1[i]/100*l)
    return xx

en_letters = 'abcdefghijklmnopqrstuvwxyz'
en_le_freq = dict(zip(en_letters, [8.167,1.492,2.782,4.253,12.702,2.228,2.015,6.094,6.966,0.153,0.772,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.056,2.758,0.978,2.360,0.150,1.974,0.074]))
etaoin = 'etaoinshrdlcumwfgypbvkjxqz'
s = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
print 's = ', s
score = 0
for i in xrange(128):
    o = ''.join([chr(i^ord(x)) for x in s.decode('hex')])
    le_freq = dict(zip(en_letters, [0]*len(en_letters)))
    for i in o:
        if i.lower() in en_letters:
            le_freq[i.lower()] += 1
    c_s = chi_squared(en_le_freq, le_freq, len(o))
    if score == 0:
        score = c_s
        ro = o
    else:
        if c_s < score:
            score = c_s
            ro = o
print 'o = ', ro
raw_input()
#Challenge 4
score = 0
for s in open('4.txt').readlines():
    s = s.strip('\n')
#    print s
#    score = 0
    for i in xrange(100):
        o = ''.join([chr(ord(chr(i))^ord(x)) for x in s.decode('hex')])
        le_freq = dict(zip(en_letters, [0]*len(en_letters)))
        for i in o:
            if i.lower() in en_letters:
                le_freq[i.lower()] += 1
        c_s = chi_squared(en_le_freq, le_freq, len(o))
        print c_s
        if score == 0:
            score = c_s
            ro = o
        else:
            if c_s < score:
                score = c_s
                ro = o
print 'o = ', ro

