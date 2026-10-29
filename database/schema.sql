CREATE TABLE tickets(
	ticket_id INTEGER PRIMARY KEY,
	requester_name TEXT,
	title TEXT,
	description TEXT,
	status TEXT,
	created_at TIMESTAMPTZ

);