-- INSERT INTO `person` (personID, lastName, firstName)
-- VALUES (1, 'Wang', 'Allen'),
--     (2, 'Alice', 'Bob');
-- INSERT INTO `address` (AddressID, personID, city, state)
-- VALUES (1, 2, 'New York City', 'New York');
SELECT firstName,
    lastName,
    city,
    state
FROM person
    LEFT JOIN address ON person.personID = address.personID
