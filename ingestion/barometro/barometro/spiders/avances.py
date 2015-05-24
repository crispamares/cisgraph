# -*- coding: utf-8 -*-
import scrapy
from barometro.items import AvanceItem


class AvancesSpider(scrapy.Spider):
    name = "avances"
    allowed_domains = ["www.cis.es"]
    start_urls = (
        'http://www.cis.es/cis/opencms/ES/11_barometros/avances.html',
    )

    def parse(self, response):
        for avance in response.css(".resultados_busqueda li"):
            item = AvanceItem()

            item["barometro_id"] = int(avance.re("\D(\d{4})\D<")[0])
            month, year = avance.xpath("a/text()").re("(\w*) de (\d{4})")
            item["month"], item["year"] = month, int(year)
            link = "http://www.cis.es" + avance.xpath("a/@href").extract()[0]
            item["download_link"] = link

            request = scrapy.Request(link, callback=self.parse_download)
            request.meta['item'] = item
            yield request

    def parse_download(self, response):
        print "**********", response
        item = response.meta['item']
        item["file_urls"] = response.css(".resultados_busqueda li a").xpath("@href").extract()

        return item
