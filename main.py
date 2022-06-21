import parser
from semantics import *

code = parser.main()
check(Context(), code)