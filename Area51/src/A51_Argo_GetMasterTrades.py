'''
/********** 2019 stobiepole ************
In his recordings in the early 1940s Woody Guthrie included the following “Copyright Warning”:; Madman drummers bummers and Indians in the summer with a teenage diplomat;
This song is Copyrighted in U.S., under Seal of Copyright # 154085, for a period of 28 years,; In the dumps with the mumps as the adolescent pumps his way into his hat;
and anybody caught singin it without our permission, will be mighty good friends of ours,; With a boulder on my shoulder, feelin' kinda older, I tripped the merry-go-round;
cause we don’t give a darn. Publish it. Write it. Sing it. Swing to it. Yodel it.; With this very unpleasing sneezing and wheezing, the calliope crashed to the ground
We wrote it, that’s all we wanted to do.; And she was blinded by the light, Cut loose like a deuce, another runner in the night
*/
'''
statement_file = 'c:\\argo\\mt4api\\StatementDetailed_1450088889.htm'

def Get_Master_Trades(master_statement,trade_data_list):


    index_feq = 0
    start_of_closed_trades = 40

    with open(master_statement) as f:
        todays_trades_html = f.readlines()

    this_line = 0
    for index in todays_trades_html:
        this_line += 1
        if this_line > start_of_closed_trades :
            if this_line % 2 == 0:
                current_trade = index.split('</td>', -1)
                if current_trade[0] == '\n':
                    break
                current_trade_values = []
                for c1 in range(len(current_trade)):
                    local_rval = current_trade[c1][(current_trade[c1].rfind('>') + 1):len(current_trade[c1])]
                    if c1 == 13:
                        local_rval = ''.join(local_rval.split())
                    current_trade_values.append(local_rval)
                trade_data_list.append(current_trade_values)

    looper1 = 0
    floating_value_next = False
    for index in todays_trades_html:
        looper1 += 1
        if looper1 > this_line :
            if floating_value_next:
                find_floating_equity = index.split('</b>', -1)
                local_rval = find_floating_equity[index_feq][(find_floating_equity[index_feq].rfind('>') + 1):len(find_floating_equity[index_feq])]
                open_PnL = ''.join(local_rval.split())
                break
            if "Floating" in index:
                floating_value_next = True


    print( len(todays_trades_html) )

if __name__ == '__main__':
    Get_Master_Trades('c:\\argo\\mt4api\\StatementDetailed_1450088889.htm')
