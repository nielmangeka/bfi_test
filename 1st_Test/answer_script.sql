-- running on postgres
SELECT 
	owner,
	split_part(owner, '(a.k.a. ', 1) as owner_name_1,
	TRIM(translate(translate(SUBSTRING(split_part(owner, 'a.k.a', 2) FROM POSITION('.' IN split_part(owner, 'a.k.a', 2))),'.',''),';','')) AS owner_name_2,
	TRIM(REPLACE(TRANSLATE(SUBSTRING(owner FROM POSITION('; a.k.a. ' IN owner) FOR POSITION('),' IN owner) - POSITION('; a.k.a. ' IN owner)) ,';',''),'a.k.a.','')) AS owner_name_3,
	TRIM(REPLACE(SUBSTRING(split_part(owner, ';',2) FROM POSITION('),' IN split_part(owner, ';',2))), '),','')) as address,
	TO_CHAR(CAST(REPLACE(SUBSTRING(owner FROM POSITION('DOB ' IN owner) FOR POSITION('; POB' IN owner) - POSITION('DOB ' IN owner)),'DOB ','') AS DATE), 'yyyymmdd') as dob,
	REPLACE(SUBSTRING(owner FROM POSITION('POB ' IN owner) FOR POSITION('; Gender' IN owner) - POSITION('POB ' IN owner)), 'POB ','') as pob,
	REPLACE(SUBSTRING(owner FROM POSITION('Gender ' IN owner) FOR POSITION(' (individual)' IN owner) - POSITION('Gender ' IN owner)),'Gender ','') AS gender
from customer_asset;