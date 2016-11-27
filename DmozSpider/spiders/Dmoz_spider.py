import scrapy

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

		filename = response.url.split("/")[-2]
		with open(filename + ".txt","wb") as f:
			f.write(response.body)