from playwright.sync_api import sync_playwright
import json

def scraper_amazon(str_url:str):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(str_url)
        page.locator('xpath=//*[@id="olpLinkWidget_feature_div"]/div[2]/span/a/div').first.click()
        page.wait_for_timeout(2000)
        # page.locator('xpath=//*[@id="aod-show-more-offers"]').scroll_into_view_if_needed()
        # page.wait_for_timeout(1000)
        # page.locator('xpath=//*[@id="aod-show-more-offers"]').click()
        dict_product = {}
        dict_product['title'] = page.locator('xpath=//*[@id="productTitle"]').first.inner_text()
        dict_product['price'] = page.locator('xpath=//*[@id="corePrice_feature_div"]/div/div/span[1]/span[1]').first.inner_text()
        dict_product['review_count'] = page.locator('xpath=//*[@id="acrCustomerReviewText"]').first.inner_text()
        dict_product['review_average'] = page.locator('xpath=//*[@id="acrPopover"]/span[1]/a/span').first.inner_text()
        dict_product['weight'] = page.locator('xpath=//*[@id="productDetails_detailBullets_sections1"]/tbody/tr[2]/td').first.inner_text()
        dict_product['dimensions'] = page.locator('xpath=//*[@id="productDetails_detailBullets_sections1"]/tbody/tr[1]/td').first.inner_text()
        dict_product['ASIN'] = page.locator('xpath=//*[@id="productDetails_detailBullets_sections1"]/tbody/tr[4]/td').first.inner_text()
        dict_product['model_number'] = page.locator('xpath=//*[@id="productDetails_detailBullets_sections1"]/tbody/tr[5]/td').first.inner_text()
        dict_product['ships_from'] = page.locator('xpath=//*[@id="fulfillerInfoFeature_feature_div"]/div[2]/div/span').first.inner_text()
        dict_product['sold_by'] = page.locator('xpath=//*[@id="merchantInfoFeature_feature_div"]/div[2]/div/span').first.inner_text()
        dict_product['sellers'] = page.locator('xpath=//*[@id="aod-offer"]').all_inner_texts()
        # dict_product[''] = page.locator('xpath=').first.inner_text()
        # dict_product[''] = page.locator('xpath=').first.inner_text()
        browser.close()

    json_product = json.dumps(dict_product,indent=2)
    with open('product_output.json','w') as json_file:
        json_file.write(json_product)

if __name__ == "__main__":
    scraper_amazon('https://www.amazon.com/LEGO-Classic-Large-Creative-Brick/dp/B00NHQF6MG?th=1')