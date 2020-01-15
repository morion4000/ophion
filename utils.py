import csv
import codecs

from django.conf import settings


def set_layout_session(request, template, view):
    session_name = "layout_%s" % view
    default = settings.DEFAULT_LAYOUT

    if not request.session.get(session_name):
        request.session[session_name] = (default[0], default[1] % template)

    if request.method == 'POST':
        layout = request.POST['layout']
        matched_layout = [l for l in settings.LAYOUTS if l[0] == layout]
        matched_layout = matched_layout[0] if len(matched_layout) > 0 else default
        request.session[session_name] = (matched_layout[0], matched_layout[1] % template)


def parse_csv_file(file):
	dialect = csv.Sniffer().sniff(codecs.EncodedFile(file, "utf-8").read(1024))
	file.open()
	reader = csv.DictReader(codecs.EncodedFile(file, "utf-8"), dialect=dialect)

	return reader
