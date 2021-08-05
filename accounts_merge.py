#https://leetcode.com/problems/accounts-merge/

class Solution:
    
    def check_if_exists(self, account):
        for index, acc in enumerate(self.combined_accounts):
            acc_name = list(acc.keys())[0]
            if acc_name == account:
                return index
        return None

    def check_overlap(self, index, accounts):
        existing_accs = list(self.combined_accounts[index].values())
        for acc in accounts:
            if acc in existing_accs[0]:
                existing_accs[0].extend(accounts)
                return list(set(existing_accs[0]))
        return None

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.combined_accounts = []
        for account in accounts:
            account_index = self.check_if_exists(account[0])
            if account_index is not None:
                # check for possible overlap
                new_accounts = self.check_overlap(account_index, account[1:])
                if new_accounts is not None:
                    new_accounts.sort()
                    self.combined_accounts[account_index][account[0]] = new_accounts
                else:
                    self.combined_accounts.append({account[0]: account[1:]})
            else:
                self.combined_accounts.append({account[0]: account[1:]})
        final_list = []
        for acc in self.combined_accounts:
              for name,accounts in acc.items():
                    accounts.insert(0, name)
                    final_list.append(accounts)
        return final_list
