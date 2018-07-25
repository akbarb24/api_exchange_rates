CREATE DATABASE exchange_db;

CREATE TABLE exchange_currencies
(
  id            INT AUTO_INCREMENT
    PRIMARY KEY,
  from_currency VARCHAR(3) NULL,
  to_currency   VARCHAR(3) NULL
)
  ENGINE = InnoDB;

CREATE TABLE exchange_rates
(
  id          INT AUTO_INCREMENT
    PRIMARY KEY,
  currency_id INT   NOT NULL,
  date        DATE  NULL,
  rate        FLOAT NULL,
  CONSTRAINT exchange_rates_ibfk_1
  FOREIGN KEY (currency_id) REFERENCES exchange_currencies (id)
)
  ENGINE = InnoDB;

CREATE INDEX currency_id
  ON exchange_rates (currency_id);