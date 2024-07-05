# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import json
import re
import uuid
import hashlib
import scrapy
from datetime import datetime
from lahtis.items import LahtisItem
from pyquery import PyQuery as pq

class DubiCarsSpider(scrapy.Spider):
    name= 'lahtis'
    # headers = {
    #     'accept': '*/*',
    #     'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    #     # 'cookie': 'DDC.postalCode=; locale=en_US; ddc_diag_akam_clientIP=197.133.224.234; DDC.postalCityState=CAIRO%2C%20%2C%20EG; DDC.userCoordinates=30.05%2C31.25; activeSession=true; __ssoid=48dcf135451a4f5e9c5f2c54a386e3c0; callTrackingSessionId=xtk1mir8kely95o7z4; _gtm_group=false; _gid=GA1.2.296007295.1720211771; calltrk_referrer=direct; calltrk_landing=https%3A//www.lahtis.net/; _ga_last=GA1.2.1971229608.1720211771; ak_bmsc=E4D773FC25CC15BBF1308167C0AD6BD5~000000000000000000000000000000~YAAQt48hFz6PLn6QAQAARJKchBhpYtwcKqS2vkP0KliV3NEj4n/tudGCSvsE6k4g16dcYH8+5fSGDzBiynh7hhq1QVwsafzsAFsSdICt0DUlUROADueoqcVVS2nHdEJcDQ/hDKbGiDRduxftO3W4PdJiIOtCgen83jOmIuiPYZe0WIk9hPkEiTKefZ3z36vhy/ZDNFGTapNbcURydKThDeeXGeUzFlh3vbs/4aOzCPZdG/6eRXvjmG0RIb3eDZZnMTku+tE/khFuEUsk7+sw8nwooRrbT6JsGMV3XmKIHYYbPEED9a3+U7po/VFNNju0G9lWfIdGAkzEgwIOKlwyF3jQzxVnsbGGiN1yOWV0HJ1EP/OKVlCJ2hDNJKwPg4cRiy9Y54GiZOat6kqPwsF4uvLWDWMAQCH78Jj0pipOELHuMGTAFnO5idE0OCJNnunx9o29e4pO9GXAP6m5jCHF; fullthrottlelims_t2=3026904178; r=1; AMP_MKTG_16a5c84b5b=JTdCJTdE; AMCVS_3ECF483F53AB366E0A490D44%40AdobeOrg=1; ddc_abcamm_cache=; ddc_abcc_cache=; AMCV_3ECF483F53AB366E0A490D44%40AdobeOrg=179643557%7CMCIDTS%7C19910%7CMCMID%7C39358182435529676643645083881090814897%7CMCAAMLH-1720816573%7C6%7CMCAAMB-1720816573%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1720218973s%7CNONE%7CMCSYNCSOP%7C411-19917%7CMCAID%7CNONE%7CvVersion%7C5.5.0; _aeaid=248957e7-c129-4f74-a1eb-07b0dde9bc7d; s_cc=true; aelastsite=0zvcQKFJVAkiljTUKCTR1nMIJ7FQl5wMH0oMzO1MU3klsvF%2FcQiEQHDqs6BY3%2FfP; aelreadersettings=%7B%22c_big%22%3A0%2C%22rg%22%3A0%2C%22memph%22%3A0%2C%22contrast_setting%22%3A0%2C%22colorshift_setting%22%3A0%2C%22text_size_setting%22%3A0%2C%22space_setting%22%3A0%2C%22font_setting%22%3A0%2C%22k%22%3A0%2C%22k_disable_default%22%3A0%2C%22hlt%22%3A0%2C%22disable_animations%22%3A0%2C%22display_alt_desc%22%3A0%7D; s_vnc365=1751747774806%26vn%3D1; s_ivc=true; __td_signed=true; _sda:stellantis:T3:user=0a051e9b-389e-44b7-8618-88909e2df0ce%3A4.0%3A1720211775431%3A3ekg5hp404ex0!a1ef904e9f311cb3e0663b93f055fa1c!2opprm2lxqnfu!%3A65828!65828!65828!; vlVisitCreatedUtc=Sat, 06 Jul 2024 08:36:18 GMT; lmc=17193.1720211778128.3736; ipe_s=fdae60ab-fd7a-daed-ce4a-359182ac780f; IPE_LandingTime=1720211779331; ipe.29665.pageViewedDay=187; forty_n_fbuid=d2c334de4995fd21cd548a0c585936e8acbbaefed63f4bf88ea719c86896d020; caconsentcookie={"version":"1.0","categories":{"general":true,"functional":true,"targeting":true,"statistics":true},"updatedAt":"2024-07-05T20:36:32.086Z","expiresAt":"2025-07-05T20:36:32.086Z","consentMethod":"OPT_IN","hasInteractedWithBanner":true,"limitSensitivePersonalData":null}; abc=AylXYegYClGjmNKfQNiMs0vt; pxa_ipv4=197.133.224.234; _gcl_au=1.1.882428833.1720211793; _fbp=fb.1.1720211792871.90196335991574363; uptracs_utm_campaign=; uptracs_utm_medium=; uptracs_utm_source=; uptracs_send_to_ga=0; re-evaluation=true; pxa_id=40CxZi4bV6shk2em1HXoqeiP; abc_3rd_party=AylXYegYClGjmNKfQNiMs0vt; pixall_cookie_sync=true; pxa_at=true; ddc_abcg_cache=CAESEOY_FqNyaRRTerxkdeM1zkE; ddc_abc_cache=AylXYegYClGjmNKfQNiMs0vt; ddc_diag_akam_currentTime=1720213041; ddc_diag_akam_requestID=8ecd24c; ddc_diag_akam_ghostIP=23.33.143.187; ddc_diag_akam_fullPath=/akam-sw-policy.json; ipe.29665.pageViewedCount=5; ipe_29665_fov=%7B%22numberOfVisits%22%3A1%2C%22sessionId%22%3A%22fdae60ab-fd7a-daed-ce4a-359182ac780f%22%2C%22expiry%22%3A%222024-08-04T20%3A36%3A19.336Z%22%2C%22lastVisit%22%3A%222024-07-05T20%3A57%3A34.117Z%22%7D; _ga_YYYYYYYYYY=GS1.1.1720211777.1.0.1720213066.0.0.0; aeatstartmessage=true; lastItemViewed=%7B%22eventTimestamp%22%3A1720213090883%2C%22dealerCode%22%3Anull%2C%22vehicleType%22%3A%22new%22%2C%22make%22%3A%22Jeep%22%2C%22model%22%3A%22Grand+Cherokee%22%2C%22bodyStyle%22%3A%22SUV%22%2C%22vin%22%3Anull%2C%22vehicleId%22%3A%221d6912540a0e0a902a280e521a3f5bd3%22%2C%22stockNumber%22%3Anull%2C%22year%22%3A2023%2C%22price%22%3A54690%2C%22pageType%22%3Anull%2C%22listingType%22%3Anull%2C%22listingDomain%22%3Anull%2C%22listingCode%22%3Anull%2C%22mpgCity%22%3A19%2C%22mpgHighway%22%3A26%2C%22odometer%22%3A26%7D; akaalb_pixall_prod=1720214892~op=ddc_ana_pixall_prod:eng_ana_pixall_prod-pico-us-east-1|~rv=94~m=eng_ana_pixall_prod-pico-us-east-1:0|~os=6aafa3aac97a52a58cd06655a170720e~id=434c87dd8dd9381d45cd97462be94d22; _ga_XXXXXXX=GS1.1.1720211771.1.1.1720213093.0.0.0; _ga_L0S371KWFW=GS1.1.1720211771.1.1.1720213094.0.0.0; _ga_6MZMCE2125=GS1.1.1720211771.1.1.1720213095.0.0.0; _ga_FY1PWF1K1F=GS1.2.1720211771.1.1.1720213097.0.0.0; _ga_FTX8ZLHYYT=GS1.2.1720211793.1.1.1720213097.0.0.0; _uetsid=cc76bfb03b0e11efaf1eff1af497c71d; _uetvid=cc7721d03b0e11efa1a253ac089c453a; bm_sv=4F5B0C00984575DB16DF5D25CE27E8B1~YAAQt48hF3HBLn6QAQAAus+whBgoMEUHzxbhPWcWlnl1V4PsMxhq0qngPlMuMUP2T/jLIz8hewwy2L2e6Lct5RQGC4EsCQzfRwsBMT9T9CS1sluecnb4JM7KStiFa4wUATb2mwbC+7q6y5NU1ajKKYLdrF1Q07HK9/Ct6l5gGNjRu278efUNv8pMQz4MiFf38qPRI5/WoqgDsYjFD0i7epq0HQXJASu3j2LybfTg5GlBYcTWkc72rsH5R40GcmrXQA==~1; _ga_3Q85YSXWE9=GS1.2.1720211772.1.1.1720213099.0.0.0; _ga_5ECK8W73XE=GS1.1.1720211799.1.1.1720213102.0.0.0; AMP_16a5c84b5b=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjIxMjcyZjMyNS1jZTM5LTRmZDgtYWFkMy0zZGNlODRhZTUzODElMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzIwMjExNzczMTY4JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcyMDIxMzEwNjYwNyU3RA==; _ga_NHVS2FM866=GS1.1.1720211771.1.1.1720213108.60.0.1668047584; _ga_ZNWYLLMGKJ=GS1.1.1720211771.1.1.1720213108.60.0.915057410; _ga_7XSR3ST7D2=GS1.1.1720211771.1.1.1720213108.60.0.1802005590; _ga_SJP76C452Z=GS1.1.1720211771.1.1.1720213108.60.0.2007513024; _ga_TRPWMEP5QY=GS1.1.1720211771.1.1.1720213108.60.0.1803814618; _ga_E0H3P7B86E=GS1.1.1720211771.1.1.1720213108.0.0.0; _ga_SB4SCXY874=GS1.1.1720211794.1.1.1720213108.0.0.0; _ga_XMRK861STD=GS1.1.1720211794.1.1.1720213108.0.0.0; _ga_QL0WV279GL=GS1.1.1720211773.1.1.1720213108.0.0.0; _ga_4BZJKD1FGT=GS1.1.1720211773.1.1.1720213108.58.0.0; forty_n_user=v2D8JChR2AvReXZzSnpTcGp0Q0ZrUU9DQ3Ayd0NyUXhEVGFWazFTTHpUYUtYQ0wrcEpxZz0~; forty_n_t=1.8d2431.1720211774.1.7.1720211774.1720213109.4.0; _td=8c33d3c9-8f94-4847-bcd2-5f53f5154b03; s_sq=fcanaftafca.dealers.usa%252Cfcaentrp.globalreportsuite%3D%2526c.%2526a.%2526activitymap.%2526page%253Ddealer%25253Aus%25253Asearch-inventory%25253Aother-inventory%2526link%253D2%2526region%253Dinventory-paging1-app-root%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Ddealer%25253Aus%25253Asearch-inventory%25253Aother-inventory%2526pidt%253D1%2526oid%253Dhttps%25253A%25252F%25252Fwww.lahtis.net%25252Fall-inventory%25252Findex.htm%25253Fstart%25253D18%2526ot%253DA; _ga=GA1.2.1971229608.1720211771; _gat_UA-9899509-3=1; cgpd=%7B%22es%22%3A%5B%22318-3%3Amind-flayer.podium.com%3A%22%2C%22318-3%3Amind-flayer.podium.com%3A%22%2C%22318-3%3Amind-flayer.podium.com%3A%22%2C%22318-3%3Awww.googleadservices.com%3A%22%2C%22318-3%3Awww.googleadservices.com%3A%22%2C%22318-3%3Awww.googleadservices.com%3A%22%2C%22318-3%3Amind-flayer.podium.com%3A%22%2C%22318-3%3Amind-flayer.podium.com%3A%22%2C%22318-3%3Awww.googleadservices.com%3A%22%2C%22311-0%3A%22%2C%22312%22%2C%22318-3%3Amind-flayer.podium.com%3A%22%2C%22318-3%3Awww.googleadservices.com%3A%22%2C%22318-3%3Awww.googleadservices.com%3A%22%2C%22318-3%3Amind-flayer.podium.com%3A%22%2C%22318-3%3Amind-flayer.podium.com%3A%22%2C%22318-3%3Awww.googleadservices.com%3A%22%2C%22318-3%3Awww.googleadservices.com%3A%22%2C%22318-3%3Amind-flayer.podium.com%3A%22%2C%22318-3%3Awww.googleadservices.com%3A%22%5D%7D; _ga_DRYFC644X2=GS1.1.1720211771.1.1.1720213110.0.0.0; _sda:stellantis:T3:session=25b6aa9c-cecb-492b-995f-1a6c961100ab%3AN%3A1720214880692%3A%3A3ekg5hp404ex0!a1ef904e9f311cb3e0663b93f055fa1c!2opprm2lxqnfu!%3A1720211775433%3AN%3A%3ASTELLANTIS%3ADEALERDOTCOM%3A23050%3AN%3A',
    #     'priority': 'u=1, i',
    #     'referer': 'https://www.lahtis.net/all-inventory/index.htm?start=18',
    #     'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    #     'sec-ch-ua-mobile': '?0',
    #     'sec-ch-ua-platform': '"Windows"',
    #     'sec-fetch-dest': 'empty',
    #     'sec-fetch-mode': 'no-cors',
    #     'sec-fetch-site': 'same-origin',
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    #     }

