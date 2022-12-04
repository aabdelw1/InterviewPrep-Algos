def reorderLogFiles(self, logs: List[str]) -> List[str]:
        logs = [ x.split(' ') for x in logs]  # split the logs to a list
        digitsLog = [ x for x in logs if x[1].isdigit()] # separate the digits logs
        letterLog = [ x for x in logs if not x[1].isdigit()] # filter the logs starting with letter
        
        # now this custom sort will take each letter logs and create a tuple of list starting with second
        # element of list and then adding the first element. Tuple are easier in python for sorting
        # since the first letter is identifier we are appending at the end in tuple so that the sorting happens
        # on identifier in case earlier letter list elements are same
        
        def customsort(log):
            return (log[1:],log[0])
        return [ ' '.join(x) for x in sorted(letterLog,key=customsort) + digitsLog]