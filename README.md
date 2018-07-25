# API Flask Currency

----------------

A set of APIs to be used to store and display foreign exchange to develop application that store and display foreign exchange.

----------------

## ADD Exchange Currency

```
POST http://localhost:5000/currencies
```

To add exchange currency


----------------

### Request

> 
> **Header**
> 
> |Key|Value|Description|
> |---|---|---|
> |Content-Type|application/json||
> 
> **Body**
> 
> ```
> {
> 	"from": "IDR",
> 	"to": "USD"
> }
> ```
> 



> 

----------------

## DELETE Exchange Currency

```
DELETE http://localhost:5000/currencies?from=IDR&to=USD
```

To remove exchange currency with 2 input parameters 

----------------

### Request

> 
> **Query**
> 
> |Key|Value|Description|
> |---|---|---|
> |from|IDR||
> |to|USD||
> 



> 

----------------

## ADD Exchange Rate

```
POST http://localhost:5000/rates
```

To input daily exchange rate data


----------------

### Request

> 
> **Header**
> 
> |Key|Value|Description|
> |---|---|---|
> |Content-Type|application/json||
> 
> **Body**
> 
> ```
> {
> 	"from": "IDR",
> 	"to": "USD",
> 	"date": "2018-07-24",
> 	"rate": 2000
> }
> ```
> 



> 

----------------

## GET All Exchange Rates By Date

```
GET http://localhost:5000/rates?date=2018-07-24
```

To get a list of exchange rates to be tracked

Average here means the average of exchange rate for the last 7 days, including date selected. For example, last 7 days in the example will
calculate the rate average from 26 Jun 2018 to 2 Jul 2018.



----------------

### Request

> 
> **Query**
> 
> |Key|Value|Description|
> |---|---|---|
> |date|2018-07-24||
> 



> 

----------------

----------------

Built with [Postdown][PyPI].

Author: [Akbar Binaji](https://github.com/akbarb24)

[PyPI]:    https://pypi.python.org/pypi/Postdown
