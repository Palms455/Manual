from dateutil import parser

def get_date(row_date):
	if len(row_date) < 4:
		raise  ParseError
	return parser.parse(row_date)
