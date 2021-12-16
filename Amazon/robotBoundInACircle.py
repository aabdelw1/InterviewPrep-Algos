class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = [0,0]
        facing = "N"
        for instruction in instructions:
            if instruction == "G":
                if facing == "N":
                    pos = [pos[0], pos[1] + 1]
                elif facing == "E":
                    pos = [pos[0] + 1, pos[1]]
                elif facing == "S":
                    pos = [pos[0], pos[1] - 1]
                else:
                    pos = [pos[0] - 1, pos[1]]
            else:
                if facing == "N":
                    facing = "W" if instruction == "L" else "E"
                elif facing == "E":
                    facing = "N" if instruction == "L" else "S"
                elif facing == "S":
                    facing = "E" if instruction == "L" else "W"
                else:
                    facing = "S" if instruction == "L" else "N"
        
        return facing != "N" or (pos[0] == 0 and pos[1] == 0)