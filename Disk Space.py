for i in range(0,100):
    f = open('myfile' + str(i) + '.txt', 'w+')
    for i in range(0,100):
        f.write('Woops! I have deleted the content! \n')
    f.close()
