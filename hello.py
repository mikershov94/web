def wsgi_app(environ, start_response):
	query = environ['QUERY_STRING'].split('&')
	for i in range(len(query)):
		query[i] += '\n'
	body = [bytes(i, 'ascii') for i in query]
	status = '200 OK'
	headers = [
		('Content-Type', 'text/plain')
	]
	start_response(status, headers)
	return body

#Gunicorn config
bind = '0.0.0.0:8000'
		