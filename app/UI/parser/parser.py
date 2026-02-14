import xml.etree.ElementTree as ET 

def parseBible(path):
    tree = ET.parse(path)
    root = tree.getroot()

    bibleDict = {}

    for elementos in root.iter():
        tag = elementos.tag

        match tag:
            case 'book':
                livros = elementos.attrib['number']
                bibleDict[livros] = {}

            case 'chapter':
                capitulo = elementos.attrib['number']
                bibleDict[livros][capitulo] = {}
            
            case 'verse':
                verso = elementos.attrib['number']
                verso_texto = elementos.text
                
                bibleDict[livros][capitulo][verso] = verso_texto
    return bibleDict