@pont_t = global i1 1, align 4
@pont_f = global i1 0, align 4
define i32 @teste(i32 %pont_a) {
ret i32 %pont_a
}
define i32 @max(i32 %pont_a, i32 %pont_b) {
%cas_2 = load i1,  i1* @pont_t
%cas_3 = call i32 @teste (i32 5)
%cas_4 = icmp sgt i32 %pont_a, %cas_3
%cas_5 = or i1 %cas_2, %cas_4
br i1 %cas_5, label %if_then_cas_1, label %else_thencas_1
if_then_cas_1:
ret i32 5
br label %if_else_fim_cas_1
else_thencas_1:
ret i32 %pont_b
if_else_fim_cas_1:
ret i32 5
}
define i32 @main() #0 {
   ret i32 0
}