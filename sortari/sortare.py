class Sorter():
    def _identitate(self,x):
        return x
    
    def _negatie(self,x):
        return not x
        
    def sort(self,list,key=lambda x:x,cmp=lambda x,y:x<y,reverse=False):
        pass

class InsertSort(Sorter):
    def sort(self, list, key=lambda x:x, cmp=lambda x, y:x < y, reverse=False):
        if reverse:
            operatie = self._negatie
        else:
            operatie = self._identitate
        self.__insert_sort(list,key,cmp,operatie)
        
    def __insert_sort(self,list,key,cmp,operatie):
        for i in range(1,len(list)):
            value = list[i]
            j = i-1
            while j >= 0 and operatie(cmp(key(value),key(list[j]))):
                list[j+1] = list[j]
                j -= 1
            list[j+1] = value

class CombSort(Sorter):
    def sort(self, list, key=lambda x:x, cmp=lambda x, y:x < y, reverse=False):
        if reverse:
            operatie = self._negatie
        else:
            operatie = self._identitate
        self.__comb_sort(list,key,cmp,operatie)
        
    def __comb_sort(self,list,key,cmp,operatie):
        gap = len(list)
        swap = False
        while swap or gap > 1:
            gap = int((gap*10)/13)
            if gap < 1:
                gap = 1
            swap = False
            for i in range(len(list)-gap):
                j = i + gap
                if operatie(cmp(key(list[j]),key(list[i]))):
                    list[i],list[j] = list[j],list[i]
                    swap = True
    """  
class Sortare(object):
    def insert_sort(self,list):
        for i in range(1,len(list)):
            value = list[i]
            j = i-1
            while j >= 0 and value > list[j]:
                list[j+1] = list[j]
                j -= 1
            list[j+1] = value
        return list

    def comb_sort(self, list):
        gap = len(list)
        swap = False
        while swap or gap > 1:
            gap = max(1,int(gap/1.25))
            swap = False
            for i in range(len(list)-gap):
                j = i + gap
                if list[i] >= list[j]:
                    list[i],list[j] = list[j],list[i]
                    swap = True
            
        return list
        """