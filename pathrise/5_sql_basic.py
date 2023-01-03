-- SQL
/*
Question
SQL - Product Sales Analysis I, II, III

Product Sales Analysis I
Write an SQL query that reports all product names of the products in the Sales table along with their selling year and price.
Result table:
+--------------+-------+-------+
| product_name | year  | price |
+--------------+-------+-------+
| Nokia        | 2008  | 5000  |
| Nokia        | 2009  | 5000  |
| Apple        | 2011  | 9000  |
+--------------+-------+-------+
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+ 
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+
Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |
+------------+--------------+


Product Sales Analysis II
Write an SQL query that reports the total quantity sold for every product id.

The query result format is in the following example:
Result table:
+--------------+----------------+
| product_id   | total_quantity |
+--------------+----------------+
| 100          | 22             |
| 200          | 15             |
+--------------+----------------+
Product Sales Analysis III
Write an SQL query that selects the product id, year, quantity, and price for the first year of every product sold.
Result table:
+------------+------------+----------+-------+
| product_id | first_year | quantity | price |
+------------+------------+----------+-------+ 
| 100        | 2008       | 10       | 5000  |
| 200        | 2011       | 15       | 9000  |
+------------+------------+----------+-------+

*/
-- Answer part 1
create table result as
select p.names, s.year, s.price
from  sales as s right join product as p on p.product_id = s.product_id; --so basically this line reads as join product and sales with respect to product_id column? Answer=Yes