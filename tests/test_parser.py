from crawler.vieclam24h.parser import get_source_job_id, parse_job_detail


def test_job_id_ignores_title_and_tracking_parameters():
    first = "https://vieclam24h.vn/it-phan-mem/developer-c8p122id200947717.html?open_from=1"
    renamed = "https://vieclam24h.vn/it-phan-mem/senior-developer-c8p122id200947717.html?open_from=2#details"
    assert get_source_job_id(first) == "200947717"
    assert get_source_job_id(renamed) == "200947717"
    assert get_source_job_id(first.replace("200947717", "200900419")) == "200900419"


def test_unknown_url_format_has_stable_distinct_fallback():
    url = "https://vieclam24h.vn/it-phan-mem/developer.html"
    assert get_source_job_id(url) == get_source_job_id(url + "?tracking=1#details")
    assert get_source_job_id(url) != get_source_job_id(url.replace("developer", "tester"))


def test_parser_assigns_extracted_job_id():
    html = '<div class="text-14 break-words text-se-neutral-80 leading-6 text-description">Description</div>' * 2
    url = "https://vieclam24h.vn/it-phan-mem/developer-c8p122id200947717.html"
    assert parse_job_detail(html, url)["source_job_id"] == "200947717"
