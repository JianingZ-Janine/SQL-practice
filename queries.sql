SELECT c.name, COUNT(o.order_id) as order_count
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name;

SELECT order_id, total_amount
FROM orders
WHERE total_amount > 100;

WITH HighValueCustomers AS (
    SELECT customer_id, SUM(total_amount) as total_spent
    FROM orders
    GROUP BY customer_id
    HAVING total_spent > 150
)
SELECT c.name, h.total_spent
FROM customers c
JOIN HighValueCustomers h ON c.customer_id = h.customer_id;

SELECT order_id, total_amount,
       RANK() OVER (ORDER BY total_amount DESC) as amount_rank
FROM orders;

SELECT strftime('%Y-%m', order_date) as month,
       SUM(total_amount) as total_sales,
       COUNT(order_id) as order_count
FROM orders
GROUP BY month
ORDER BY month;