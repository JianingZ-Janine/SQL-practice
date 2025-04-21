-- Schema for a simple e-commerce database
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date DATE,
    total_amount REAL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Sample data
INSERT INTO customers (name, email) VALUES
('Alice Smith', 'alice@example.com'),
('Bob Jones', 'bob@example.com'),
('Cathy Lee', 'cathy@example.com');

INSERT INTO orders (customer_id, order_date, total_amount) VALUES
(1, '2025-01-15', 99.99),
(1, '2025-02-10', 149.50),
(2, '2025-03-01', 49.99),
(3, '2025-04-01', 200.00);