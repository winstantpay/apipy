import zeep

userLogin       = "" # From you KYC
userPassword    = "" # From you KYC
callerId        = "" # caller ID from KYC completion provided by us
wsdl            = './WSDL/WinstantPayWebService.xml'

client = zeep.Client(wsdl=wsdl)

res = client.service.UserSettingsGetSingle(request = {
    'ServiceCallerIdentity':{
        'LoginId': userLogin,
        'Password': userPassword,
        'ServiceCallerId': callerId
    }
})

customer_id = res.UserSettings.UserId

res = client.service.CustomerAccountBalancesGet(request = {
    'ServiceCallerIdentity':{
        'LoginId': userLogin,
        'Password': userPassword,
        'ServiceCallerId': callerId
    },
    'CustomerId': customer_id
})

print res