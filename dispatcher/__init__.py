import argparse

from graphs import Edge, enhancer
from parsing import generate, write_result


class Dispatcher(object):
    def __init__(self):
        parser = argparse.ArgumentParser(description='Generate a Network Design')
        parser.add_argument('--input', '-i', nargs=1, action='store', default='input.txt', type=argparse.FileType('r'),
                            help='Input file containing symmetric reliabilities then costs in row major form '
                                 '(default: input.txt)'
                            )

        parser.add_argument('--output', '-o', nargs=1, action='store', default='output.txt', type=argparse.FileType('w'),
                            help='Output file containing selected edges'
                                 ' (default: output.txt)'
                            )

        subparsers = parser.add_subparsers(help='Sub-command help', dest='command', required=True)

        parser_rel = subparsers.add_parser('reliability', description='Generate a network design meeting the given '
                                                                      'reliability goal (not necessarily, minimum cost)'
                                           )
        parser_rel.add_argument('reliability', type=float, nargs=1,
                                help="Reliability Goal for this design (must be between 0 and 1)")

        parser_cost = subparsers.add_parser('cost', description='Generate a network design meeting the given cost '
                                                                'constraint, with maximal reliability.')

        parser_cost.add_argument('cost', type=int, nargs=1,
                                 help="Cost Constraint")

        args = parser.parse_args()

        try:
            self.rel_goal = args.reliability[0]
        except AttributeError as e:
            self.rel_goal = 0

        try:
            self.cost_goal = args.cost[0]
        except AttributeError as e:
            self.cost_goal = 1000000

        getattr(self, args.command)(args.input, args.output)

    def reliability(self, input_file, output_file):
        print("Attempting to generate Network meeting Reliability Goal: {} ...".format(self.rel_goal))
        network = generate(input_file)
        max_reliability = network.compute_reliability()
        if max_reliability > self.rel_goal:
            self.print_output(network)
            write_result(network, output_file)
        else:
            print("Could not find Network satisfying Reliability Goal!")
            output_file.write("N/A")

    def cost(self, input_file, output_file):
        print("Attempting to generate network with Maximal Reliability under Cost Constraint: {} ...".format(self.cost_goal))
        network = generate(input_file)
        cost_mst = network.find_mst(Edge.get_cost)
        maximized = enhancer.enhance_cost(network, cost_mst, self.cost_goal)
        if maximized:
            self.print_output(maximized)
            write_result(maximized, output_file)
        else:
            print("There is no connected Network meeting Cost Goal!")
            output_file.write("N/A")

    @staticmethod
    def print_output(network):
        print("Found Network satisfying Reliability Goal!")
        print("Reliability: {}".format(network.compute_reliability()))
        print("Cost: {}".format(network.compute_cost()))
        print(network.edges)