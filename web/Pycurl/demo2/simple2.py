import pycurl
import io

url = "https://www.baidu.com/"
crl = pycurl.Curl()
crl.setopt(pycurl.VERBOSE, 1)
crl.setopt(pycurl.FOLLOWLOCATION, 1)
crl.setopt(pycurl.MAXREDIRS, 5)
crl.fp = io.StringIO()
crl.setopt(pycurl.URL, url)
crl.setopt(crl.WRITEFUNCTION, crl.fp.write)

crl.perform()

print(crl.fp.getvalue())
