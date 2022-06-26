import sys
import os

import parser
from semantics import *
from codegen import *

def run_semantic_and_codegen(code):
    check(Context(), code)

    codigo_llvm = codegen(code, Context())
    print(codigo_llvm)
    with open("code.ll", "w") as f:
        f.write(codigo_llvm)
    import subprocess

    r = subprocess.call(
        "llc code.ll && clang code.s -o code && ./code",
        shell=True,
    )


def main():
    ok_tests = ["basic.simp", "basic_example.simp", "complex_example.simp", "functions_example.simp", "expressions_example.simp", "scopes_example.simp"]
    all_files = os.listdir("./tests/")

    args = sys.argv[1:]
    if len(args) > 1:
        print("Too many arguments")
        return

    if args[0] == "failed_tests":
        for f in all_files:
            if f not in ok_tests:
                code = parser.main(f)
                run_semantic_and_codegen(code)
                print("================== FINISHED ==================\n")
    elif args[0] == "ok_tests":
        for f in ok_tests:
            code = parser.main(f)
            run_semantic_and_codegen(code)
            print("================== FINISHED ==================\n")

    else:
        code = parser.main(args[0])
        run_semantic_and_codegen(code)
        print("================== FINISHED ==================\n")


if __name__ == '__main__':
    main()