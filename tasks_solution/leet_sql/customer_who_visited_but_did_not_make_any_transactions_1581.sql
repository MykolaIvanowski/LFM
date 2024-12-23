
SELECT customer_id,count(customer_id)as count_no_trans
    FROM visits AS v
    LEFT JOIN transactions AS t ON v.visit_id = t.visit_id
    WHERE t.transaction_id IS NULL
group by customer_id
