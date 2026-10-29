INSERT INTO tickets (ticket_id, requester_name, title, description, status, created_at)
	VALUES(1001, 'John', 'Printer not working', 'My printer will not connect', 'Open', NOW());

SELECT * FROM tickets;

SELECT ticket_id, title, status FROM tickets;

SELECT ticket_id, title, status FROM tickets WHERE status = 'Open';

INSERT INTO tickets (ticket_id, requester_name, title, description, status, created_at)
	VALUES(1002, 'Sarah', 'Wi-Fi connection issue', 'Cannot connect to Wi-Fi', 'Resolved', NOW());

SELECT ticket_id, title, status
FROM tickets
WHERE status = 'Open';

SELECT ticket_id, title, status
FROM tickets
WHERE status = 'Resolved';


SELECT ticket_id, title, status
FROM tickets
WHERE status <> 'Resolved';

SELECT ticket_id, title, status
FROM tickets
WHERE ticket_id > 1001;

SELECT ticket_id, title, status
FROM tickets
WHERE ticket_id >= 1001;

SELECT ticket_id, title, status
FROM tickets
WHERE status = 'Resolved' AND ticket_id > 1001;

SELECT ticket_id, title, status
FROM tickets
WHERE status = 'Open' OR ticket_id > 1001;

SELECT ticket_id, title, status
FROM tickets
WHERE (status = 'Open' OR requester_name = 'Sarah') AND ticket_id > 1001;

