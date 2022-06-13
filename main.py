import parser
from semantics import *

code = parser.main()
print(code)
check(Context(), code)