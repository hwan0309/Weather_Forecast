from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import requests
import json
from xml.etree.ElementTree import parse
import xmltodict
import pandas as pd
import numpy as np
import os
import time
from datetime import datetime


url = 'http://apis.data.go.kr/1360000/AsosHourlyInfoService'

std_list = [90,93,95,98,99,100,101,102,104,105,106,108,112,114,115,119,121,127,129,130,131,133,135,136,137,138,140,143,146,152,155,156,159,162,165,168,169,170,172,174,177,184,185,188,189,192,201,202,203,211,212,216,217,221,226,232,235,236,238,239,243,244,245,247,248,251,252,253,254,255,257,258,259,260,261,262,263,264,266,268,271,272,273,276,277,278,279,281,283,284,285,288,289,294,295]

for std in std_list:
    df = pd.DataFrame()
    print(f'지점번호 {std} 시작 {datetime.now(). time() } ' )
    breaker = False
    for year in range(11, 21, 1):
        print(f'{year}년 시작', end = ',')
        if breaker == True:
            break
        page = 1

        while True:
            try:
                queryParams = '?' + urlencode({
                    quote_plus('ServiceKey') : 'G19S8d%2FEA%2BbTkez5dK80%2BMu2ik%2FJqffvezfEzGkfrBCI0R%2B%2FQYOpzg%2FVa%2FN%2BWOPL2BvNV%2FfoTubLGKipiIhBiw%3D%3D',
                    quote_plus('pageNo'): f'{page}',
                    quote_plus('numOfRows') : '880',
                    quote_plus('dataType') : 'XML',
                    quote_plus('dataCd') : 'ASOS',
                    quote_plus('dateCd'): 'HR',
                    quote_plus('startDt'): f'20{year}0101',
                    quote_plus('endDt'): f'20{year}1231',
                    quote_plus('startHh'):'00',
                    quote_plus('pagendHheNo'): '23',
                    quote_plus('stnIds'): f'{std}',
                })
                request = urllib.request.Request(url + unquote(queryParams) )
                response_body = urlopen(request, timeout=60).read()
                decode_data = response_body.decode('utf-8')

                xml_parse = xmltodict.parse(decode_data)
                xml_dict = json.loads(json.dumps(xml_parse) )
                result = xml_dict['response']['header']['resultMsg']
                if result == 'NO_DATA':
                    breaker = True
                    break
                dicts = xml_dict['reqonse']['body']['items']['item']
                df_temp = pd.DataFrame(columns =['날짜', '시간', '지점_번호', '지점명', '기온', '강수량', '풍속', '풍향', '습도', '증기압', '이슬점온도', '현지기압', '해면기압', '일조', '일사', '적설',
                                                 '3시간_신절설', '전운량', '중하층운량', '운형', '최저운고', '시정', '지면온도', '5cm_지중온도', '10cm_지중온도', '20cm_지중온도', '30cm_지중온도'])
                for i in range(len(dicts)):
                   df_temp.loc[i] = [dicts[i]['tm'][:10], dicts[i]['tm'][11:], dicts[i]['stnId'], dicts[i]['stnNm'], dicts[i]['ta'], dicts[i]['rn'], dicts[i]['ws'], dicts[i]['wd'], dicts[i]['hm'], dicts[i]['pv'], dicts[i]['td'], dicts[i]['pa'], dicts[i]['ps'], dicts[i]['ss'], dicts[i]['icsr'], dicts[i]['dsnw'], dicts[i]['hr3Fhsc'], dicts[i]['dc10Tca'], dicts[i]['dc10LmcsCa'], dicts[i]['clfmAbbrCd'], dicts[i]['lcsCh'], dicts[i]['vs'], dicts[i]['ts'], dicts[i]['m005Te'], dicts[i]['m01Te'], dicts[i]['m02Te'], dicts[i]['m03Te']]
                df = pd.concat([df, df_temp])
                print(f'{page}page 완료', end = ', ')
                page += 1
            except:
                print(f'{page}page 오류 다시 시작', end = ', ')
            if page == 11:
                break

            print()
            print(f'{year}완료 -- {datetime.now().time()}')

        if len(df.values) != 0:
            df.to_csv(f"./tmtm/{df['지점명'].unique()[0]}" + "_tm_fianl.csv", index=False)
            print(f'지점번호 {std} 완료 -- {datetime.now().time()}')
        else:
            print(f'지점번호 {std} NO DATA')


