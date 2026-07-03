CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    job VARCHAR(100)
);

INSERT INTO users (name, job) VALUES
('Alice', 'Engineer'),
('Bob', 'Designer'),
('Charlie', 'DevOps Engineer');
