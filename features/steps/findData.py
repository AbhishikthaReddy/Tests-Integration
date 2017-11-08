

class find(object):
    def find(self,AccountID):
        number_types = (int,float, complex)

        if isinstance(AccountID, number_types):
            return AccountID
        else:
            raise ValueError