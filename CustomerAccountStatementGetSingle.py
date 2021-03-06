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

    res = client.service.CustomerAccountBalancesGet(request = {
        'ServiceCallerIdentity':{
            'LoginId': config.userLogin,
            'Password': config.userPassword,
            'ServiceCallerId': config.callerId
        },
        # If you do not know your customerID, you can find them in the response to UserSettingsGetSingle
        'CustomerId': customer_id
    })

    #Let's in this example just take the first account to get a statement
    #This is actually bad programming but for the sake of clarity there are no range checks here
    account_id = res.Balances.CustomerBalanceData[0].AccountId
    print "Acount ID is %s\n" % account_id

    # get the Statement for the first account
    res = client.service.CustomerAccountStatementGetSingle(request = {
        'ServiceCallerIdentity':{
            'LoginId': config.userLogin,
            'Password': config.userPassword,
            'ServiceCallerId': config.callerId
        },
        # If you do not know your customerID, you can find them in the response to UserSettingsGetSingle
        "AccountId": account_id,
        "StartDate": "2018-01-01",
        "EndDate": "2018-12-01"
    })

    print res



#
# Invoke Main from here to solve accidential import 
#
if __name__ == "__main__":
    main()