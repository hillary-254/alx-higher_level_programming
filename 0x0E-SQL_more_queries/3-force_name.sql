-- Create table force_name in the specified database

-- Create table if not exists
CREATE TABLE IF NOT EXISTS hbtn_0d_2.force_name (
    id INT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

-- Insert data
INSERT INTO hbtn_0d_2.force_name (id, name) VALUES (89, "Best School");

-- Attempt to insert data without specifying 'name'
-- This will result in an error
INSERT INTO hbtn_0d_2.force_name (id) VALUES (333);

-- Display data from force_name table
SELECT * FROM hbtn_0d_2.force_name;
