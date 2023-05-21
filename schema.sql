CREATE TABLE usertable (
  id SERIAL PRIMARY KEY,
  login TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE product (
  id SERIAL PRIMARY KEY ,
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  price DECIMAL NOT NULL,
  picture TEXT NOT NULL,
  category TEXT NOT NULL,
  promotion INTEGER,
  unit TEXT NOT NULL
);


CREATE TABLE promotion (
  id SERIAL PRIMARY KEY ,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  percentage DECIMAL NOT NULL
);


CREATE TABLE category (
  id SERIAL PRIMARY KEY ,
  title TEXT NOT NULL
);