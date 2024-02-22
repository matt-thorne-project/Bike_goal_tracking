CREATE TABLE t_measurements (
    id int NOT NULL AUTO_INCREMENT,
    Date date NOT NULL,
    ftp int,
    weight float,
    body_fat float,
    notes varchar(255)
    PRIMARY KEY (id)
);


CREATE TABLE t_blood_pressure (
    id int NOT NULL AUTO_INCREMENT,
    date date NOT NULL,
    hr int,
    systolic int,
    diastolic int,
    notes varchar(255),
    PRIMARY KEY(id)
);



CREATE TABLE t_interval_power_weight (
    id int NOT NULL AUTO_INCREMENT,
    date date NOT NULL,
    60_sec float,
    5_min float,
    20_min float,
    60_min
    90_min float,
    PRIMARY KEY(id)
);