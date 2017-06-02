from django.http import HttpResponse
from django.shortcuts import render

from .utils import get_org_units, get_data_el, get_geojson, get_analytics


def org_view(request):
	if 'q' in request.GET:
		q = request.GET['q']
		org_units = get_org_units(query=q)
	else:
		org_units = get_org_units()
	
	data = []
	for org in org_units['organisationUnits']:
		data.append(org)
	
	context = {
		'org_units': data
	}
	return render(request, 'index.html', context)


def data_elements_view(request):
	if 'q' in request.GET:
		q = request.GET['q']
		data_elements = get_data_el(query=q)
	else:
		data_elements = get_data_el()
	data = []
	for el in data_elements['dataElements']:
		data.append(el)
	
	context = {
		'data_els': data
	}
	return render(request, 'data_el.html', context)


def org_map_data(request):
	geo_data = get_geojson()
	return HttpResponse(geo_data)


def map_view(request):
	return render(request, 'gis.html')


def analytics(request):
	an_data = get_analytics()
	context = {
		'data': an_data
	}
	return render(request, 'analytics.html', context)
