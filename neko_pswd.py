import urllib2
import json

resp = urllib2.urlopen("http://hpmobile.jp/app/nekoatsume/neko_daily.php")
pswd = unicode(resp.read().split(",")[1], 'utf-8').encode('utf-8')

resp = urllib2.urlopen("http://beta.jisho.org/api/v1/search/words?keyword="+pswd)
data = json.load(resp)

print "Word:\t\t" + data["data"][0]["japanese"][0]["word"]
print "Reading:\t" + data["data"][0]["japanese"][0]["reading"]
print "English:\t" +", ".join( data["data"][0]["senses"][0]["english_definitions"])
