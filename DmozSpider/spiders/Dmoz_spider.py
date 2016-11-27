import scrapy
from DmozSpider.items import DmozSpiderItem

class DmozSpider(scrapy.Spider):
	# �������֣�Ψһ��
	name = "dmoz"
	# ������ȡ���ӵ�������Χ��ֻ�����б��е�������Χ����ȡ
	allowed_domains = ["dmoz.org"]
	# ��ʼ�������
	start_urls = [
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Modules/GUI/"
	]

	def parse(self,response):
		# ����������ȡ�������غ����Ӧ����

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