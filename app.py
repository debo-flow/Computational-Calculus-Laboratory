import argparse
import json
from calculus.core.calculus_engine import CalculusEngine
from calculus.core.pipeline import master_calculus_workflow

def main():
    parser = argparse.ArgumentParser(description="Computational Calculus Laboratory CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available mathematical commands")

    # Workflow Command
    pipe_parser = subparsers.add_parser("analyze", help="Run master workflow on an expression")
    pipe_parser.add_argument("expression", type=str, help="Mathematical expression")

    # Calculus Commands
    diff_parser = subparsers.add_parser("diff", help="Differentiate an expression")
    diff_parser.add_argument("expression", type=str)
    diff_parser.add_argument("--var", type=str, default="x")

    int_parser = subparsers.add_parser("int", help="Integrate an expression")
    int_parser.add_argument("expression", type=str)
    int_parser.add_argument("--var", type=str, default="x")
    
    args = parser.parse_args()
    engine = CalculusEngine()

    if args.command == "analyze":
        report = master_calculus_workflow(args.expression)
        print(json.dumps(report, indent=4))
    elif args.command == "diff":
        print(f"Derivative: {engine.differentiate(args.expression, args.var)}")
    elif args.command == "int":
        print(f"Integral: {engine.integrate(args.expression, args.var)}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
