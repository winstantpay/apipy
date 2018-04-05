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
        'LoginId': userLogin,
        'Password': userPassword,
        'ServiceCallerId': callerId
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
import zeep

userLogin       = "" # get your details through our KYC
userPassword    = "" # get your details through our KYC
callerId        = ""
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
#### Call
```python
#TODO: Add Code
```
Method: 
```python
#TODO: Add Code
```
#### Response
The Path:
```python
#TODO: Add Code
```
The Object:
```python
{ CurrencyData: 
   [ { CurrencyId: 76,
       CurrencyCode: 'KHR',
       CurrencyName: 'Cambodian Riels',
       CurrencyAmountScale: 2,
       CurrencyRateScale: 5,
       Symbol: '៛',
       PaymentCutoffTime: '16:00',
       SettlementDaysToAdd: 0 },
     { CurrencyId: 83,
       CurrencyCode: 'LAK',
       CurrencyName: 'Lao Kips',
       CurrencyAmountScale: 2,
       CurrencyRateScale: 5,
       Symbol: '₭',
       PaymentCutoffTime: '16:00',
       SettlementDaysToAdd: 0 },
     { CurrencyId: 95,
       CurrencyCode: 'MMK',
       CurrencyName: 'Myanmar (Burma) Kyats',
       CurrencyAmountScale: 2,
       CurrencyRateScale: 4,
       Symbol: 'MMK',
       PaymentCutoffTime: '16:00',
       SettlementDaysToAdd: 0 },
     { CurrencyId: 141,
       CurrencyCode: 'THB',
       CurrencyName: 'Thai Baht',
       CurrencyAmountScale: 2,
       CurrencyRateScale: 3,
       Symbol: '฿',
       PaymentCutoffTime: '16:00',
       SettlementDaysToAdd: 0 },
     { CurrencyId: 153,
       CurrencyCode: 'USD',
       CurrencyName: 'US Dollars',
       CurrencyAmountScale: 2,
       CurrencyRateScale: 4,
       Symbol: '$',
       PaymentCutoffTime: '23:00',
       SettlementDaysToAdd: 2 } ] }

```
### CustomerAccountBalancesGet
#### Call
```python
args = {
    request: {
        ServiceCallerIdentity: {
            LoginId: userLogin,
            Password: userPassword,
            ServiceCallerId: callerId 
        },
        CustomerId: customerId // this is the userId from the priory called UserSettingsGetSingle
    }
};
```
Method: 
```python
var method = client['GPWebService']['BasicHttpsBinding_IGPWebService1']['CustomerAccountBalancesGet'];
```
#### Response
The Path:
```python
var balances = gpWebResult.CustomerAccountBalancesGetResult.Balances;

```
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
#### Call
```python
let args = {
    request: {
        ServiceCallerIdentity: {
            LoginId: userLogin,
            Password: userPassword,
            ServiceCallerId: callerId 
        },
        AccountId: accountId, // If you do not know them, you can find them in the response to CustomerAccountBalancesGet
        StartDate: "2018-01-01", // Date format is YYYY-MM-DD
        EndDate: "2018-12-01" // Date format is YYYY-MM-DD        
    }
};
```
Method: 
```python
var method = client['GPWebService']['BasicHttpsBinding_IGPWebService1']['CustomerAccountStatementGetSingle'];
```
#### Response
The Path:
```python
var transactions = gpWebResult.CustomerAccountStatementGetSingleResult.Entries;
```
> This is the main response object, even though there is more...
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
>The endpoints are listed alphabetically. IRL you would create a quote from a FX deal first
#### Call
```python
let args = {
    request: {
        ServiceCallerIdentity: {
            LoginId: userLogin,
            Password: userPassword,
            ServiceCallerId: callerId 
        },
        QuoteId: quoteId // comming from FXDealQuoteCreate
    }
}
```
Method: 
```python
var method = client['GPWebService']['BasicHttpsBinding_IGPWebService1']['FXDealQuoteBookAndInstantDeposit'];
```
#### Response
The Path:
```python
var gpWebResult = result.FXDealQuoteBookAndInstantDepositResult.FXDepositData;
```
The Object:
```python
{ FXDealId: 'an ID',
  FXDealReference: 'SPOT1009694',
  DepositId: 'an ID',
  DepositReference: 'DEPO1001106' }
```
>The FXDeal and Deposit references above will be different in your case

