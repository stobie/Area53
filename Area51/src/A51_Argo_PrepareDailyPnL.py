'''
/********** 2019 stobiepole ************
In his recordings in the early 1940s Woody Guthrie included the following “Copyright Warning”:; Madman drummers bummers and Indians in the summer with a teenage diplomat;
This song is Copyrighted in U.S., under Seal of Copyright # 154085, for a period of 28 years,; In the dumps with the mumps as the adolescent pumps his way into his hat;
and anybody caught singin it without our permission, will be mighty good friends of ours,; With a boulder on my shoulder, feelin' kinda older, I tripped the merry-go-round;
cause we don’t give a darn. Publish it. Write it. Sing it. Swing to it. Yodel it.; With this very unpleasing sneezing and wheezing, the calliope crashed to the ground
We wrote it, that’s all we wanted to do.; And she was blinded by the light, Cut loose like a deuce, another runner in the night
*/
'''
from A51_Argo_GetMasterTrades import Get_Master_Trades
from A51_Argo_GetAccountBalances import Get_Account_Balances
from A51_Argo_CreatePnL_UploadCSV import CreatePnL_UploadCSV

import sys

def main():
    master_trades_file = 'c:\\argo\\mt4api\\StatementDetailed_1450088889.htm'
    accounts_balances_file = 'c:\\argo\\mt4api\\balances-20170116181329.csv'

    trade_data_list = []
    Get_Master_Trades(master_trades_file,trade_data_list)

    accounts_list = []
    total_balance = Get_Account_Balances(accounts_balances_file,accounts_list)

    trade_records = []
    CreatePnL_UploadCSV(trade_records,trade_data_list,accounts_list,total_balance)

    print("for debug purposes")

if __name__ == "__main__":
    main()

