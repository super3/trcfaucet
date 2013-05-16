from flask import Flask
from DripRequest import *
app = Flask(__name__)

# Globals
DATABASE_FILE = 'trc.db'
DATABASE_TABLE = 'drip_request'
DEFAULT_SEND_VAL = 0.0001

# Helper Functions
def sub_cypher(num, offset):
	"""Number substitution offset cypher. Don't use offset values 0-9."""
	# rotate((ip % sum1bits(ip) ), sum0bits(ip))
	return [(abs(int(x) - offset)%10) if x.isdigit() else '.' for x in num]

def get_index(form_submit_status = None):
	"""Displays the default index page, or a success/error page."""
	# captcha = (random.randrange(1, 15), random.randrange(1, 15))
	# captcha_awns = captcha[0] + captcha[1]
	# recent_drips = Database(DATABASE_FILE, DATABASE_TABLE).get_recent()
	# recent_drips_html = [get_html(x[1], x[2], x[5]) for x in recent_drips if True]
	# recent_drips_html = ''.join(map(str, recent_drips_html))

	return render_template('index.html')

# Routes
@app.route('/')
def index():
	get_index()

if __name__ == '__main__':
	app.run()