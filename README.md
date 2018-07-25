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

### Request Example

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
DELETE http://localhost:5000/currencies?from=FROM_PARAM&to=TO_PARAM
```

To remove exchange currency with 2 input parameters 
FROM_PARAM and TO_PARAM are an `input_field`
----------------

### Request Example

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

### Request Example

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
GET http://localhost:5000/rates?date=DATE
```

To get a list of exchange rates to be tracked

Average here means the average of exchange rate for the last 7 days, including date selected. For example, last 7 days in the example will
calculate the rate average from 26 Jun 2018 to 2 Jul 2018.

DATE is an `input_field`



----------------

### Request Example

> 
> **Query**
> 
> |Key|Value|Description|
> |---|---|---|
> |date|2018-07-24||
> 
> 

----------------
## Database Structure

![alt text](https://raw.githubusercontent.com/akbarb24/api_exchange_rates/master/doc/database_structure.png)

> `exchange_currency` table to store a couple of Foreign Currency that will be compared. `from_currency`column stores a From Currency data to compare. `to_currency` column stores a To Currency data to compare.
>
> `exchange_rates` table to store a rates value of Foreign Exchange Currency daily. `currency_id` column stores a foreign key  from `exchange_currency`. `date` column stores a Foreign Exchange Currency date information. `rates` column stores a rates > value of Foreign Exchange Currency.
----------------

Built with [Postdown][PyPI].

Author: [Akbar Binaji](https://github.com/akbarb24)

[PyPI]:    https://pypi.python.org/pypi/Postdown
