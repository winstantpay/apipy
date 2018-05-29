import zeep
import config

#
# The nain 
#
def main():
    wsdl            = './WSDL/WinstantPayWebService.xml'
    client          = zeep.Client(wsdl=wsdl)

    res = client.service.CustomerAccountStatementGetSingle(request = {
        'ServiceCallerIdentity':{
            'LoginId': config.userLogin,
            'Password': config.userPassword,
            'ServiceCallerId': config.callerId
        },
        # If you do not know your customerID, you can find them in the response to CustomerAccountBalancesGet
        'AccountId': config.accountId,
        'StartDate': "2018-01-01", # Date format is YYYY-MM-DD
        'EndDate': "2018-12-01" # Date format is YYYY-MM-DD        
    })
    print res

#
# Invoke Main from here to solve accidential import 
#
if __name__ == "__main__":
    main()