class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        
        
        sorted_list = sorted(boxTypes, key=lambda x:-x[1])
        
        units = 0
        curr = 0
        for i in range(len(sorted_list)):
            
            arr = sorted_list[i]
            # unit = 0
            for j in range(arr[0]):
                curr += 1
                if curr > truckSize:
                    return units
                units += arr[1]
            # units += unit
            
        return units

  def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    count=0
    for box in boxTypes:
        rem=min(truckSize,box[0])
        count+=rem*box[1]
        truckSize-=rem
        if truckSize<=0:
            break
    return count

  def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:-x[1])
        ans=0
        while boxTypes:
            if boxTypes[0][0]<=truckSize:
                ans+=boxTypes[0][0]*boxTypes[0][1]
                truckSize-=boxTypes[0][0]
            else:
                ans+=truckSize*boxTypes[0][1]
                break
            boxTypes.pop(0)
        return ans

  def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
    
    # sort boxes from highest load to lowest load
    boxTypes = sorted(boxTypes, key=lambda x: x[-1], reverse=True)
    results = 0
    # iterate over boxes and total units
    for nbox, nunits in boxTypes:
        # keep a running track of box space used
        truckSize = truckSize - nbox
        # if we still have space keep loading
        if not truckSize < 0:
            results+= nbox * nunits
        else:
            # if we run out of space find residual box space left and load it
            results += (truckSize + nbox) * nunits
            # once we enter negative territory theres no more space in the truck, return
            return results
    
    return results

  def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key=lambda x: x[-1], reverse=True)
        count=0
        
        for box, units in boxTypes:
            truckSize -= box
            if truckSize >= 0:
                count += box * units
            else:
                count += (truckSize + box) * units
                
                return count
        return count