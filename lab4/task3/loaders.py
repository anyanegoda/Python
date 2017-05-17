import json
import xml.dom.minidom
from model import Author


class json_loader(object):

    @staticmethod
    def parse_loaded_dict(loaded_dict):
        return Author(name=loaded_dict['name'],
                      country=loaded_dict['country'],
                      years='-'.join(map(str, loaded_dict['years']))
                            if len(loaded_dict['years']) > 1
                            else ''.join(loaded_dict['years']))

    @staticmethod
    def load(string):
        loaded = json.loads(string)
        if isinstance(loaded, list):
            return [json_loader.parse_loaded_dict(item) for item in loaded]
        else:
            return [json_loader.parse_loaded_dict(loaded)]

    @staticmethod
    def dump(author):
        return json.dumps({'name': author.name,
                           'country': author.country,
                           'years': author.years.split('-')})


class xml_loader(object):

    @staticmethod
    def load(string):
        parsed = xml.dom.minidom.parseString(string)
        author = parsed.getElementsByTagName('author')[0]
        name = author.getElementsByTagName('name')[0].firstChild.data
        country = author.getElementsByTagName('country')[0].firstChild.data
        years = author.getElementsByTagName('years')[0]
        return [Author(name=name,
                       country=country,
                       years='-'.join((years.attributes['born'].value,
                                       years.attributes['died'].value)))]

    @staticmethod
    def dump(author):
        try:
            document = xml.dom.minidom.Document()
            dom_author = document.createElement('author')
            dom_name = document.createElement('name')
            dom_name.appendChild(document.createTextNode(author.name))
            dom_author.appendChild(dom_name)
            dom_country = document.createElement('country')
            dom_country.data = author.country
            dom_country.appendChild(document.createTextNode(author.country))
            dom_author.appendChild(dom_country)
            dom_years = document.createElement('years')
            years = author.years.split('-')
            if len(years) < 2:
                years.append('')
            (dom_years.attributes['born'],
             dom_years.attributes['died']) = years
            dom_author.appendChild(dom_years)
            document.appendChild(dom_author)
            return document.toprettyxml()
        except BaseException as e:
            print(e)
            raise
