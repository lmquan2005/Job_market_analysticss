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
    for page in range(1, 4):
        page_url = f"https://www.vietjobs.vn/vi%E1%BB%87c-l%C3%A0m-c%C3%B4ng-ngh%E1%BB%87-th%C3%B4ng-tin-cntt-30?page={page}"
        print(f"Crawling page: {page_url}")
        jobs = crawl_jobs(page_url)

        total_jobs = total_jobs + jobs
    return total_jobs