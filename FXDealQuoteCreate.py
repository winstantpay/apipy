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
    res = client.service.UserSettingsGetSingle(request = {
        'ServiceCallerIdentity':{
            'LoginId': config.userLogin,
            'Password': config.userPassword,
            'ServiceCallerId': config.callerId
        }
    })

    customer_id = res.UserSettings.UserId

    res = client.service.FXDealQuoteCreate(request = {
        'ServiceCallerIdentity':{
            'LoginId': config.userLogin,
            'Password': config.userPassword,
            'ServiceCallerId': config.callerId
        },
        # If you do not know your customerID, you can find them in the response to UserSettingsGetSingle
        'CustomerId': customer_id,
        'BuyCCY': 'MMK',
        'SellCCY': 'THB',
        'Amount': '1000.00',
        'AmountCCY': 'THB',
        'DealType': 'Spot',
        'IsForCurrencyCalculator': False
    })

    print res



#
# Invoke Main from here to solve accidential import 
#
if __name__ == "__main__":
    main()