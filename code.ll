@.casual_str_cas_52 = private unnamed_addr constant [8 x i8] c"%cas_51\00", align 1
@.casual_str_cas_48 = private unnamed_addr constant [8 x i8] c"%cas_47\00", align 1
@.casual_str_cas_1 = private unnamed_addr constant [12 x i8] c"Hello World\00", align 1
@.casual_str_pont_const = private unnamed_addr constant [14 x i8] c"Goodbye World\00", align 1
@pont_const = global i8* getelementptr inbounds ([14 x i8], [14 x i8]* @.casual_str_pont_const, i32 0, i32 0)
@pont_multiplier = global i32 3, align 4
@pont_multiplierdois = global i32 5, align 4
define i8* @helloworld() {
ret i8* getelementptr inbounds ([12 x i8], [12 x i8]* @.casual_str_cas_1, i64 0, i64 0)
}
define i32 @max(i32 %cas_2, i32 %cas_3) {
%pont_a = alloca i32
store i32 %cas_2, i32* %pont_a, align 4
%pont_b = alloca i32
store i32 %cas_3, i32* %pont_b, align 4
%cas_4 = call i8* @helloworld()
%cas_6 = load i32, i32* %pont_a
store i32 %cas_6, i32* %pont_a, align 4
%cas_7 = load i32, i32* %pont_b
store i32 %cas_7, i32* %pont_b, align 4
%cas_8 = icmp sgt i32 %cas_6, %cas_7
br i1 %cas_8, label %if_then_cas_5, label %if_fim_cas_5
if_then_cas_5:
%cas_9 = load i32, i32* %pont_a
store i32 %cas_9, i32* %pont_a, align 4
ret i32 %cas_9
br label %if_fim_cas_5
if_fim_cas_5:
%cas_10 = load i32, i32* %pont_b
store i32 %cas_10, i32* %pont_b, align 4
ret i32 %cas_10
}
define i1 @myfunction(i32 %cas_11) {
%pont_num = alloca i32
store i32 %cas_11, i32* %pont_num, align 4
%cas_12 = call i32 @max (i32 2, i32 100)
%pont_maxnum = alloca i32
store i32 %cas_12, i32* %pont_maxnum, align 4
br label %while_inicio_cas_13
while_inicio_cas_13:
%cas_14 = load i32, i32* %pont_num
store i32 %cas_14, i32* %pont_num, align 4
%cas_15 = icmp slt i32 %cas_14, 1000
br i1 %cas_15, label %while_body_cas_13, label %while_fim_cas_13
while_body_cas_13:
%cas_17 = load i32, i32* %pont_maxnum
store i32 %cas_17, i32* %pont_maxnum, align 4
%cas_18 = add i32 %cas_17, 2
%cas_19 = load i32, i32* %pont_num
store i32 %cas_19, i32* %pont_num, align 4
%cas_20 = icmp sge i32 %cas_18, %cas_19
%cas_21 = load i32, i32* %pont_maxnum
store i32 %cas_21, i32* %pont_maxnum, align 4
%cas_22 = icmp slt i32 %cas_21, 20
%cas_23 = and i1 %cas_20, %cas_22
%cas_24 = load i32, i32* %pont_num
store i32 %cas_24, i32* %pont_num, align 4
%cas_25 = load i32, i32* @pont_multiplier
%cas_26 = mul i32 %cas_24, %cas_25
%cas_27 = icmp sgt i32 %cas_26, 100
%cas_28 = or i1 %cas_23, %cas_27
br i1 %cas_28, label %if_then_cas_16, label %else_thencas_16
if_then_cas_16:
%cas_29 = load i32, i32* %pont_num
store i32 %cas_29, i32* %pont_num, align 4
%cas_30 = load i32, i32* @pont_multiplierdois
%cas_31 = mul i32 %cas_29, %cas_30
store i32 %cas_31, i32* %pont_num, align 4
br label %if_else_fim_cas_16
else_thencas_16:
%cas_33 = load i32, i32* %pont_maxnum
store i32 %cas_33, i32* %pont_maxnum, align 4
%cas_34 = load i32, i32* %pont_maxnum
store i32 %cas_34, i32* %pont_maxnum, align 4
%cas_35 = load i32, i32* @pont_multiplier
%cas_36 = mul i32 %cas_34, %cas_35
%cas_37 = icmp slt i32 %cas_33, %cas_36
br i1 %cas_37, label %if_then_cas_32, label %if_fim_cas_32
if_then_cas_32:
%cas_38 = load i32, i32* %pont_maxnum
store i32 %cas_38, i32* %pont_maxnum, align 4
%cas_39 = add i32 %cas_38, 100
store i32 %cas_39, i32* %pont_maxnum, align 4
br label %if_fim_cas_32
if_fim_cas_32:
%cas_40 = load i32, i32* %pont_num
store i32 %cas_40, i32* %pont_num, align 4
%cas_41 = load i32, i32* %pont_maxnum
store i32 %cas_41, i32* %pont_maxnum, align 4
%cas_42 = sub i32 %cas_40, %cas_41
store i32 %cas_42, i32* %pont_num, align 4
br label %if_else_fim_cas_16
if_else_fim_cas_16:
br label %while_inicio_cas_13
while_fim_cas_13:
%cas_43 = load i32, i32* %pont_num
store i32 %cas_43, i32* %pont_num, align 4
%cas_44 = srem i32 %cas_43, 2
%cas_45 = icmp eq i32 %cas_44, 1
ret i1 %cas_45
}
declare float @uselessdeclaredfunction(i32, float, i8*, i1)
define i8* @returnstring(i8* %cas_46) {
%pont_s = alloca i8*
store i8* %cas_46, i8** %pont_s, align 4
%cas_47 = load i8*, i8** %pont_s
store i8* %cas_47, i8** %pont_s, align 4
ret i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.casual_str_cas_48, i64 0, i64 0)
}
define i32 @main() {
%cas_49 = call i1 @myfunction (i32 10)
%pont_res = alloca i1
store i1 %cas_49, i1* %pont_res, align 4
%cas_51 = load i8*, i8** @pont_const
%cas_50 = call i8* @returnstring (i8* getelementptr inbounds ([8 x i8], [8 x i8]* @.casual_str_cas_52, i64 0, i64 0))
ret i32 0
}