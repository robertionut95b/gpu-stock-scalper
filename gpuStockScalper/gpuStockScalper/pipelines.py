# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from win10toast import ToastNotifier
import webbrowser


class GpustockscalperPipeline:
    def process_item(self, item, spider):
        self.notify_in_stock(item)
        return item

    def notify_in_stock(self, item):
        if "IN_STOCK" in item.get('stock', ''):
            toaster = ToastNotifier()
            toaster.show_toast("GPU IN STOCK", "{}".format(item.get('url')),
                               duration=10,
                               threaded=True)
