from decimal import Decimal
import yfinance as yf
import pandas
import csv
import xml.etree.ElementTree as xml
from xml.dom.minidom import parseString
from threading import *
from enum import Enum

class variables:
    elaborate_ticker_thread1: list[str] = []
    elaborate_ticker_thread2: list[str] = []
    elaborate_ticker_thread3: list[str] = []
    elaborate_ticker_thread4: list[str] = []
    elaborate_ticker_thread5: list[str] = []
    elaborate_ticker_thread6: list[str] = []
    elaborate_ticker_thread7: list[str] = []
    elaborate_ticker_thread8: list[str] = []
    elaborate_ticker_thread9: list[str] = []
    elaborate_ticker_thread10: list[str] = []
    elaborate_ticker_thread11: list[str] = []
    elaborate_ticker_thread12: list[str] = []
    elaborate_ticker_thread13: list[str] = []
    elaborate_ticker_thread14: list[str] = []
    elaborate_ticker_thread15: list[str] = []
    elaborate_ticker_thread16: list[str] = []
    elaborate_ticker_thread17: list[str] = []
    elaborate_ticker_thread18: list[str] = []
    elaborate_ticker_thread19: list[str] = []
    elaborate_ticker_thread20: list[str] = []

    list_thread1: list[dict] = []
    list_thread2: list[dict] = []
    list_thread3: list[dict] = []
    list_thread4: list[dict] = []
    list_thread5: list[dict] = []
    list_thread6: list[dict] = []
    list_thread7: list[dict] = []
    list_thread8: list[dict] = []
    list_thread9: list[dict] = []
    list_thread10: list[dict] = []
    list_thread11: list[dict] = []
    list_thread12: list[dict] = []
    list_thread13: list[dict] = []
    list_thread14: list[dict] = []
    list_thread15: list[dict] = []
    list_thread16: list[dict] = []
    list_thread17: list[dict] = []
    list_thread18: list[dict] = []
    list_thread19: list[dict] = []
    list_thread20: list[dict] = []

class data_types(Enum):
        id = 0
        industry = 1
        longBusinessSummary = 2
        previousClose = 3
        open = 4
        dayLow = 5
        dayHigh = 6
        dividendRate = 7
        dividendYield = 8
        marketCap = 9
        sharesOutstanding = 10
        exchange = 11
        symbol = 12
        shortName = 13
        currentPrice = 14
        recommendationMean = 15
        recommendationKey = 16
        financialCurrency = 17
        percentChange = 18
        
class message_types(Enum):
        info = 0
        warning = 1
        error = 2

class finance():
    def test():
        df = pandas.DataFrame([158.82, 158,44])
        print(df.pct_change())

    def get_all_stock_symbols() -> list[str]:
        result: list[str] = []
        csv_file = csv.reader(open("nasdaq_screener.csv"), delimiter=",")
        lines_counter: int = 0
        for line in csv_file:
            if lines_counter > 0:
                result.append(str(line[0]))
            lines_counter += 1
        return result

    def get_single_company_data(ticker: str) -> dict | None:
        include_only: list[str] = ["industry",
                                   "longBusinessSummary",
                                   "previousClose",
                                   "open",
                                   "dayLow",
                                   "dayHigh",
                                   "dividendRate",
                                   "dividendYield",
                                   "marketCap",
                                   "sharesOutstanding",
                                   "exchange",
                                   "symbol",
                                   "shortName",
                                   "currentPrice",
                                   "recommendationMean",
                                   "recommendationKey",
                                   "financialCurrency"
                                   ]
        result: dict = {}
        try:
            company_info = yf.Ticker(ticker)
            for key, value in company_info.info.items():
                if key in include_only:
                    use_value: str = ""
                    if key == "marketCap" or key == "sharesOutstanding":
                        use_value = "0"
                    else:
                        use_value = value
                    result[key] = use_value
            result["percentChange"] = str((((int(result["currentPrice"]) - int(result["previousClose"])) / int(result["previousClose"])) * 100 ))
            for include in include_only:
                if include not in result.keys():
                    result[include] = ""
            return result
        except:
            return None

    def get_company_data_async(use_elaborate_list: list[str], use_list: list[dict]):
        for elab in use_elaborate_list:
            result: dict = finance.get_single_company_data(elab)
            use_list.append(result)

    def get_all_companies_data(tickers: list[str]) -> list[dict]:
        include_only: list[str] = ["industry",
                                   "longBusinessSummary",
                                   "previousClose",
                                   "open",
                                   "dayLow",
                                   "dayHigh",
                                   "dividendRate",
                                   "dividendYield",
                                   "marketCap",
                                   "sharesOutstanding",
                                   "exchange",
                                   "symbol",
                                   "shortName",
                                   "currentPrice",
                                   "recommendationMean",
                                   "recommendationKey",
                                   "financialCurrency"
                                   ]
        result: list[dict] = []
        for ticker in tickers:
            single_result: dict = {}
            try:
                t: str = ticker
                company_info = yf.Ticker(t)
                for key, value in company_info.info.items():
                    if key in include_only:
                        use_value: str = ""
                        if key == "marketCap" or key == "sharesOutstanding":
                            use_value = "0"
                        else:
                            use_value = value
                        single_result[key] = use_value
                single_result["percentChange"] = str(round((((int(single_result["currentPrice"]) - int(single_result["previousClose"])) / int(single_result["previousClose"])) * 100 ), 2))
                for include in include_only:
                    if include not in single_result.keys():
                        single_result[include] = ""
                result.append(single_result)
            except:
                continue
        return result

