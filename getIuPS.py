"""
A script to extract IuPS addresses from an RNC CMExport file
Works with Huawei RNC CMExport

By Tubagus Rizal 
2017
"""


import xml.etree.ElementTree as ET
import glob
import pdb


def getRncInfo(xmlroot):
    # get RNC info
    rnc = {}
    for rncInfo in xmlroot.findall(".//*[@className='BSC6900UMTSNE']/attr"):
        if rncInfo.attrib["name"] == "fdn":
            rnc["fdn"] = rncInfo.text
        
        if rncInfo.attrib["name"] == "name":  
            rnc["name"] = rncInfo.text
            
        if rncInfo.attrib["name"] == "neID": 
            rnc["neid"] = rncInfo.text 
    return rnc      


def getIuPSIpAddress(xmlroot):
    # get a list of IuPS interface
    iupsIpAddr = []
    for ipPath in xmlroot.findall(".//*[@className='BSC6900UMTSIPPATH']/attr"):
        if ipPath.attrib["name"] == "IPADDR":
            ipAddress = ipPath.text
            
        if ipPath.attrib["name"] == "ITFT" and ipPath.text == "IUPS":
            if not ipAddress in iupsIpAddr:
                iupsIpAddr.append(ipAddress)
    return iupsIpAddr             


def main():
    xmlFolder = "D:\\1000-MyDocuments\\100-Projects\\098-ProximusCFT\\TAADisttributor\\3G-OSS"
    xmlFiles = [file for file in glob.glob(xmlFolder + "/**/*.xml", recursive=True)]
    for xmlFile in xmlFiles:
        tree = ET.parse(xmlFile)
        root = tree.getroot()
    
        #print result
        rnc = getRncInfo(root)
        for key, value in rnc.items():
            print (key, value, ",", end=" ")
        
        iupsIpAddr = getIuPSIpAddress(root)
        for item in iupsIpAddr:
            print ( "IuPS: ", item,  end=" ")  
            
        print("\n")    
        

if __name__ == "__main__":
    main()














      