import zeep

userLogin       = "Ralf4IOU"
userPassword    = "Letmein123"
callerId        = "773B3EBA-D4FC-4853-A32F-06FD23A5C902"
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