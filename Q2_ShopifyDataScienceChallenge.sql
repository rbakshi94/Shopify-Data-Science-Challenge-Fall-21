------------------------- Question 2 --------------------------------------------------------------------
--By Rajat Bakshi

--A)
--Nested SQL statement where ShipperID from Shippers table is identified, then passed into another query that 
--calculates and displays Count of orders with the appropriate Shipper ID.
SELECT COUNT(*) FROM Orders WHERE ShipperID=(SELECT ShipperID FROM Shippers WHERE ShipperName="Speedy Express");
--ANS: 54

--B)
--The following query is used to identify employee ID with the most orders. EmployeeID field is grouped by 
--COUNT and ordered from highest to lowest, with only the highest being outputted.
SELECT *
FROM Orders
GROUP BY EmployeeID
ORDER BY COUNT(*) DESC
LIMIT 1
--The above query is then nested into a query getting employee name given EmployeeID using Employees table.
--The result is as follows:
SELECT LastName FROM Employees WHERE EmployeeID=(SELECT EmployeeID
FROM Orders
GROUP BY EmployeeID
ORDER BY COUNT(*) DESC
LIMIT 1)
--ANS: Peacock

--C)
--The following query sums the Quantity field while grouping by ProductID, in effect yielding
--a table where Product IDs are uniquely listed alongside summed Quantity field. The last two lines
--order the table by greatest quantity first, and only showing the first entry.
SELECT ProductID, SUM(Quantity)
FROM OrderDetails
GROUP BY ProductID
ORDER BY SUM(Quantity) DESC
LIMIT 1
--The above query, which returns a table with ProductID and Total Quantity of the most
--ordered product (one row) is then nested into a query that returns product name given ProductID using Products table
--The result is as follows:
SELECT ProductName FROM Products WHERE ProductID = (SELECT ProductID FROM (
SELECT ProductID, SUM(Quantity)
FROM OrderDetails
GROUP BY ProductID
ORDER BY SUM(Quantity) DESC
LIMIT 1))
--ANS: Gorgonzola Telino
