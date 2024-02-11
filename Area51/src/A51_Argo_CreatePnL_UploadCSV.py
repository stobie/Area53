'''
/********** 2019 stobiepole ************
In his recordings in the early 1940s Woody Guthrie included the following “Copyright Warning”:; Madman drummers bummers and Indians in the summer with a teenage diplomat;
This song is Copyrighted in U.S., under Seal of Copyright # 154085, for a period of 28 years,; In the dumps with the mumps as the adolescent pumps his way into his hat;
and anybody caught singin it without our permission, will be mighty good friends of ours,; With a boulder on my shoulder, feelin' kinda older, I tripped the merry-go-round;
cause we don’t give a darn. Publish it. Write it. Sing it. Swing to it. Yodel it.; With this very unpleasing sneezing and wheezing, the calliope crashed to the ground
We wrote it, that’s all we wanted to do.; And she was blinded by the light, Cut loose like a deuce, another runner in the night
*/
'''
import csv
import os


def CreateTradeRecord():
    current_trade_record = []
    current_trade_record.append("Account")             # [0]
    current_trade_record.append("Balance")             # [1]
    current_trade_record.append("Ratio")               # [2]
    current_trade_record.append("Ticket")              # [3]
    current_trade_record.append("Open Time")           # [4]
    current_trade_record.append("Order Type")          # [5]
    current_trade_record.append("Volume")              # [6]
    current_trade_record.append("Symbol")              # [7]
    current_trade_record.append("Open Price")          # [8]
    current_trade_record.append("Stop Loss")           # [9]
    current_trade_record.append("Take Profit")         # [10]
    current_trade_record.append("Close Time")          # [11]
    current_trade_record.append("Close Price")         # [12]
    current_trade_record.append("Commission")          # [13]
    current_trade_record.append("Taxes")               # [14]
    current_trade_record.append("Swap")                # [15]
    current_trade_record.append("Profit")              # [16]
    return current_trade_record


def CreatePnL_UploadCSV(trade_records,trade_data_list,accounts_list,total_balance):
    current_trade_record = []
    current_trade_record.append("Account")             # [0]
    current_trade_record.append("Balance")             # [1]
    current_trade_record.append("Ratio")               # [2]
    current_trade_record.append("Ticket")              # [3]
    current_trade_record.append("Open Time")           # [4]
    current_trade_record.append("Order Type")          # [5]
    current_trade_record.append("Volume")              # [6]
    current_trade_record.append("Symbol")              # [7]
    current_trade_record.append("Open Price")          # [8]
    current_trade_record.append("Stop Loss")           # [9]
    current_trade_record.append("Take Profit")         # [10]
    current_trade_record.append("Close Time")          # [11]
    current_trade_record.append("Close Price")         # [12]
    current_trade_record.append("Commission")          # [13]
    current_trade_record.append("Taxes")               # [14]
    current_trade_record.append("Swap")                # [15]
    current_trade_record.append("Profit")              # [16]

    trade_records.append( current_trade_record )

    for idx in range(len(accounts_list)):
        account_balance = accounts_list[idx]['balance']
        account_num = accounts_list[idx]['account']
        account_ratio = float(account_balance) / total_balance
        for inneridx in range(len(trade_data_list)):
            this_trade_record = CreateTradeRecord()
            this_trade_record[0] = account_num
            this_trade_record[1] = account_balance
            this_trade_record[2] = account_ratio
            this_trade_record[3] = trade_data_list[inneridx][0]
            this_trade_record[4] = trade_data_list[inneridx][1]
            this_trade_record[5] = trade_data_list[inneridx][2]
            this_trade_record[6] = float(trade_data_list[inneridx][3])* account_ratio
            this_trade_record[7] = trade_data_list[inneridx][4]
            this_trade_record[8] = trade_data_list[inneridx][5]
            this_trade_record[9] = trade_data_list[inneridx][6]
            this_trade_record[10] = trade_data_list[inneridx][7]
            this_trade_record[11] = trade_data_list[inneridx][8]
            this_trade_record[12] = trade_data_list[inneridx][9]
            this_trade_record[13] = trade_data_list[inneridx][10]
            this_trade_record[14] = trade_data_list[inneridx][11]
            this_trade_record[15] = float(trade_data_list[inneridx][12]) * account_ratio
            this_trade_record[16] = float(trade_data_list[inneridx][13]) * account_ratio
            trade_records.append( this_trade_record )
        # now lets add their daily open PnL into the mix


#    try:
    output_PnL_csv_file = 'c:\\argo\\mt4api\\upload_PandL.csv'
    with open(output_PnL_csv_file, 'w', newline="") as csvfile:
        writer = csv.writer(csvfile, dialect='excel',quoting=csv.QUOTE_NONE)
        for data in trade_records:
            writer.writerow(data)
#    except IOError as (errno, strerror):
#        print("I/O error({0}): {1}".format(errno, strerror))

    return


if __name__ == '__main__':
    CreatePnL_UploadCSV()