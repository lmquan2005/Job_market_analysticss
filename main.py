from crawler.vieclam24h.crawler import crawl_jobs_from_pages
from tests.report import profile_jobs

from storage.storage import save_raw

if __name__ == "__main__":
    total_jobs = crawl_jobs_from_pages()
    save_raw(total_jobs)
    profile_jobs(total_jobs)
