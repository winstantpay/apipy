import zeep
import config

#
# The nain 
#
def main():
    wsdl            = './WSDL/WinstantPayWebService.xml'
    client          = zeep.Client(wsdl=wsdl)

    res = client.service.CurrencyListGetPaymentCurrencies(request = {
        'ServiceCallerIdentity':{
            'LoginId': config.userLogin,
            'Password': config.userPassword,
            'ServiceCallerId': config.callerId
        }
    })

    print res

#
# Invoke Main from here to solve accidential import 
#
if __name__ == "__main__":
    main()