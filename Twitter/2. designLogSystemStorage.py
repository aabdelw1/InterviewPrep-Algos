'''
You are given several logs, where each log contains a unique ID and timestamp. 
Timestamp is a string that has the following format: Year:Month:Day:Hour:Minute:Second, for example, 2017:01:01:23:59:59. All domains are zero-padded decimal numbers.

Implement the LogSystem class:

LogSystem() Initializes the LogSystem object.
void put(int id, string timestamp) Stores the given log (id, timestamp) in your storage system.
int[] retrieve(string start, string end, string granularity) Returns the IDs of the logs whose timestamps are within the range from start to end inclusive. 
start and end all have the same format as timestamp, and granularity means how precise the range should be (i.e. to the exact Day, Minute, etc.). 
For example, start = "2017:01:01:23:59:59", end = "2017:01:02:23:59:59", and granularity = "Day" means that we need to find the logs within the inclusive range from Jan. 
1st 2017 to Jan. 2nd 2017, and the Hour, Minute, and Second for each log entry can be ignored.

'''

class LogSystem:
  def __init__(self):
      self.log = {}
      
  def put(self, id: int, timestamp: str) -> None:
      self.log[id] = timestamp

  def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
      res = []
      gran = {
          "Year": 4,
          "Month": 7,
          "Day": 10,
          "Hour": 13,
          "Minute": 16,
          "Second": 19
      }
      g = gran[granularity]
      
      for key, value in self.log.items():
          if start[:g] <= value[:g] <= end[:g]:
              res.append(key)
              
      return res
        
        
        


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)