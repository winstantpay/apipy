import zeep
import config

#
# The nain 
#
def main():
    wsdl            = './WSDL/WinstantPayWebService.xml'
    client          = zeep.Client(wsdl=wsdl)

    res = client.service.InstantPaymentCreate(request = {
        'ServiceCallerIdentity':{
            'LoginId': config.userLogin,
            'Password': config.userPassword,
            'ServiceCallerId': config.callerId
        },
        'FromCustomer': 'RALF',
        'ToCustomer': 'Argie1970',
        'Amount': 10.000,
        'CurrencyCode': 'THB',
        'ValueDate': '',
        'ReasonForPayment':'',
        'ExternalReference': '',
        'Memo':''

    })

    print res


#
# Invoke Main from here to solve accidential import 
#
if __name__ == "__main__":
    main()