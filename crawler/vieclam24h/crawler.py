import time

from crawler.fetcher import fetch_page
from crawler.vieclam24h.parser import (
    get_job_urls,
    parse_job_detail
)


def crawl_jobs( base_url):

    list_html = fetch_page(base_url)

    job_urls = get_job_urls(
        list_html,
        base_url
    )

    jobs = []

    for url in job_urls:

        try:
            html = fetch_page(url)

            job = parse_job_detail(
                html,
                url
            )

            jobs.append(job)

            time.sleep(1)

        except Exception as e:
            print(
                f"Failed: {url}",
                e
            )

    return jobs

def crawl_jobs_from_pages():
    total_jobs= []
    for page in range(1, 15):
        page_url = f"https://vieclam24h.vn/viec-lam-it-phan-mem-o8.html?page={page}&sort_q=priority_max%2Cdesc"
        print(f"Crawling page: {page_url}")
        jobs = crawl_jobs(page_url)

        total_jobs = total_jobs + jobs
    return total_jobs

def test_crawl():
    jobs = crawl_jobs("https://vieclam24h.vn/viec-lam-it-phan-mem-o8.html?page=1&sort_q=priority_max%2Cdesc")
    return jobs
