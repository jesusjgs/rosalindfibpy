# This is a class with the method compute that given a number of months and sons per pair of rabbits, calculates how
# many will be when that time happens beggining on 1 pair.


class RabbitsCalculation:
    @classmethod
    def compute(self, months: int, sons_per_pair: int, earlier_rabbits: int, before_earlier_rabbits) -> int:
        if months > 40 or months < 0 or sons_per_pair > 5 or sons_per_pair < 0:
            raise Exception('Arguments are not the on the valid range')
        else:
            if months > 1:
                new_months = months - 1
                updated_early_rabb = earlier_rabbits + before_earlier_rabbits * sons_per_pair
                res = RabbitsCalculation.compute(self, new_months, sons_per_pair, updated_early_rabb, earlier_rabbits)
            else:
                res = earlier_rabbits
            return res

