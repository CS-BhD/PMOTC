

def write_result(file, protien, result):
    f = open(file, 'w')
    for i in range(0, len(protien)):
        f.write('%s' % protien[i])
        f.write(',%s' % result[i])
        f.write('\n')
    f.close()

