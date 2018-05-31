import zeep
import config

#
# The nain 
#
def main():
    wsdl            = './WSDL/WinstantPayWebService.xml'
    client          = zeep.Client(wsdl=wsdl)

    # 
    # First we get the customer Id
    #
    res = client.service.GetLibraryVersion()
    print res



#
# Invoke Main from here to solve accidential import 
#
if __name__ == "__main__":
    main()