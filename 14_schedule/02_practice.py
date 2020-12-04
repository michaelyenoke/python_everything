import schedule
import crawler 

def job():
    print("Start my scheduled job...")
    cw.run()
    for title, link in zip(cw.titles, cw.links):
        print("%s[%s]" % (title, link))

if __name__ == "__main__":
    cw = crawler.crawler()

    print("Initial crawling...")
    cw.run()

    schedule.every(10).seconds.do(job)

    while True:
        schedule.run_pending()
