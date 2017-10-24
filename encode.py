import os
import base64


def convert42():
    with open("sample.xml", "rb") as imageFile:
        str = base64.b64encode(imageFile.read())
        str = bytearray(str,"utf-8")
        outputFile = open('sample.bin', 'wb+')
        outputFile.write(str)
        outputFile.close()



def convertToBase64(filename):
    f = open(filename, 'rb')
    data = f.read()
    f.close()

    string = base64.b64encode(data)
    name_components = filename.split('.')
    newName = '_'.join(name_components)
    outputFilePath = newName + '.txt'
    outputFile = open(outputFilePath, 'wb+')
    outputFile.write(bytearray(string))
    outputFile.close()



if __name__ == "__main__":
    for filename in os.listdir(os.getcwd()):
        convertToBase64(filename)

