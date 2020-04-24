import argparse


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

        parser_rel = subparsers.add_parser('reliability', description='Generate a network design meeting the given'
                                                                      ' reliability goal (not necessarily, minimum cost')
        parser_rel.add_argument('reliability', type=float, nargs=1,
                                help="Reliability Goal for this design (must be between 0 and 1)")

        parser_cost = subparsers.add_parser('cost', description='Generate a network design meeting the given cost '
                                                                'constraint, with maximal reliability.')

        parser_cost.add_argument('cost', type=int, nargs=1,
                                 help="Cost Constraint")

        args = parser.parse_args()

        getattr(self, args.command)()

    def reliability(self):
        print("reliability initiated")

    def cost(self):
        print("cost initiated")