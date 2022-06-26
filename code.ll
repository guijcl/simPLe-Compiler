@pont_b1 = global i1 0, align 4
@pont_b2 = global i1 0, align 4
@pont_n1 = global i32 0, align 4
@pont_n2 = global i32 1, align 4
@pont_f1 = global float 0.0, align 4
@pont_f2 = global float 1.5, align 4
define void @exp(i1 %cas_1, i32 %cas_2, float %cas_3) {
%pont_b = alloca i1
store i1 %cas_1, i1* %pont_b, align 4
%pont_n = alloca i32
store i32 %cas_2, i32* %pont_n, align 4
%pont_f = alloca float
store float %cas_3, float* %pont_f, align 4
%cas_4 = load i1, i1* %pont_b
store i1 %cas_4, i1* %pont_b, align 4
store i1 %cas_4, i1* @pont_b1, align 4
%cas_5 = load i32, i32* %pont_n
store i32 %cas_5, i32* %pont_n, align 4
store i32 %cas_5, i32* @pont_n1, align 4
%cas_6 = load float, float* %pont_f
store float %cas_6, float* %pont_f, align 4
store float %cas_6, float* @pont_f1, align 4
%pont_b3 = alloca i1
store i1 0, i1* %pont_b3, align 4
%cas_7 = load i1, i1* @pont_b1
%cas_8 = load i1, i1* @pont_b2
%cas_9 = and i1 %cas_7, %cas_8
store i1 %cas_9, i1* %pont_b3, align 4
%cas_10 = load i1, i1* @pont_b1
%cas_11 = load i1, i1* @pont_b2
%cas_12 = or i1 %cas_10, %cas_11
store i1 %cas_12, i1* %pont_b3, align 4
%cas_13 = load i32, i32* @pont_n1
%cas_14 = load i32, i32* @pont_n2
%cas_15 = icmp eq i32 %cas_13, %cas_14
%pont_b4 = alloca i1
store i1 %cas_15, i1* %pont_b4, align 4
%cas_16 = load i32, i32* @pont_n1
%cas_17 = load i32, i32* @pont_n2
%cas_18 = icmp ne i32 %cas_16, %cas_17
%pont_b5 = alloca i1
store i1 %cas_18, i1* %pont_b5, align 4
%cas_19 = load i1, i1* %pont_b4
store i1 %cas_19, i1* %pont_b4, align 4
%cas_20 = load i1, i1* %pont_b5
store i1 %cas_20, i1* %pont_b5, align 4
%cas_21 = and i1 %cas_19, %cas_20
store i1 %cas_21, i1* %pont_b3, align 4
%cas_22 = load i32, i32* @pont_n1
%cas_23 = load i32, i32* @pont_n2
%cas_24 = icmp sge i32 %cas_22, %cas_23
store i1 %cas_24, i1* %pont_b4, align 4
%cas_25 = load i32, i32* @pont_n1
%cas_26 = load i32, i32* @pont_n2
%cas_27 = icmp sgt i32 %cas_25, %cas_26
store i1 %cas_27, i1* %pont_b5, align 4
%cas_28 = load i1, i1* %pont_b4
store i1 %cas_28, i1* %pont_b4, align 4
%cas_29 = load i1, i1* %pont_b5
store i1 %cas_29, i1* %pont_b5, align 4
%cas_30 = or i1 %cas_28, %cas_29
store i1 %cas_30, i1* %pont_b3, align 4
%cas_31 = load i1, i1* %pont_b3
store i1 %cas_31, i1* %pont_b3, align 4
%cas_32 = xor i1 1, %cas_31
store i1 %cas_32, i1* %pont_b3, align 4
%cas_33 = load i32, i32* @pont_n1
%cas_34 = load i32, i32* @pont_n2
%cas_35 = icmp sle i32 %cas_33, %cas_34
store i1 %cas_35, i1* %pont_b4, align 4
%cas_36 = load i32, i32* @pont_n1
%cas_37 = load i32, i32* @pont_n2
%cas_38 = icmp slt i32 %cas_36, %cas_37
store i1 %cas_38, i1* %pont_b5, align 4
%cas_39 = load float, float* @pont_f1
%cas_40 = load float, float* @pont_f2
%cas_41 = fadd float %cas_40, 2.5
%cas_42 = fcmp ogt float %cas_39, %cas_41
%cas_43 = load i1, i1* %pont_b4
store i1 %cas_43, i1* %pont_b4, align 4
%cas_44 = or i1 %cas_42, %cas_43
%cas_45 = load i1, i1* %pont_b5
store i1 %cas_45, i1* %pont_b5, align 4
%cas_46 = and i1 %cas_44, %cas_45
store i1 %cas_46, i1* %pont_b3, align 4
%cas_47 = load i32, i32* %pont_n
store i32 %cas_47, i32* %pont_n, align 4
%cas_48 = load i32, i32* @pont_n2
%cas_49 = mul i32 %cas_47, %cas_48
store i32 %cas_49, i32* @pont_n1, align 4
%cas_50 = load i32, i32* %pont_n
store i32 %cas_50, i32* %pont_n, align 4
%cas_51 = add i32 5, %cas_50
store i32 %cas_51, i32* @pont_n1, align 4
%cas_52 = load i32, i32* @pont_n1
%cas_53 = sdiv i32 %cas_52, 2
store i32 %cas_53, i32* @pont_n1, align 4
%cas_54 = load i32, i32* @pont_n2
%cas_55 = load i32, i32* %pont_n
store i32 %cas_55, i32* %pont_n, align 4
%cas_56 = srem i32 %cas_54, %cas_55
store i32 %cas_56, i32* @pont_n1, align 4
%cas_57 = sub i32 5, 2
store i32 %cas_57, i32* @pont_n1, align 4
ret void
}
define i32 @main() {
call void @exp (i1 0, i32 2, float 2.5)
ret i32 0
}