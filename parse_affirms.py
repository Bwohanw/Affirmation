f = open('affirmations.csv', 'r')
f.readline()
lst = f.readlines()
f.close()
f = open('output.txt', 'w')
affirm_type = ''
for line in lst:
    tmp = line.split(',')
    typ = tmp[-1]
    if (typ != affirm_type):
        affirm_type = typ
        f.write('\n')
    out = ','.join(tmp[:-1])
    if (out[-1] == '.'):
        out = out[:-1]
    if (out[-2] == '.'):
        out = out[:-2]
    f.write("\"" + out + '\",')
    f.write('\n')
f.close()