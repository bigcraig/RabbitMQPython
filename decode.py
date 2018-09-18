import base64
import zlib
import gzip
import StringIO
#data = 'H4sIAAAAAAAAAGWNwQ6CMAyG36VnSDYmaLgZ0cQr7AWWUZHIBtkKiTG+uwVv2lu///XFyxQwpIJuU/FARIg9MYTMxNCHxszYGQa7R3becBW9w6hlLnaqSyTYh1OyQT6T4oE0P9eqFzJBPzsKlx6y/KSV3pO3IGTo1jfLsbS+rML4zxdW+YUUyweqXUbd7HT336jj7WGzXYOYQwsE+8P6RLy0NIAAAA='
data='H4sIAAAAAAAAAGWNyw6CMBBF/2XWkPQhatgZH4lb6A/UMiqRFjItJMb47w6401meO/fcF0xQwqSE3ORiCxkkDDYkZpaojbXtMDKN7o7N2GFjWo9QykKvtFJSzMdpspT+Eq0ywPDb0MXMw+gPOLWO5aXk0efAP7D3KVbXk3Vp3rxRPw7nhnlnLzmuH7nzS+DjzXwLtdlVBhbdkagnton3B6WcD+7TAAAA'
#decoded_data = base64.b64decode(data+"===")
#idecoded_data= zlib.decompress(base64.b64decode(data+"==="))
#decode_data=zlib.decompress(base64.b64decode(response.json().get("data")), 16 + zlib.MAX_WBITS)
#decode_data=zlib.decompress(base64.b64decode(data+"==="), 16 + zlib.MAX_WBITS).decode('utf-8')

decoded_data=gzip.GzipFile(fileobj=StringIO.StringIO(base64.b64decode(data+"==="))).read()

print(" %r",decoded_data)

