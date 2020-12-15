# -*- coding: utf-8 -*-
from datetime import date
from libxml2 import htmlParseDoc
from urllib2 import urlopen

from models import Currency
from models import Exchange

def update():
    EXCHANGE_URL = 'http://www.brou.com.uy/web/guest/institucional/cotizaciones'
    html = urlopen(EXCHANGE_URL).read()
    htmldoc = htmlParseDoc(html, 'utf8')
    CURRENCIES = ('dolar', 'euro', 'argentino', 'real')

    # texto en celdas hermanas a la que tiene el nombre de la divisa:
    EXCHANGE_XPATH = \
        '//td[normalize-space(text())="%s"]/following-sibling::td/text()'
    
    for currency_slug in CURRENCIES:
        try:
            currency = Currency.objects.get(slug=currency_slug)
            params = {'currency': currency, 'date': date.today()}
            exchange = Exchange.objects.filter(** params)
            if exchange.count():
                exchange = exchange[0]
            else:
                exchange = Exchange(** params)
                exchange.buy, exchange.sale = [
                    td.get_content().replace(',', '.') for td in \
                        htmldoc.xpathEval2(EXCHANGE_XPATH % currency.name)]
                exchange.save()
        except Exception, e:
            print "ERROR:", currency_slug, e
