import os
import base64

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

