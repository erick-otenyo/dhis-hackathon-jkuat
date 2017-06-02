import requests

base_url = 'https://play.dhis2.org/release1/api/'

org_unit_url = 'organisationUnits.json'
data_el_url = 'dataElements.json'
org_unit_geo = 'organisationUnits.geojson'
analy = '/25/analytics.json'


def get_org_units(query=None):
	params = {
		'paging': 'false',
		'query': query,
		'fields': 'name,code,level'
	}
	
	r = requests.get(base_url + org_unit_url, params=params, auth=('admin', 'district')).json()
	return r


def get_data_el(query=None):
	params = {
		'paging': 'false',
		'query': query,
		'fields': 'name,code'
	}
	r = requests.get(base_url + data_el_url, params=params, auth=('admin', 'district')).json()
	return r


def get_geojson(level=2):
	params = {
		'level': level
	}
	r = requests.get(base_url + org_unit_geo, params=params, auth=('admin', 'district'))
	return r


def get_analytics():
	params = {
		'dimension': 'dx:YtbsuPPo010;l6byfWFUGaP;s46m5MS0hxu',
		'dimension': 'pe:LAST_12_MONTHS',
		'filter': 'ou:ImspTQPwCqd&displayProperty=NAME',
		'skipMeta': 'false'
	}
	
	r = requests.get(
		'https://play.dhis2.org/release1/api/25/analytics.json?dimension=dx:YtbsuPPo010;l6byfWFUGaP;s46m5MS0hxu&dimension=pe:LAST_12_MONTHS&filter=ou:ImspTQPwCqd&displayProperty=NAME&skipMeta=false',
		auth=('admin', 'district'))
	return r