#     params = {
#         'start': '18',
#     }

# response = requests.get(
#     'https://www.lahtis.net/apis/widget/INVENTORY_LISTING_DEFAULT_AUTO_ALL:inventory-data-bus1/getInventory',
# )
    start_urls = ['https://www.lahtis.net/apis/widget/INVENTORY_LISTING_DEFAULT_AUTO_ALL:inventory-data-bus1/getInventory']

    def parse(self, response):
        # print(response.text)
        JSON = json.loads(response.text)
        TotalCars = JSON['pageInfo']['totalCount']
        for page in range(0,TotalCars,18):
            api_link = f'https://www.lahtis.net/apis/widget/INVENTORY_LISTING_DEFAULT_AUTO_ALL:inventory-data-bus1/getInventory?start={page}'
            yield scrapy.Request(api_link,callback=self.parse_data)
            print(api_link)
            # break

    def parse_data(self,response):
        JSON = json.loads(response.text)
        Cars = JSON['inventory']
        for car in Cars:
            item = LahtisItem()
            item['Name'] = ' '.join(car['title'])
            item["Year"] = car['year']
            item["Make"] = car['make']
            item["Model"] = car['model']
            item['Trim'] = car['trim']
            item['retailPrice'] = car['pricing']['retailPrice']
            item['finalPrice'] = car['pricing']['dPrice'][-1]['value']
            yield item

    # def parse_data(self, response):
    #     selector = pq(response.text)
    #     pages_item = response.meta['pages_item']
    #     item = AutodataItem()
    #     item2 = MetaItem()

    #     item["Scrapping_Date"] = datetime.today().strftime('%A, %B %d, %Y')
    #     item["Year"] = pages_item.get('car_year')
    #     item["Make"] = pages_item.get('car_make')
    #     item["model"] = selector('.fw-500 span:contains("Model")+a span').text()
    #     item["bodystyle"] = pages_item.get('body_type')
    #     item["colour_exterior"] = selector('.fw-500 span:contains("Color")+a span').text()
    #     item["colour_interior"] = selector('.fw-500 span:contains("Interior")+span').text()
    #     item["fuel_type"] = pages_item.get('fuel_type')
    #     item["mileage"] = pages_item.get('kilometers')
    #     item["regional_spec"] = pages_item.get('regional_specs')
    #     item["condition"] = pages_item.get('condition')
    #     item["warranty_untill_when"] = pages_item.get('warranty')
    #     item["Last_Code_Update_Date"] = datetime.today().strftime('%Y-%m-%d')
    #     item["Scrapping_Date"] = datetime.today().strftime('%Y-%m-%d')
    #     item["Country"] = "UAE"
    #     item["City"] = selector('.icon-location a span').text()
    #     #         #vat service contract and hp information extracted from the title
    #     title = selector('span.car-title').text()
    #     finder_eng = re.compile(r'\d\.\dL')  # scraping engine size using RE
    #     mo1 = finder_eng.search(title)
    #     if mo1 is None:
    #         pass
    #     else:
    #         item['engine_size'] = mo1.group().replace('L', '')
        
    #     finder_dr = re.compile(r'AWD|4WD')  # scraping drive type using RE
    #     mo2 = finder_dr.search(title)
    #     if mo2 is None:
    #         pass
    #     else:
    #         item['drive_type'] = mo2.group()

    #     if 'inclusive' in title.lower():
    #         item['vat'] = "Yes"
    #     else:
    #         item['vat'] = "No"

    #     if 'service' in title.lower():
    #         item['service_contract'] = 'Yes'
    #     else:
    #         item['service_contract'] = 'No'
    #     if 'hp' in title.lower():
    #         item['horse_power'] = title
    #     else:
    #         item['horse_power'] = ' '
    #     item["Seller_Name"] = pages_item.get('seller_name')
    #     item["Seller_Type"] = "Independent Dealer" if pages_item.get('seller_name') else ''
    #     item["Car_URL"] = response.url
    #     item['img'] = response.xpath('//ul[@class="slide-thumbnails"]/li/img/@src').getall()
    #     item['cylinders'] = selector('.fw-500 span:contains("Cylinders")+span').text()
    #     item2['src'] = "dubicars.com"
    #     item2['ts'] = datetime.utcnow().isoformat()
    #     item2['name'] = self.name
    #     item2['url'] = response.url
    #     item2['uid'] = str(uuid.uuid4())
    #     item2['cs'] = hashlib.md5(json.dumps(dict(item), sort_keys=True).encode('utf-8')).hexdigest()
    #     item['meta'] = dict(item2)
    #     item['Source'] = item2['src']
    #     item['Price_Currency'] = 'AED'
    #     try:
    #         price = ''.join(response.xpath('(//div[@class="price updated-price"])[1]/text()').extract()).split('AED')[1]
    #     except:
    #         price = ''
    #     if 'AED 0' in price:
    #         item['asking_price_ex_VAT'] = 'Price not available'
    #     elif '$' in price:
    #         item['asking_price_ex_VAT'] = 'Price not available'
    #     else:
    #         item["asking_price_ex_VAT"] = price
    #     item["Car_Name"] = title
    #     item['Spec'] = title
    #     yield item