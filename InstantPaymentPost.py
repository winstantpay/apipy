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
    payment_id = res.PaymentInformation.PaymentId
    print("Payment id is %s\n" % payment_id)

    res = client.service.InstantPaymentPost(request = {
        'ServiceCallerIdentity':{
            'LoginId': config.userLogin,
            'Password': config.userPassword,
            'ServiceCallerId': config.callerId
        },
        'InstantPaymentId': payment_id

    })

    print res
#
# Invoke Main from here to solve accidential import 
#
if __name__ == "__main__":
    main()