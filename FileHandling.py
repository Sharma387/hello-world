#File Handlings
import csv

'''
import tensorflow as tf

hello = tf.constant('Hello Tensorflow')
sess =  tf.session()
print(sess.run(hello))


'''
fileName = 'NewFileCreation.txt'

file = open(fileName, mode = 'w')
file.write('this is my first line \n')
file.write('this is my Second line \n')
file.write('this is my third line \n')
file.write('this is my Fourth line \n')
file.close()

#now ope the same file and print

with open(fileName,mode ='r') as Diffcsvfile:
    allRowList = csv.reader(Diffcsvfile)

    for currentRow in allRowList:
        print(currentRow)