--Ex 1:
SELECT username
FROM Users
WHERE username ~ '^dev_'

--Ex. 2
SELECT email
FROM Contacts
WHERE email ~ '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

--Ex. 3
SELECT conditions
FROM Patients
WHERE conditions ~ '(^|,|\s)DIAB1(\s|,|$)'

--Ex.4
SELECT password
FROM Accounts
WHERE password ~ '^.{8,}$'
AND password ~'[a-z]'
AND password ~ '[A-Z]'
AND password ~ '[0-9]'
AND password ~ '[!@#$%^&*]'
--how to do length at least 8?

--Ex.5
SELECT url
FROM Links
WHERE url ~ '^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$' 