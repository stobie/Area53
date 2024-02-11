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
filename = 'c:\\argo\\mt4api\\balances-2017test.csv'

def Get_Account_Balances(balances_file, accounts_list):

    input_file = csv.DictReader(open(balances_file))

    for line in input_file:
        accounts_list.append(line)

    total_balance = 0.0
    for i, balance in enumerate(d['balance'] for d in accounts_list):
        total_balance += float(balance)

    return total_balance


if __name__ == '__main__':
    Get_Account_Balances('c:\\argo\\mt4api\\balances-2017test.csv')