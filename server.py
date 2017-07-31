import sys, os
abspath = os.path.dirname(__file__)
sys.path.append(abspath)
import site
site.addsitedir('/home/ram/dev/myenv/lib/python2.6/site-packages/')
import web
import json
import suggester

urls = (
	'/', 'suggest_ugly',
	'/seq/(.*)', 'suggest_pretty'
)

class suggest_ugly:
	def GET(self):
		i = web.input(seq=None)
		return do_suggest(i.seq)

class suggest_pretty:
    def GET(self, seq):
	return do_suggest(seq)
        
def do_suggest(seq):
	suggestions = suggester.keysearch(seq)
        web.header('Content-Type', 'application/json')
        web.header('Access-Control-Allow-Origin', '*')
        desc = [{'word': a, 'count': b} for a,b in sorted(suggestions.iteritems(), key = lambda x: x[1], reverse=True)]
        return json.dumps({'suggestions': desc})

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
    
suggester.train(os.path.join(abspath, 'alice_in_wonderland.txt'))
web.debug = False
application = web.application(urls, globals(), autoreload=False).wsgifunc()
