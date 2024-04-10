class TuringMachine:
    def __init__(self, tape, states, transition_function, initial_state, final_states):
        self.tape = tape
        self.head_position = 0
        self.states = states
        self.transition_function = transition_function
        self.current_state = initial_state
        self.final_states = final_states

    def move_left(self):
        if self.head_position > 0:
            self.head_position -= 1

    def move_right(self):
        self.head_position += 1
        if self.head_position == len(self.tape):
            self.tape += ' '

    def write(self, symbol):
        self.tape = self.tape[:self.head_position] + symbol + self.tape[self.head_position+1:]

    def read(self):
        return self.tape[self.head_position]

    def run(self):
        while self.current_state not in self.final_states:
            print(self.tape)
            for i in range(self.head_position):
                print(" ", end="")
            print("^")
            current_symbol = self.read()
            if current_symbol == ' ':
                current_symbol = '0'
            if (self.current_state, current_symbol) not in self.transition_function:
                print("Transição não definida para estado:", self.current_state, "e símbolo:", current_symbol)
                return
            new_state, write_symbol, move_direction = self.transition_function[(self.current_state, current_symbol)]
            print(self.transition_function[(self.current_state, current_symbol)])
            print("head position: " + str(self.head_position))
            self.current_state = new_state
            self.write(write_symbol)
            if move_direction == 'L':
                self.move_left()
            elif move_direction == 'R':
                self.move_right()
            print("tape: " + self.tape)
            print("state: " + self.current_state)
            print("-----------------------------------------------------")
        print("Resultado:", self.tape)

if __name__ == "__main__":
    input_tape = "0110111"
    multiplication_transition_function = {
        ('001', '0'): ('001', '0', 'R'),
        ('001', '1'): ('002', '0', 'R'),
        ('002', '0'): ('003', '0', 'R'),
        ('002', '1'): ('002', '1', 'R'),
        ('003', '0'): ('001', '0', 'R'),
        ('003', '1'): ('004', '0', 'R'),
        ('004', '1'): ('004', '1', 'R'),
        ('004', '0'): ('005', '0', 'R'),
        ('005', '0'): ('006', '1', 'L'),
        ('005', '1'): ('005', '1', 'R'),
        ('006', '0'): ('007', '0', 'L'),
        ('006', '1'): ('006', '1', 'L'),
        ('007', '0'): ('009', '1', 'L'),
        ('007', '1'): ('008', '1', 'L'),
        ('008', '0'): ('003', '1', 'R'),
        ('008', '1'): ('008', '1', 'L'),
        ('009', '0'): ('010', '0', 'L'),
        ('013', '0'): ('013', '0', 'R'),
        ('009', '1'): ('009', '1', 'L'),
        ('010', '0'): ('012', '0', 'L'),
        ('010', '1'): ('011', '1', 'L'),
        ('011', '0'): ('001', '1', 'R'),
        ('011', '1'): ('011', '1', 'L'),
        ('012', '0'): ('013', '0', 'L'),
        ('012', '1'): ('012', '0', 'L'),
        ('013', '1'): ('014', '0', 'R'),
        ('014', '0'): ('015', '0', 'R'),
        ('014', '1'): ('014', '0', 'R'),
        ('015', '0'): ('016', '0', 'R'),
        ('015', '1'): ('015', '1', 'R'),
        ('016', '0'): ('000', '0', 'L'),
        ('016', '1'): ('000', '0', 'R')
    }
    input_tape = "01101110"
    states = {'001', '002', '003', '004', '005', 
            '006', '007', '008', '009', '010', 
            '011', '012', '013', '014', '015', 
            '016', '000'}
    final_states = {'000'}
    tm = TuringMachine(input_tape, states, multiplication_transition_function, '001', final_states)
    tm.run()