### FXDealQuoteCreate
#### Call
```python
let args = {
    request: {
        ServiceCallerIdentity: {
            LoginId: userLogin,
            Password: userPassword,
            ServiceCallerId: callerId 
        },
        CustomerId: customerId, // You know where to get this
        BuyCCY: "MMK",
        SellCCY: "THB",
        Amount: "1000.00",
        AmountCCY: "THB",
        DealType: "Spot",
        IsForCurrencyCalculator: false
    }
};
```
Method: 
```python
var method = client['GPWebService']['BasicHttpsBinding_IGPWebService1']['FXDealQuoteCreate'];
```
#### Response
The Path:
```python
var gpWebResult = result.FXDealQuoteCreateResult.Quote;
```
The Object:
```python
{ QuoteId: 'an ID',
  QuoteReference: 'QUOT1234203',
  QuoteSequenceNumber: '1234203',
  CustomerAccountNumber: '0123455667',
  DealType: 'SPOT',
  BuyAmount: '42071.00 MMK',
  BuyCurrencyCode: 'MMK',
  SellAmount: '1000.00 THB',
  SellCurrencyCode: 'THB',
  Rate: '42.071',
  RateFormat: 'THB / MMK',
  DealDate: '4/2/2018 12:00:00 AM',
  ValueDate: '4/4/2018 12:00:00 AM',
  QuoteTime: '2018-04-01T15:11:26.130Z',
  ExpirationTime: '2018-04-01T15:11:56.130Z',
  IsForCurrencyCalculator: false }
```

