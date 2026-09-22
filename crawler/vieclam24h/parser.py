from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_text(soup, selector):
    element = soup.select_one(selector)
    if element:
        return element.get_text(" ", strip=True)
    return None

def get_job_urls(html, base_url):
    soup = BeautifulSoup(html, "html.parser")

    urls = []

    links = soup.select("a[href*='/it-phan-mem/']")

    for link in links:
        href = link.get("href")

        if href:
            full_url = urljoin(base_url, href)
            urls.append(full_url)

    return list(dict.fromkeys(urls))

def parse_job_detail(html, url):
    soup = BeautifulSoup(html, "html.parser")

    job = {
        "source": "vietjobs",
        "source_url": url,
        "source_job_id": '001',
        "title": get_text(soup, "h1[class='text-24 font-bold leading-10 text-se-neutral-84 !font-medium']"),
        "company_name": get_text(soup, 'a div[class="text-18 font-medium leading-7 text-se-neutral-84 !font-medium text-center w-full sm_cv:text-left"]'),
        "job_location_raw": get_text(soup, "div[class='flex flex-col w-full gap-3'] div[class='flex flex-col gap-2 w-full']"),
        "salary_raw": get_text(soup, 'div[class="text-14 font-normal leading-6 text-se-neutral-84 sm_cv:text-[#8B5CF6] md:!font-medium text-[#8B5CF6]"]'),
        "description": get_text(soup, "div[class='text-14 break-words text-se-neutral-80 leading-6 text-description']"),
        "requirements": None,
        "posted_date": get_text(soup, "div[class='w-full bg-gradient-400 p-4 rounded-[12px] sm_cv:rounded-[8px]'] div[class='text-14 font-normal leading-6 text-se-neutral-84 line-clamp-2 break-words']"),
        "expired_date": get_text(soup, "div[class='flex items-center gap-2 w-full sm_cv:flex-col sm_cv:items-start sm_cv:gap-1 sm_cv:hidden'] div[class='text-14 font-normal leading-6 text-se-neutral-84']"),
        "company_url": None,
        "company_location": get_text(soup, "div[class='flex flex-col gap-3 w-full p-5 bg-white rounded-[12px] shadow-sd-005 sm_cv:bg-transparent sm_cv:shadow-none sm_cv:p-0'] div[class='text-14 font-normal leading-6 text-se-neutral-84']")
    }

    requirements_element = soup.select("div[class='text-14 break-words text-se-neutral-80 leading-6 text-description']")[1]
    if requirements_element:
        job["requirements"] = requirements_element.get_text(
            " ",
            strip=True
        )

    return job