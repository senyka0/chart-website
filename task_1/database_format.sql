CREATE TABLE IF NOT EXISTS data (
    id INT PRIMARY KEY AUTO_INCREMENT,
    symbol VARCHAR(10) NOT NULL,
    interval VARCHAR(10) NOT NULL,
    open_time DATETIME NOT NULL,
    open FLOAT NOT NULL,
    high FLOAT NOT NULL,
    low FLOAT NOT NULL,
    close FLOAT NOT NULL,
    volume FLOAT NOT NULL,
    close_time DATETIME NOT NULL,
    quote_asset_volume FLOAT NOT NULL,
    number_of_trades INT NOT NULL,
    taker_buy_base_asset_volume FLOAT NOT NULL,
    taker_buy_quote_asset_volume FLOAT NOT NULL,
    ignore INT NOT NULL
);