### GetCustomerAccountBalances
This is identical to the [CustomerAccountBalancesGet](#customeraccountbalancesget) endpoint and is listed for historical reasons only.

### GetLibraryVersion
#### Call
```python
let args = {
};
```
Method: 
```python
var method = client['GPWebService']['BasicHttpsBinding_IGPWebService1']['GetLibraryVersion'];
```
#### Response
The Path:
```python
var librayVersion = gpWebResult.GetLibraryVersionResult;
```
The Object:
```json
4.5.7.15
```
>Just use this example to see if your SOAP client is working allright

### InstantPaymentCreate
#### Call
```python
let args = {
    let args = {
        request: {
            ServiceCallerIdentity: {
                LoginId: userLogin,
                Password: userPassword,
                ServiceCallerId: callerId // iou_caller_id / bank id
            },
            FromCustomer: fromWallet, // that is an alias - check the wallet demmo for more information
            ToCustomer: toWallet, // that is an a;ias
            Amount: amount,
            CurrencyCode: currency,
            ValueDate: "",
            ReasonForPayment:"",
            ExternalReference: "",
            Memo:""
        }
    };
};
```
Method: 
```python
var method = client['GPWebService']['BasicHttpsBinding_IGPWebService1']['InstantPaymentCreate'];
```
#### Response
The Path:
```python
var gpWebResult = result.InstantPaymentCreateResult.PaymentInformation;
```
The Object:
```python
{ PaymentId: 'an ID',
  PaymentReference: 'INST1000857' }
```
>The payment references above will be different in your case
>The ID above will be used in the payment related calls following

### InstantPaymentGetSingle
>Even though the InstantPaymentCreate returns a paymentId, this InstantPaymentGetSingle service depends on a payment that is completed already.
> So this service is called after the InstantPaymentPost function as shown in the example.

#### Call
```python
let args = {
    request: {
        ServiceCallerIdentity: {
            LoginId: userLogin,
            Password: userPassword,
            ServiceCallerId: callerId
        },
        InstantPaymentId: paymentId
    }
};
```
Method: 
```python
var method = client['GPWebService']['BasicHttpsBinding_IGPWebService1']['InstantPaymentGetSingle'];
```
#### Response
The Path:
```python
var gpWebResult = result.InstantPaymentGetSingleResult.Payment;
```
The Object:
```python
{ PaymentId: 'an ID',
  PaymentReference: 'INST1000864',
  FromCustomerAlias: 'gFromWallet', // see axample code
  ToCustomerAlias: 'tToWallet', // see example code
  FromCustomerName: 'String',
  FromCustomerId: 'an ID',
  ToCustomerName: 'String',
  ToCustomerId: 'an ID',
  PaymentStatus: 'Posted',
  Amount: 20,
  AmountCurrencyScale: 2,
  CCY: 'THB',
  ValueDate: '2018-04-01T00:00:00.000Z',
  ProcessingBranchName: undefined,
  ProcessingBranchCode: undefined,
  CreatedTime: '2018-04-01T09:45:06.160Z',
  CreatedByName: 'String - fullanem of the gFromWallet',
  PostedTime: '2018-04-01T09:45:07.440Z',
  PostedByName: 'String',
  IsDeleted: false,
  ReasonForPayment: undefined,
  ExternalReference: undefined,
  BankMemo: undefined }
```
### InstantPaymentPost
#### Call
```python
let args = {
    request: {
        ServiceCallerIdentity: {
            LoginId: userLogin,
            Password: userPassword,
            ServiceCallerId: callerId
        },
        InstantPaymentId: paymentId
    }
};
```
Method: 
```python
var method = client['GPWebService']['BasicHttpsBinding_IGPWebService1']['InstantPaymentPost'];
```
#### Response
The Path:
```python
var gpWebResult = result.InstantPaymentPostResult;
```
The Object:
```python
{ ServiceResponse: 
   { HasErrors: false,
     HasWarnings: false,
     Responses: 
      { ServiceResponseData: 
         { ResponseCode: 0,
           ResponseType: 'Information',
           Message: 'Success',
           MessageDetails: 'Command completed successfully',
           FieldName: undefined,
           FieldValue: undefined } } } }
```
>Call the InstantPaymentGetSingle servcie to get all the details of  the successful payment

### UserSettingsGetSingle
>his service returns all the settings, The user id will be required in other services.

#### Call
```python
let args = {
    request: {
        ServiceCallerIdentity: {
            LoginId: userLogin,
            Password: userPassword,
            ServiceCallerId: callerId // iou_caller_id / bank id
        }
    }
};
```
Method: 
```python
var method = client['GPWebService']['BasicHttpsBinding_IGPWebService1']['UserSettingsGetSingle'];
```
#### Response
The Path:
```python
var userId = gpWebResult.UserSettingsGetSingleResult.UserSettings;
```
The Object:
```python
{ UserSettingsGetSingleResult: 
   { ServiceResponse: 
      { HasErrors: false,
        HasWarnings: false,
        Responses: 
         { ServiceResponseData: 
            { ResponseCode: 0,
              ResponseType: 'Information',
              Message: 'Success',
              MessageDetails: 'Command completed successfully',
              FieldName: undefined,
              FieldValue: undefined } } },
     UserSettings: 
      { AccessRights: 
         { AccessRightData: 
            [ 
                { 
                    AccessRightCategoryName: 'Customers',
                    AccessRightDescription: 'Manage all the users from the same customer.',
                    AccessRightId: 6,
                    AccessRightName: 'Manage Customer Users',
                    CanOverrideDualControl: false,
                    LimitAmount: 0,
                    UsesDualControl: false,
                    UsesLimitAmount: false 
                }
            ]

        },
        BankID: 'the bank ID code - 00000000-0000-0000-0000-000000000000',
        BaseCountryCode: 'US',
        BaseCurrencyCode: 'THB',
        BaseCurrencyID: 141,
        BelongsToWhiteLabelBranch: false,
        BranchID: 'The branch Id if any - 00000000-0000-0000-0000-000000000000',
        CultureCode: 'en-US',
        CultureID: 1,
        EmailAddress: 'yourKYCEmail address',
        Fax: "String or undefined",
        FirstName: 'String',
        IsACHBatchFeatureEnabled: true,
        IsBankAutoCoverFeatureEnabled: true,
        IsBankIncomingPaymentEnabled: true,
        IsBankInstantPaymentFeatureEnabled: true,
        IsCurrencyCalculatorEnabled: true,
        IsEnabled: true,
        IsFileAttachmentFeatureEnabled: true,
        IsLockedOut: false,
        IsManageCustomOFACListsFeatureEnabled: true,
        IsPaymentValueTypeEnabled: true,
        IsSWIFTMessageFeatureEnabled: true,
        IsTradeFinanceFeatureEnabled: true,
        IsTwoFactorAuthenticationFeatureEnabled: false,
        IsTwoFactorAuthenticationRequired: false,
        LastName: 'Hundertmark',
        LinkedAccessRightTemplateID: 'an ID 00000000-0000-0000-0000-000000000000',
        LinkedAccessRightTemplateName: 'AllCustomerAccessRight',
        OrganizationID: 'an ID - 00000000-0000-0000-0000-000000000000',
        OrganizationName: 'a String from your KYC',
        OrganizationTypeID: 2,
        PageTitle: undefined,
        Phone: undefined,
        Theme: 'TSG',
        UserId: '00000000-0000-0000-0000-000000000000 - That is the ID you want',
        UserName: 'Ralf4IOU',
        WhiteLabelProfileID: '00000000-0000-0000-0000-000000000000' } } }

```
>Note:
> The import field to use from the response is the UserId field has this is used in suquent calls of the webservice


## Wallet Demo

https://demoewallet.winstantpay.com/

## Support

Support for the WinstantPay API is available through the WinstantPay API team. We will share the details about how to interact with our teams at the end of the KYC process.  Should you have pUiany issues before that you can send a twitter message to us to <api@winstantpay.com>

## License

WinstantPay API example scripts are released under the MIT license.










