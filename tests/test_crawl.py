from crawler.vieclam24h.crawler import test_crawl
from storage.test_storage import save_raw

def test_crawl_jobs_from_pages():
    jobs = test_crawl()
    if not jobs:
        print("No jobs were crawled.")
    else:
        print(f"Crawled {len(jobs)} jobs.")
        save_raw(jobs)

if __name__ == "__main__":
    print("Starting the crawl test...")
    test_crawl_jobs_from_pages()