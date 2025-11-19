-- Creates another table with new data

CREATE TABLE IF NOT EXISTS second_table(
    id INT,
    NAME VARCHAR(256),
    score INT
);

-- Create new records

INSERT INTO second_table (id, name, score)
VALUES 
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);
