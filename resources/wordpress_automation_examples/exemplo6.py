from woocommerce import *
import json
#import xlrd

wcapi = API(
    url="http://dominio.url/",
    consumer_key="ck_000000000000000000000000000000000",
    consumer_secret="cs_00000000000000000000000000000000",
    version="wc/v3",
    timeout=30
)

data = {
	"name": "pyBirras2",
	"type": "simple",
	"regular_price": "1",
	"description": "Segunda reunión PyBirras",
	"short_description": "pyBirras",
	}

r = wcapi.post("products", data).json
print(r)
