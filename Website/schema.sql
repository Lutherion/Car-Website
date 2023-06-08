CREATE TABLE IF NOT EXISTS Cars(
	Cars_id integer PRIMARY KEY,
    Name varchar(255),
	Available_since date,
    German_price integer,
    Netherlands_price integer,
    UnitedKingdom_price integer,
    Battery integer,
    Acceleration integer,
    Top_speed integer,
    Range integer,
    Efficiency integer,
    Fast_charge integer,
    Towing integer,
    Seats integer
);

CREATE TABLE IF NOT EXISTS Users(
	C_id integer PRIMARY KEY,
    C_name varchar(20),
    C_email varchar(255),
    C_password varchar(120)
);

CREATE TABLE IF NOT EXISTS favBrand(
	C_id integer REFERENCES Users(C_id),
    Cars_id integer REFERENCES Cars(Cars_id),
    PRIMARY KEY (C_id, Cars_id)
);

CREATE TABLE IF NOT EXISTS usageReason(
    C_id integer REFERENCES Users(C_id),
    Cars_id integer REFERENCES Cars(Cars_id),
    Usage varchar(255),
	PRIMARY KEY (C_id, Cars_id)
);