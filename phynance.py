from libs.utils import *
from threading import *
from datetime import *
from time import sleep
import sys

execution_seconds: int = 0

def main():
    event = Event()
    execution_thread: Thread = Thread(target=operations.execution_time, args=(event,))
    execution_thread.start()
    # ESEGUI DI SEGUITO IL CODICE PRINCIPALE
    application_arguments.handle_arguments()
    # FINE
    event.set()
    global execution_seconds
    print(f"Eseguito in {str(timedelta(seconds=execution_seconds))}")

class application_arguments:
    def handle_arguments():
        arguments: list[str] = sys.argv
        if len(arguments) <= 1:
            print("ERRORE 1: Inserire almeno un argomento al comando. Per ulteriori informazioni aggiungi --help o -h.")
        else:
            for index in range(len(arguments) - 1):
                if index == 0:
                    arguments.remove(arguments[index])
            for argument in arguments:
                if argument == "--help" or argument == "-h":
                    print("OPZIONE 1: --help o -h per visualizzare la lista corrente.")
                    print("OPZIONE 2: --all o -a per ottenere i dati di tutto il mercato e inserirli in data_container.xml.")
                    print("OPZIONE 3: --single \"[symbol]\" o -s \"[symbol]\" per ottenere i dati di una singola compagnia.")
                    break
                elif argument == "--all" or argument == "-a":
                    operations.fill_data_container()
                    break
                elif argument == "--single" or argument == "-s":
                    symbol: str = arguments[(arguments.index(argument) + 1)]
                    #codice qui
                    break
                    
class operations:
    def fill_data_container():
        result: list[str] = finance.get_all_stock_symbols()
        for i in range(len(result)):
            if i >= 0 and i <= 10:
                variables.elaborate_ticker_thread1.append(result[i])
            elif i >= 11 and i <= 21:
                variables.elaborate_ticker_thread2.append(result[i])
            elif i >= 22 and i <= 32:
                variables.elaborate_ticker_thread3.append(result[i])
            elif i >= 33 and i <= 43:
                variables.elaborate_ticker_thread4.append(result[i])
            elif i >= 44 and i <= 54:
                variables.elaborate_ticker_thread5.append(result[i])
            elif i >= 55 and i <= 65:
                variables.elaborate_ticker_thread6.append(result[i])
            elif i >= 66 and i <= 76:
                variables.elaborate_ticker_thread7.append(result[i])
            elif i >= 77 and i <= 87:
                variables.elaborate_ticker_thread8.append(result[i])
            elif i >= 88 and i <= 98:
                variables.elaborate_ticker_thread9.append(result[i])
            elif i >= 99 and i <= 109:
                variables.elaborate_ticker_thread10.append(result[i])
            elif i >= 110 and i <= 120:
                variables.elaborate_ticker_thread11.append(result[i])
            elif i >= 121 and i <= 131:
                variables.elaborate_ticker_thread12.append(result[i])
            elif i >= 132 and i <= 142:
                variables.elaborate_ticker_thread13.append(result[i])
            elif i >= 143 and i <= 153:
                variables.elaborate_ticker_thread14.append(result[i])
            elif i >= 154 and i <= 164:
                variables.elaborate_ticker_thread15.append(result[i])
            elif i >= 165 and i <= 175:
                variables.elaborate_ticker_thread16.append(result[i])
            elif i >= 176 and i <= 186:
                variables.elaborate_ticker_thread17.append(result[i])
            elif i >= 187 and i <= 197:
                variables.elaborate_ticker_thread18.append(result[i])
            elif i >= 198 and i <= 208:
                variables.elaborate_ticker_thread19.append(result[i])
            elif i >= 209 and i <= 219:
                variables.elaborate_ticker_thread20.append(result[i])
        thread1 = multithread.execute_thread(1)
        thread2 = multithread.execute_thread(2)
        thread3 = multithread.execute_thread(3)
        thread4 = multithread.execute_thread(4)
        thread5 = multithread.execute_thread(5)
        thread6 = multithread.execute_thread(6)
        thread7 = multithread.execute_thread(7)
        thread8 = multithread.execute_thread(8)
        thread9 = multithread.execute_thread(9)
        thread10 = multithread.execute_thread(10)
        thread11 = multithread.execute_thread(11)
        thread12 = multithread.execute_thread(12)
        thread13 = multithread.execute_thread(13)
        thread14 = multithread.execute_thread(14)
        thread15 = multithread.execute_thread(15)
        thread16 = multithread.execute_thread(16)
        thread17 = multithread.execute_thread(17)
        thread18 = multithread.execute_thread(18)
        thread19 = multithread.execute_thread(19)
        thread20 = multithread.execute_thread(20)    
        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()
        thread5.join()
        thread6.join()
        thread7.join()
        thread8.join()
        thread9.join()
        thread10.join()
        thread11.join()
        thread12.join()
        thread13.join()
        thread14.join()
        thread15.join()
        thread16.join()
        thread17.join()
        thread18.join()
        thread19.join()
        thread20.join() 
        master_results: list[dict] = variables.list_thread1 + variables.list_thread2 + variables.list_thread3 + variables.list_thread4 + variables.list_thread5 + variables.list_thread6 + variables.list_thread7 + variables.list_thread8 + variables.list_thread9 + variables.list_thread10 + variables.list_thread11 + variables.list_thread12 + variables.list_thread13 + variables.list_thread14 + variables.list_thread15 + variables.list_thread16 + variables.list_thread17 + variables.list_thread18 + variables.list_thread19 + variables.list_thread20
        xml_handler.reset_file_content()
        for master_result in master_results:
            xml_handler.insert_row(master_result)

    def execution_time(event: Event) -> None:
        while (event.is_set() == False):
            sleep(1)
            global execution_seconds
            execution_seconds += 1
            
if __name__ == '__main__':
    main()