class xml_handler:
    def get_index() -> int:
        xml_doc = xml.parse("data_container.xml")
        root_node = xml_doc.getroot()
        return int(root_node.find(".//indexer").text)

    def set_index(newIndex: int):
        xml_doc = xml.parse("data_container.xml")
        root_node = xml_doc.getroot()
        root_node.find(".//indexer").text = str(newIndex)
        xml_doc.write("data_container.xml", encoding="utf-8", xml_declaration=True)

    def get_value(where_column: data_types) -> str:
        xml_doc = xml.parse("data_container.xml")
        root_node = xml_doc.getroot()

    def get_row(where_column: data_types) -> list[str]:
        xml_doc = xml.parse("data_container.xml")
        root_node = xml_doc.getroot()

    def insert_row(new_data: dict):
        if new_data != None:
            xml_doc = xml.parse("data_container.xml")
            root_node = xml_doc.getroot()
            data_node: xml.Element = root_node.find(".//data")
            id: str = str(xml_handler.get_index())
            id_node: xml.Element = xml.Element("id")
            id_node.set("index", id)
            for key, value in new_data.items():
                use_key: str = ""
                for c in str(key):
                    if c.isdigit() == False:
                        use_key += c
                child_node: xml.Element = xml.Element(use_key)
                child_node.text = str(value)
                id_node.append(child_node)
            data_node.append(id_node)
            xml.indent(xml_doc, space="\t", level=0)
            xml_doc.write("data_container.xml", encoding="utf-8", xml_declaration=True)
            xml_handler.set_index((xml_handler.get_index() + 1))

    def reset_file_content():
        open("data_container.xml", "w").close()
        xml_file = open("data_container.xml", "w+")
        xml_file.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n")
        xml_file.write("<container>\n")
        xml_file.write("<indexer>0</indexer>\n")
        xml_file.write("<data>\n")
        xml_file.write("</data>\n")
        xml_file.write("</container>")
        xml_file.close()
    
class multithread:
    def execute_thread(thread_index: int) -> Thread:
        use_elaborate_list: list[str] = []
        use_companies_data_list: list[dict]
        match thread_index:
            case 1:
                thread = Thread(target=finance.get_company_data_async, args=(variables.elaborate_ticker_thread1, variables.list_thread1))
                thread.start()
                return thread
            case 2:
                thread = Thread(target=finance.get_company_data_async, args=(variables.elaborate_ticker_thread2, variables.list_thread2))
                thread.start()
                return thread
            case 3:
                thread = Thread(target=finance.get_company_data_async, args=(variables.elaborate_ticker_thread3, variables.list_thread3))
                thread.start()
                return thread
            case 4:
                thread = Thread(target=finance.get_company_data_async, args=(variables.elaborate_ticker_thread4, variables.list_thread4))
                thread.start()
                return thread
            case 5:
                thread = Thread(target=finance.get_company_data_async, args=(variables.elaborate_ticker_thread5, variables.list_thread5))
                thread.start()
                return thread
            case 6:
                thread = Thread(target=finance.get_company_data_async, args=(variables.elaborate_ticker_thread6, variables.list_thread6))
                thread.start()
                return thread
            case 7:
                thread = Thread(target=finance.get_company_data_async, args=(variables.elaborate_ticker_thread7, variables.list_thread7))
                thread.start()
                return thread
            case 8:
                thread = Thread(target=finance.get_company_data_async, args=(variables.elaborate_ticker_thread8, variables.list_thread8))
                thread.start()
                return thread
            case 9:
                thread = Thread(target=finance.get_company_data_async, args=(variables.elaborate_ticker_thread9, variables.list_thread9))
                thread.start()
                return thread
            case 10:
                thread = Thread(target=finance.get_company_data_async, args=(variables.elaborate_ticker_thread10, variables.list_thread10))
                thread.start()
                return thread
            case 11:
                thread = Thread(target=finance.get_company_data_async, args=(variables.elaborate_ticker_thread11, variables.list_thread11))
                thread.start()
                return thread
            case 12:
                thread = Thread(target=finance.get_company_data_async, args=(variables.elaborate_ticker_thread12, variables.list_thread12))
                thread.start()
                return thread
            case 13:
                thread = Thread(target=finance.get_company_data_async, args=(variables.elaborate_ticker_thread13, variables.list_thread13))
                thread.start()
                return thread
            case 14:
                thread = Thread(target=finance.get_company_data_async, args=(variables.elaborate_ticker_thread14, variables.list_thread14))
                thread.start()
                return thread
            case 15:
                thread = Thread(target=finance.get_company_data_async, args=(variables.elaborate_ticker_thread15, variables.list_thread15))
                thread.start()
                return thread
            case 16:
                thread = Thread(target=finance.get_company_data_async, args=(variables.elaborate_ticker_thread16, variables.list_thread16))
                thread.start()
                return thread
            case 17:
                thread = Thread(target=finance.get_company_data_async, args=(variables.elaborate_ticker_thread17, variables.list_thread17))
                thread.start()
                return thread
            case 18:
                thread = Thread(target=finance.get_company_data_async, args=(variables.elaborate_ticker_thread18, variables.list_thread18))
                thread.start()
                return thread
            case 19:
                thread = Thread(target=finance.get_company_data_async, args=(variables.elaborate_ticker_thread19, variables.list_thread19))
                thread.start()
                return thread
            case 20:
                thread = Thread(target=finance.get_company_data_async, args=(variables.elaborate_ticker_thread20, variables.list_thread20))
                thread.start()
                return thread
 
class message_handler:
    def output_message(message, message_type: message_types):
        match message_type.value:
            case 0:
                print(f"<INFORMAZIONE>{message}</INFORMAZIONE>")
            case 1:
                print(f"<ATTENZIONE>{message}</ATTENZIONE>")
            case 2:
                print(f"<ERRORE>{message}</ERRORE>")