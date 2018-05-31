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

    res = client.service.InstantPaymentGetSingle(request = {
        'ServiceCallerIdentity':{
            'LoginId': config.userLogin,
            'Password': config.userPassword,
            'ServiceCallerId': config.callerId
        },
        'InstantPaymentId': payment_id
        # Please note that we are using the same payment id, we just payed. IRL 
        # you would most likely use these endpoint to look into payments that happened a bit 
        # longer ago
    })

    print res
#
# Invoke Main from here to solve accidential import 
#
if __name__ == "__main__":
    main()