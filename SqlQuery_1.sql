/*
This is a remark

AS = alias


*/

USE Movies_DB
SELECT TOP 15 WITH TIES   // repeated are counted as 1, so I may get more than 15  
	firstname AS First-Name,
	lastname AS Last-Name,
	city
FROM
  table01
WHERE
	filename LIKE '%die hard%' AND// anywhere there is die hard
	lastname <> 'David' OR // execlude lines where lastname="David"
	city NOT LIKE '%TORONTO%' // execlude lines where city has TORONTO somewhere in it
GROUP BY 
	city WITH ROLLUP
ORDER BY
	firstname DESC  // or ASC




	

SELECT EMPLOYEE.first_name, EMPLOYEE.INCOME, WEALTH.wealth_Status
FROM EMPLOYEE
INNER JOIN WEALTH ON EMPLOYEE.income = WEALTH.income
GROUP BY  EMPLOYEE.income
ORDER BY  EMPLOYEE.first_name
LIMIT 0 , 300