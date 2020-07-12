from state import State


class FSM:
    def __init__(self, executor):
        self.executor = executor
        self.states = {}
        self.states.update(self.__createState(self.executor(0, 0)))
        
    def __createState(self, name):
        new_item = {}
        new_item[str(name)] = State(name, self.executor)
        return new_item

    def defineUnknownStates(self):
        new_states = {}
        for stateName in self.states.keys():
            ways = self.states[str(stateName)].getWays()
            for x in [0, 1]:
                for y in [0, 1]:
                    if ways[x][y][0] not in self.states.keys() and ways[x][y][0] not in new_states.keys():
                        new_states.update(self.__createState(ways[x][y][0]))
        self.states.update(new_states)
    
    def run(self):
        old_states_size = len(self.states)
        self.defineUnknownStates()
        new_states_size = len(self.states)
        while new_states_size > old_states_size:
            self.defineUnknownStates()
            old_states_size = new_states_size
            new_states_size = len(self.states)
        print("State: stateValue (x, y)->[next_state, value-to-print]")
        for string in self.formatize():
            print(string)

    def formatize(self):
        output = []
        for stateName in self.states.keys():
            output.append("State: " + str(stateName) + " " + ", ".join(str((x, y)) + "->" + str(self.states[stateName].getWays()[x][y]) for x in [0, 1] for y in [0, 1]))
        return output


    def getStates(self):
        return self.states
