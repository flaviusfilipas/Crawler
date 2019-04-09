import scrapy


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
                print(link)
                continue
            else:
                yield scrapy.Request(base_url + link, callback=self.parse_course_info)

    def parse_course_info(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        item = {
            'title': response.css('h1#course-title::text').get().strip(' \n'),
            'provider': response.css('a.text-2::text').get().strip(' \n'),
            'link_to_course': response.css('a#btnProviderCoursePage::attr(href)').get().strip(' \n')
        }
        yield item
