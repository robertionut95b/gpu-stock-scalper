import schedule
import time
import os

print('Scheduler initialised')
os.chdir("gpuStockScalper")
schedule.every(2).minutes.do(lambda: os.system('scrapy crawl gpu_spider -o items.json'))
print('Next job is set to run at: ' + str(schedule.next_run()))

if __name__ == '__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
