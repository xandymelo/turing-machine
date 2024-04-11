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
            print(self.current_state, current_symbol, "=>", end="")
            new_state, write_symbol, move_direction = self.transition_function[(self.current_state, current_symbol)]
            print(new_state, write_symbol, move_direction)
            print("head position: " + str(self.head_position))
            self.current_state = new_state
            self.write(write_symbol)
            if move_direction == 'L':
                self.move_left()
            elif move_direction == 'R':
                self.move_right()
            print("-----------------------------------------------------")
        print("Resultado:", self.tape)


def multiplication_unario(input_tape="0110111"):
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

def convert_unario_plus_one_to_unario(input_tape="011101111"):
    turing_transition_function = {
        ('E1', '0'): ('E2', '0', 'R'),
        ('E2', '1'): ('E2', '1', 'R'),
        ('E2', '0'): ('E3', '0', 'L'),
        ('E3', '1'): ('E4', '0', 'R'),
        ('E4', '0'): ('E5', '1', 'R'),
        ('E5', '1'): ('E5', '1', 'R'),
        ('E5', '0'): ('E6', '0', 'L'),
        ('E6', '1'): ('E7', '0', 'L'),
        ('E7', '1'): ('E8', '0', 'L'),
        ('E8', '1'): ('E9', '1', 'L'),
        ('E9', '1'): ('E9', '1', 'L'),
        ('E9', '0'): ('E10', '0', 'L'),
        ('E10', '1'): ('E10', '1', 'L'),
        ('E10', '0'): ('E11', '0', 'L'),
        ('E11', '0'): ('E11', '0', 'R'),
        ('E11', '1'): ('E12', '0', 'R'),
        ('E12', '0'): ('E13', '0', 'R'),
        ('E12', '1'): ('E12', '1', 'R'),
        ('E13', '0'): ('E11', '0', 'R'),
        ('E13', '1'): ('E14', '0', 'R'),
        ('E14', '1'): ('E14', '1', 'R'),
        ('E14', '0'): ('E15', '0', 'R'),
        ('E15', '0'): ('E16', '1', 'L'),
        ('E15', '1'): ('E15', '1', 'R'),
        ('E16', '0'): ('E17', '0', 'L'),
        ('E16', '1'): ('E16', '1', 'L'),
        ('E17', '0'): ('E19', '1', 'L'),
        ('E17', '1'): ('E18', '1', 'L'),
        ('E18', '0'): ('E13', '1', 'R'),
        ('E18', '1'): ('E18', '1', 'L'),
        ('E19', '0'): ('E20', '0', 'L'),
        ('E23', '0'): ('E23', '0', 'R'),
        ('E19', '1'): ('E19', '1', 'L'),
        ('E20', '0'): ('E22', '0', 'L'),
        ('E20', '1'): ('E21', '1', 'L'),
        ('E21', '0'): ('E11', '1', 'R'),
        ('E21', '1'): ('E21', '1', 'L'),
        ('E22', '0'): ('E23', '0', 'L'),
        ('E22', '1'): ('E22', '0', 'L'),
        ('E23', '1'): ('E24', '0', 'R'),
        ('E24', '0'): ('E25', '0', 'R'),
        ('E24', '1'): ('E24', '0', 'R'),
        ('E25', '0'): ('E26', '0', 'R'),
        ('E25', '1'): ('E25', '1', 'R'),
        ('E26', '0'): ('E27', '0', 'L'),
        ('E26', '1'): ('E27', '1', 'R'),
        ('E27', '0'):('E27', '0', 'L'),
        ('E27', '1'):('E28', '1', 'R'),
        ('E28', '1'):('E28', '1', 'R'),
        ('E28', '0'): ('E0', '1', 'R'),
        
    }
    final_states = {'E0'}
    states = {'E0', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10',
          'E11', 'E12', 'E13', 'E14', 'E15', 'E16', 'E17', 'E18', 'E19', 'E20',
          'E21', 'E22', 'E23', 'E24', 'E25', 'E26', 'E27', 'E28'}
    tm = TuringMachine(input_tape, states, turing_transition_function, 'E1', final_states)
    tm.run()

if __name__ == "__main__":
    convert_unario_plus_one_to_unario()
    
