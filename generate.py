#!/usr/bin/python
# Generate icon theme in png

import os, re, string, sys

# Find inkscape/sodipodi
app = 'rsvg'

sizes = ['16x16', '22x22', '32x32', '48x48', '64x64']

print "Starting to generate png icons with %s" % (app)

for s in sizes:
	try: os.mkdir(s)
	except: pass
	(w,h) = string.split(s, 'x')
	for d in os.listdir('scalable'):
		try: os.mkdir('%s/%s' % (s, d))
		except: pass
		print "Working on %s/%s" % (s, d)
		for f in os.listdir('scalable/%s' % (d)):
			png = re.sub('svg', 'png', f)
			out = s + '/' + d + '/' + png
			if d == 'actions' and f == 'kde.svg':
				wh = '-w %s' % (w)
			else:
				wh = '-w %s -h %s' % (w,h)
			if app == 'rsvg':
				cmd = 'rsvg -w %s -h %s scalable/%s/%s %s' % (w, h, d, f, out)
			else:
				cmd = '%s -z %s -e %s -f scalable/%s/%s' % (app, wh, out, d, f)
			os.popen(cmd)
			print cmd
print "Done!"
