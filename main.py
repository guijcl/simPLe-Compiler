import parser
from semantics import *
from codegen import *

code = parser.main()
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