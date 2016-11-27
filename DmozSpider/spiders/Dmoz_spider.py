import scrapy
from DmozSpider.items import DmozSpiderItem

class DmozSpider(scrapy.Spider):
	# 爬虫名字（唯一）
	name = "dmoz"
	# 爬虫爬取链接的域名范围，只能在列表中的域名范围内爬取
	allowed_domains = ["dmoz.org"]
	# 开始爬的起点
	start_urls = [
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Modules/GUI/"
	]

	def parse(self,response):
		# 解析器，获取链接下载后的响应数据

		# filename = response.url.split("/")[-2]
		# with open(filename + ".txt","wb") as f:
		# 	f.write(response.body)

		sel = scrapy.selector.Selector(response)
		sites = sel.xpath('//div[@class="title-and-desc"]')
		items = []
		for site in sites:
			item = DmozSpiderItem()
			item['title'] = site.xpath('a/div[@class="site-title"]/text()').extract()
			item['des'] = site.xpath('div[@class="site-descr"]/text()').extract()
			item['url'] = site.xpath('a/@href').extract()
			items.append(item)

		return items