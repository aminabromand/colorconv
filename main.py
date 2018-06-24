from flask import Flask, redirect
from flask import render_template


app  = Flask(__name__)

@app.route('/')
def home_page():
	startcolorcode = 'rgb(0, 191, 255)'
	startcolorformat = 'any'
	targetcolorformat = 'any'
	context = {
		'title': 'my title',
		'content': 'my content',
		'color': startcolorcode,
		'startcolorformat': startcolorformat,
		'targetcolorformat': targetcolorformat,
	}
	return render_template('home_page.html', **context)

@app.route('/<target>')
def conv_page(target):
	paramlist = target.split('2')
	iterator = iter(paramlist or [])
	startcolorformat = next(iterator, 'Any')
	startcolorcode = colormap.get(startcolorformat, None)

	if startcolorcode is None:
		return redirect("/", code=302)
	
	targetcolorformat = next(iterator, None)
	if targetcolorformat is not None:
		targetcolorcode = colormap.get(targetcolorformat, None)
		if targetcolorcode is None:
			return redirect("/{0}".format(startcolorformat), code=302)
	else:
		targetcolorformat = 'any'

	context = {
		'title': 'my title',
		'content': 'my content',
		'color': startcolorcode,
		'startcolorformat': startcolorformat,
		'targetcolorformat': targetcolorformat,
	}
	return render_template('home_page.html', **context)

colormap = {
	'name': 'DeepSkyBlue',
	'rgb': 'rgb(0, 191, 255)',
	'hex': '#00bfff',
	'hsl': 'hsl(195, 100%, 50%)',
	'hwb': 'hwb(195, 0%, 0%)',
	'cmyk': 'cmyk(100%, 25%, 0%, 0%)',
	'ncol': 'C25, 0%, 0%',
}
