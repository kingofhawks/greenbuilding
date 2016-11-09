# -*- coding: utf-8 -*-
from zeep import Client
from lxml import etree
import base64

from enterprise.models import Project

location_map = {'320000': '江苏省', '320204': '北塘区'}


def get_project(code='3202041503050102'):
    print 'code ', code
    # client = Client('http://218.90.162.110:8889/WxjzgcjczyPage/DataExchange.asmx?WSDL')
    client = Client('http://192.168.153.188:8889/WxjzgcjczyPage/DataExchange.asmx?WSDL')
    # result = client.service.ReadTBDataFromZx('TBProjectInfo', 'wxjsj', 'wxjsj123!@#', '2016-09-08', '2016-09-11')
    result = client.service.ReadTBDataFromZx2('TBProjectInfo', 'wxjsj', 'wxjsj123!@#', '2016-01-01', '2016-12-31', code)
    print result

    # data = base64.b64decode(result)
    # print data
    if result is None:
        return None
    root = etree.fromstring(result)
    print root
    rows = root.xpath('/dataTable/row')
    # print len(rows)
    for row in rows:
        # print row
        prj_name = row.xpath('PrjName')[0].text
        name = base64.b64decode(prj_name).decode('GBK')
        print name
        BuildCorpName = row.xpath('BuildCorpName')[0].text
        construct_company = base64.b64decode(BuildCorpName).decode('GBK')
        print construct_company
        AllInvest = row.xpath('AllInvest')[0].text
        cost = base64.b64decode(AllInvest).decode('GBK')
        print cost
        AllArea = row.xpath('AllArea')[0].text
        print AllArea
        area = 0
        if AllArea:
            area = base64.b64decode(AllArea).decode('GBK')
            print area
        BDate = row.xpath('BDate')[0].text
        start_date = base64.b64decode(BDate).decode('GBK')
        print start_date
        EDate = row.xpath('EDate')[0].text
        end_date = base64.b64decode(EDate).decode('GBK')
        print end_date
        CountyNum = row.xpath('CountyNum')[0].text
        address = base64.b64decode(CountyNum).decode('GBK')
        print address
        return Project(name=name, area=area, cost=cost, construct_company=construct_company,
                       start_date=start_date, end_date=end_date, location=location_map.get(address))


def get_sgtsc(code='3202821609210107'):
    print 'code ', code
    # client = Client('http://218.90.162.110:8889/WxjzgcjczyPage/DataExchange.asmx?WSDL')
    client = Client('http://218.90.162.110:8889/WxjzgcjczyPage/DataExchange.asmx?WSDL')
    # result = client.service.ReadTBDataFromZx('TBProjectInfo', 'wxjsj', 'wxjsj123!@#', '2016-09-08', '2016-09-11')
    result = client.service.Read_Sgtsc(code)
    print result

    # data = base64.b64decode(result)
    # print data
    if result is None:
        return None
    root = etree.fromstring(result)
    print root


if __name__ == '__main__':
    # http://www.cnblogs.com/lout/articles/4149591.html
    project = get_project()
    print project
    # get_project('200200')
    # get_sgtsc()