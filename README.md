# winstantpay-apipy


![The WinstantPay Logo](http://www.winstantpay.com/assets/img/logo-winstantpay-L-notag-trans.png "The WinstantPay Logo")

These are the Python examples for using the WinstantPay webservice API


## Introduction

WinstantPay allows anyone to trade or pay globally with any currency, including cryptos and other tokens anytime and from anywhere. Originating from a foreign currency exchange and trade finance background the WinstantPay core is utilized by WinstantPay to provide a solid means for ecosystem partners to develop mobile and electronic wallets on this platform. 

### Install: ###
Clone this repository then get started right away
### Requirements: ###


### Quick start
We do usually use the [zeep](http://docs.python-zeep.org/) libray to provide a SOAP client.

```bash
pip install zeep
```
>Please note that you need a pre-shared key to use the API. 
>We call this key a caller-id.
>
>To get the caller id, you need to complete your KYC (Know Your Client), which will result in >you have a user ID and password with WinstantPay. 
>To complete the basic KYC, you need a working email and telephone number and head over to [WORLD-KYC](https://winstantpay.worldkyc.com/)

>Once done, send us an email to <api@winstantpay.com> from the registered email and we ?will get in touch prompty (usually via SMS to your phone 24hours).
>
>Upon verification of that number we will provide your with the caller ID

After you have all you credentials please follow the following steps (explained in section **Examples** below

## Basic Flow of the API

### Security

Our API foresees that every request has to be authorised and the ServiceCallerIdentity object has to be provided as part of the args object iin very API method call.

```python
request = {
    'ServiceCallerIdentity':{
        'LoginId': config.userLogin,
        'Password': config.userPassword,
        'ServiceCallerId': config.callerId
    }
}
```
### Flow

WinstantPay follows in the core the dual controll principle where one user prepares a transaction and a second user (usually a supervisor) approves or books the transaction.
e.g.  
1. InstantPaymentCreate -- returns a PaymentId 
2. InstantPaymentPost -- books the payment

or.

1. UserSettingsGetSingle -- returns the UserId
2. FXDealQouteCreate -- Uses UserId as CustomerId and returns a QuoteId
3. FXDealQuoteBookAndInstantDeposit -- Uses QuoteId and Books the Deal and Depositis it in the users wallet


## Example

We are sure you'll find your way around the source and keep the explanations here rather brief and explain one example in full.

Let's look into an example to get your account balances:

```python
    print res
```

In the GetAccountBalances case we call on two webservices
1. UserSettingsGetSingle  -- to retrieve the UserId and;
2. CustomerAccountBalancesGet - to get the customers account balances

> the customer in this case is the same as the user.

#### Explore the Webservice
From the command line, you can run:
```bash
python -mzeep WSDL/WinstantPayWebService.xml
```
to explore the webservice.

#### API Call and Parameters 
All the service endpouints are listed in the segment: 
```bash
Service: GPWebService: Operations. 
```
Simply call the method is then called with parameters to consume the endpoint like so:

```python
res = client.service.UserSettingsGetSingle(request = {
    'ServiceCallerIdentity':{
        'LoginId': userLogin,
        'Password': userPassword,
        'ServiceCallerId': callerId
    }
})
```
The request JSON object define the input paramters of the webservice. 

#### Response processing

upon return the result is directly returned.

the section **Endpoints** provide an overview over the  inputs (the request JSON object and the response object.

>Now that you understand how the general flow works, we hope that  and when in doubt you can browse the WSDL file by using one of the many SOAP toolsets.. 
>We recommend the free community version of [SoapUi](https://www.soapui.org/)  to browse and test our soap API's or use the zeep explorer introduced above.


## Endpoints

- [CurrencyListGetPaymentCurrencies](#currencylistgetpaymentcurrencies)
- [CustomerAccountBalancesGet](#customeraccountbalancesget)
- [CustomerAccountStatementGetSingle](#customeraccountstatementgetsingle)
- [FXDealQuoteBookAndInstantDeposit](#fxdealquotebookandinstantdeposit)
- [FXDealQuoteCreate](#fxdealquotecreate)
- [GetCustomerAccountBalances](#getcustomeraccountbalances)
- [GetLibraryVersion](#getlibraryversion)
- [InstantPaymentCreate](#instantpaymentcreate)
- [InstantPaymentGetSingle](#instantpaymentgetsingle)
- [InstantPaymentPost](#instantpaymentpost)
- [UserSettingsGetSingle](#usersettingsgetsingle)

### CurrencyListGetPaymentCurrencies
#### Code
```python
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
```
#### Response
The Object:
```python
{
    'ServiceResponse': {
        'HasErrors': False,
        'HasWarnings': False,
        'Responses': {
            'ServiceResponseData': [
                {
                    'ResponseCode': 0L,
                    'ResponseType': 'Information',
                    'Message': 'Success',
                    'MessageDetails': 'Command completed successfully',
                    'FieldName': None,
                    'FieldValue': None
                }
            ]
        }
    },
    'Currencies': {
        'CurrencyData': [
            {
                'CurrencyId': 76L,
                'CurrencyCode': 'KHR',
                'CurrencyName': 'Cambodian Riels',
                'CurrencyAmountScale': 2L,
                'CurrencyRateScale': 5L,
                'Symbol': u'\u17db',
                'PaymentCutoffTime': '16:00',
                'SettlementDaysToAdd': 0L
            },
            {
                'CurrencyId': 83L,
                'CurrencyCode': 'LAK',
                'CurrencyName': 'Lao Kips',
                'CurrencyAmountScale': 2L,
                'CurrencyRateScale': 5L,
                'Symbol': u'\u20ad',
                'PaymentCutoffTime': '16:00',
                'SettlementDaysToAdd': 0L
            },
            {
                'CurrencyId': 95L,
                'CurrencyCode': 'MMK',
                'CurrencyName': 'Myanmar (Burma) Kyats',
                'CurrencyAmountScale': 2L,
                'CurrencyRateScale': 4L,
                'Symbol': 'MMK',
                'PaymentCutoffTime': '16:00',
                'SettlementDaysToAdd': 0L
            },
            {
                'CurrencyId': 141L,
                'CurrencyCode': 'THB',
                'CurrencyName': 'Thai Baht',
                'CurrencyAmountScale': 2L,
                'CurrencyRateScale': 3L,
                'Symbol': u'\u0e3f',
                'PaymentCutoffTime': '16:00',
                'SettlementDaysToAdd': 0L
            },
            {
                'CurrencyId': 153L,
                'CurrencyCode': 'USD',
                'CurrencyName': 'US Dollars',
                'CurrencyAmountScale': 2L,
                'CurrencyRateScale': 4L,
                'Symbol': '$',
                'PaymentCutoffTime': '23:00',
                'SettlementDaysToAdd': 2L
            }
        ]
    }
}
```
### CustomerAccountBalancesGet
#### Code
```python
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
        'CustomerId': customer_id
    })
    print res

#
# Invoke Main from here to solve accidential import 
#
if __name__ == "__main__":
    main()
```
#### Response
The Object:
```python
{ CustomerBalanceData: 
   [ { AccountId: 'the ID of the account ',
       AccountNumber: '1022369',
       CCY: 'KHR',
       Balance: 0,
       ActiveHoldsTotal: 0,
       BalanceAvailable: 0,
       BaseCCY: 'THB',
       BalanceAvailableBase: 0 },
     { AccountId: 'the ID of the account ',
       AccountNumber: '1022372',
       CCY: 'LAK',
       Balance: 260646,
       ActiveHoldsTotal: 0,
       BalanceAvailable: 260646,
       BaseCCY: 'THB',
       BalanceAvailableBase: 979.19 },
     { AccountId: 'the ID of the account ',
       AccountNumber: '1022376',
       CCY: 'MMK',
       Balance: 42059,
       ActiveHoldsTotal: 0,
       BalanceAvailable: 42059,
       BaseCCY: 'THB',
       BalanceAvailableBase: 979.07 },
     { AccountId: 'the ID of the account ',
       AccountNumber: '1022381',
       CCY: 'THB',
       Balance: 495700,
       ActiveHoldsTotal: 0,
       BalanceAvailable: 495700,
       BaseCCY: 'THB',
       BalanceAvailableBase: 495700 },
     { AccountId: 'the ID of the account ',
       AccountNumber: '1022991',
       CCY: 'TND',
       Balance: 0,
       ActiveHoldsTotal: 0,
       BalanceAvailable: 0,
       BaseCCY: 'THB',
       BalanceAvailableBase: 0 },
     { AccountId: 'the ID of the account ',
       AccountNumber: '1022385',
       CCY: 'USD',
       Balance: 4950,
       ActiveHoldsTotal: 0,
       BalanceAvailable: 4950,
       BaseCCY: 'THB',
       BalanceAvailableBase: 154291.5 } ] }
```
### CustomerAccountStatementGetSingle
#### Code
```python
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
```
#### Response
The Object:
```python
 [   { EntryTypeName: 'Payment',
       ItemTypeId: 10,
       ItemTypeNa# From you KYCme: 'Deposit',
       ItemId: 'an ID',
       ItemReference: 'DEPO1001055',
       AmountCredit: 500000,
       AmountDebit: 0,
       ValueDate: '2018-03-15T00:00:00.000Z',
       BankMemo: 'TEST Examples' },
     { EntryTypeName: 'Settlement',
       ItemTypeId: 10,
       ItemTypeName: 'Deposit',
       ItemId: 'an ID',
       ItemReference: 'DEPO1001084 / SPOT1009654',
       AmountCredit: 0,
       AmountDebit: 1000,
       ValueDate: '2018-03-26T00:00:00.000Z',
       BankMemo: 'ACCOUNT INSTANT TRANSFER' } 
]
```
### FXDealQuoteBookAndInstantDeposit
>The remaining web-service calls are described here only. Please refer to the python code file with the matching name.
FXDealQuoteBookAndInstantDeposit.py

### FXDealQuoteCreate
Creates a FX Deal Quote, which later can be poosted to execute

### GetCustomerAccountBalances
This is identical to the [CustomerAccountBalancesGet](#customeraccountbalancesget) endpoint and is listed for historical reasons only.

### GetLibraryVersion
returns the version of the web-service. Please quote this version in any support request you may have.
The version of the time wriring this readme is: 4.5.7.15
>Just use this example to see if your SOAP client is working allright, before you request further support.

### InstantPaymentCreate

### InstantPaymentGetSingle
>Even though the InstantPaymentCreate returns a paymentId, this InstantPaymentGetSingle service depends on a payment that is completed already.
> So this service is called after the InstantPaymentPost function as shown in the example.
### InstantPaymentPost
This endpoint actually transacts the payment in the system and is usually called after the payment has been created with InstantPaymentCreate
>Call the InstantPaymentGetSingle service to get all the details of  the successful payment

### UserSettingsGetSingle
Here you get all the user details, such as account numbers for the user,
> The import field to use from the response is the UserId field has this is used in suquent calls of the webservice


## To get a wallet 
### KYC first
Head right to the [Demo](https://demo.winstantpay.com/) platform and complete your KYC first.
To complete your KYC you only need a working email address you can access. 
After successful subscription to KYC your user credentials will be added to the system and you can login to the wallet. 
After that, please send us an email so we can creaate a caller-id for you and your all set to go and use this API.


## Wallet Demo

https://demoewallet.winstantpay.com/

## Support

Support for the WinstantPay API is available through the WinstantPay API team. We will share the details about how to interact with our teams at the end of the KYC process.  Should you have pUiany issues before that you can send a twitter message to us to <api@winstantpay.com>

## License

WinstantPay API example scripts are released under the MIT license.










