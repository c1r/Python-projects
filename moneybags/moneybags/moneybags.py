# --------------------------------------------
#   Name: Nidal Naseem
#   ID: 1635297
#   CMPUT 274, Fall 2020
#
#   Weekly Exercise 7: Moneybags
# --------------------------------------------


def applicants():
    '''Takes in the number of applicants and the net
       worth of each applicant to return a list of their
       net worth

       Arguments:
           None

       Returns:
           net_worth: The net worth of each applicant
    '''
    num = int(input())
    net_worth = []
    for i in range(num):
        net_worth.append(int(input()))
    return net_worth


def min_wealth(net_worth):
    '''Calculates the minimum wealth threshold for
       applicants to the club, 

       Arguments:
           net_worth: The net worth of each applicant

       Returns:
           wealth: the minimum wealth required to
                      be a member of the club
    '''
    net_worth = sorted(net_worth, reverse = True)
    j = 0
    wealth = 0
    while j != len(net_worth):
        if net_worth[j] >= j + 1:
            wealth = wealth + 1
        else:
            break
        j = j + 1
    return wealth

if __name__ == "__main__":
    print(min_wealth(applicants()))