import scrapy
from ..items import GpustockscalperItem


class GPUSpider(scrapy.Spider):
    name = "gpu_spider"
    allowed_domains = ["pcgarage.ro", "emag.ro", "evomag.ro"]

    start_urls = [
        "https://www.pcgarage.ro/cauta/rtx+3080",
        "https://www.emag.ro/search/rtx%203080?ref=effective_search",
        "https://www.evomag.ro/componente-pc-gaming-placi-video/asus-placa-video-asus-geforce-rtx-3080-tuf-gaming"
        "-10gb-gddr6x-320-bit-3798493.html",
        "https://www.evomag.ro/componente-pc-gaming-placi-video/msi-placa-video-msi-geforce-rtx-3080-gaming-x-trio"
        "-10gb-gddr6x-320-bit-3798543.html",
        "https://www.evomag.ro/componente-pc-gaming-placi-video/asus-placa-video-asus-geforce-rtx-3080-rog-strix-10gb"
        "-gddr6x-320-bit-3798527.html",
    ]

    def parse(self, response, **kwargs):
        if "pcgarage" in response.url:
            products = response.css(".product_box_container")
            for product in products:
                item = GpustockscalperItem()
                product_box_availability = product.css(".product_box_availability").extract()
                product_title = product.css(".product_box_name a::attr(title)")[0].extract()
                if "placa video" not in str.lower(product_title):
                    continue
                item["name"] = product_title
                if "instock" in str(product_box_availability).lower():
                    item["stock"] = "IN_STOCK"
                else:
                    item["stock"] = "OUT_OF_STOCK"
                item["url"] = product.css(".product_box_name a::attr(href)")[0].extract()
                yield item
        elif "emag" in response.url:
            products = response.css("#card_grid .card-item")
            for product in products:
                item = GpustockscalperItem()
                product_title = product.css(".card-section-mid a::attr(title)")[0].extract()
                product_box_stock = response.css("#card_grid .card-item")[0]\
                    .css(".card-section-btm").css(".product-stock-status::text")[0].extract()
                if "placa video" not in str.lower(product_title):
                    continue
                item["name"] = product_title
                if "în stoc" in str(product_box_stock).lower():
                    item["stock"] = "IN_STOCK"
                else:
                    item["stock"] = "OUT_OF_STOCK"
                item["url"] = product.css(".card-section-mid a::attr(href)")[0].extract()
                yield item
        elif "evomag" in response.url:
            item = GpustockscalperItem()
            product_title = response.css(".product_name::text")[0].extract().strip()
            product_box_stock = response.css(".stoc_produs a span")[0].extract()
            item["name"] = product_title
            if "epuizat" in str(product_box_stock).lower():
                item["stock"] = "OUT_OF_STOCK"
            else:
                item["stock"] = "IN_STOCK"
            item["url"] = response.url
            yield item
