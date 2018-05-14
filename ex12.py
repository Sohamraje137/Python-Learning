
import json
value=""" 
{
	"title": "Tron:Legacy",
	"compser":"Soham",
	"release_year":2018,
	"budget":1700000,
	"actors":null,
	"won_oscar":false
}"""

tron=json.loads(value)
print(tron) 