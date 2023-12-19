CREATE DATABASE finalproject;
USE finalproject;

CREATE TABLE california_ischemic_stroke_data (
    County VARCHAR(50),
    Hospital VARCHAR(100),
    Measure VARCHAR(50),
    Risk_Adjusted_Rate FLOAT,
    Deaths_Readmissions INT,
    Cases INT,
    Hospital_Ratings VARCHAR(50)
);
