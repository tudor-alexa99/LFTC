from FA import *

if __name__ == '__main__':
    fa = FA()

    fa.reader("inputs\FA_input")

    option = int(input("Input:\n  0 -> exit \n 1 -> Initial state \n 2 -> States\n 3 -> Alphabet\n 4 -> Final "
                       "States\n 5 -> Transitions\n 6 -> Check sequence\n :"))
    while option != 0:
        if option == 1:
            print(fa.get_initial_state())

        if option == 2:
            print(fa.get_states())

        elif option == 3:
            print(fa.get_alphabet())

        elif option == 4:
            print(fa.get_final_states())

        elif option == 5:
            transitions = fa.get_transitions()
            for t in transitions:
                print(t)

        elif option == 6:
            sequence = input("\nAdd a sequence: ")
            if (fa.check_sequence(sequence)):
                print("Sequence accepted")
            else:
                print("Sequence rejected")

        option = int(input(
            "Input:\n  0 -> exit \n 1 -> Initial state \n 2 -> States\n 3 -> Alphabet\n 4 -> Final States\n 5 -> Transitions\n :"))
