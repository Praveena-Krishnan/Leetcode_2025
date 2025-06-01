'''
LeetCode 607: Sales Person

Given three tables: SalesPerson, Company, and Orders, write a SQL query to find all salespersons who did not have any orders related to the company named 'RED'.

Tables:
- SalesPerson: Contains salesperson information.
- Company: Contains company information.
- Orders: Contains order records linking salespersons and companies.

Return the names of all salespersons who have never sold to the company 'RED'.
'''

SELECT DISTINCT S.name
FROM SalesPerson S
LEFT JOIN Orders O ON S.id = O.salespersonId
LEFT JOIN Company C ON O.companyId = C.id
WHERE C.name != 'RED' OR C.name IS NULL