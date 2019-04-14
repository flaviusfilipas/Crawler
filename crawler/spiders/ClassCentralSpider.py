import scrapy
from crawler.items import CrawlerItem
import re
import nltk


class QuotesSpider(scrapy.Spider):
    name = "crawler"
    start_urls = [
        'https://www.classcentral.com/search?q=photography'
    ]

    def parse(self, response):
        base_url = 'https://www.classcentral.com'
        links = response.css('td.course-name-column a.course-name::attr(href)').getall()
        for link in links:
            if link[0] is not '/':
                continue
            else:
                yield scrapy.Request(base_url + link, callback=self.parse_course_info)

    def parse_course_info(self, response):
        item = CrawlerItem()
        item['title'] = response.css('h1#course-title::text').get().strip(' \n')
        item['provider'] = response.css('a.text-2::text').get().strip(' \n')
        item['link_to_course'] = response.css('a#btnProviderCoursePage::attr(href)').get().strip(' \n')
        overview_list = response.xpath('//div[@data-expand-article-target="overview"]/descendant-or-self::text()').getall()
        overview = ''.join(overview_list)
        item['overview'] = re.sub('\s+', ' ', overview).strip()
        start_date = response.css('select#sessionOptions option::attr(content)').get()
        item['start_date'] = re.sub('\s+', ' ', start_date)
        cost = response.css('li.border-box span.text-2::text').get()
        item['cost'] = re.sub('\s+', ' ', cost).strip()
        yield item
