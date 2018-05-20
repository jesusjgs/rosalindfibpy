#This is a class with the method compute that given a number of months and sons per pair of rabbits, calculates how many
#will be when that time happens beggining on 1 pair.
class RabbitsCalculation:
    def Compute(self, months: int, sons_Per_Pair: int, earlier_Rabbits: int, before_Earlier_Rabbits) -> int:
        res= None
        if months>40 or months<0 or sons_Per_Pair>5 or sons_Per_Pair<0:
            raise Exception('Arguments are not the on the valid range')
        else:
            if months>1:
                res= self.Compute(self, months - 1, sons_Per_Pair, earlier_Rabbits + before_Earlier_Rabbits*sons_Per_Pair,earlier_Rabbits)
            else:
                res= earlier_Rabbits
            return res;

