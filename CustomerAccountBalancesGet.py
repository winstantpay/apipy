import zeep
import config

#
# The nain 
#
def main():
    wsdl            = './WSDL/WinstantPayWebService.xml'
    client          = zeep.Client(wsdl=wsdl)

    res = client.service.UserSettingsGetSingle(request = {
        'ServiceCallerIdentity':{
            'LoginId': config.userLogin,
            'Password': config.gituserPassword,
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
        'CustomerId': customer_id
    })
    print res

#
# Invoke Main from here to solve accidential import 
#
if __name__ == "__main__":
    main()