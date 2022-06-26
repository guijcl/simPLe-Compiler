	.text
	.file	"code.ll"
	.globl	helloworld              # -- Begin function helloworld
	.p2align	4, 0x90
	.type	helloworld,@function
helloworld:                             # @helloworld
	.cfi_startproc
# %bb.0:
	movl	$.L.casual_str_cas_1, %eax
	retq
.Lfunc_end0:
	.size	helloworld, .Lfunc_end0-helloworld
	.cfi_endproc
                                        # -- End function
	.globl	max                     # -- Begin function max
	.p2align	4, 0x90
	.type	max,@function
max:                                    # @max
	.cfi_startproc
# %bb.0:
	pushq	%rax
	.cfi_def_cfa_offset 16
	movl	%edi, 4(%rsp)
	movl	%esi, (%rsp)
	callq	helloworld
	movl	4(%rsp), %eax
	cmpl	(%rsp), %eax
	jle	.LBB1_2
# %bb.1:                                # %if_then_cas_5
	movl	4(%rsp), %eax
	popq	%rcx
	.cfi_def_cfa_offset 8
	retq
.LBB1_2:                                # %if_fim_cas_5
	.cfi_def_cfa_offset 16
	movl	(%rsp), %eax
	popq	%rcx
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end1:
	.size	max, .Lfunc_end1-max
	.cfi_endproc
                                        # -- End function
	.globl	myfunction              # -- Begin function myfunction
	.p2align	4, 0x90
	.type	myfunction,@function
myfunction:                             # @myfunction
	.cfi_startproc
# %bb.0:
	pushq	%rax
	.cfi_def_cfa_offset 16
	movl	%edi, (%rsp)
	movl	$2, %edi
	movl	$100, %esi
	callq	max
	movl	%eax, 4(%rsp)
	cmpl	$999, (%rsp)            # imm = 0x3E7
	jle	.LBB2_2
	jmp	.LBB2_8
	.p2align	4, 0x90
.LBB2_4:                                # %if_then_cas_16
                                        #   in Loop: Header=BB2_2 Depth=1
	movl	(%rsp), %eax
	imull	pont_multiplierdois(%rip), %eax
	movl	%eax, (%rsp)
	cmpl	$999, (%rsp)            # imm = 0x3E7
	jg	.LBB2_8
.LBB2_2:                                # %while_body_cas_13
                                        # =>This Inner Loop Header: Depth=1
	movl	4(%rsp), %ecx
	leal	2(%rcx), %edx
	movl	(%rsp), %eax
	cmpl	%eax, %edx
	setge	%dl
	cmpl	$20, %ecx
	setl	%cl
	testb	%cl, %dl
	jne	.LBB2_4
# %bb.3:                                # %while_body_cas_13
                                        #   in Loop: Header=BB2_2 Depth=1
	imull	pont_multiplier(%rip), %eax
	cmpl	$101, %eax
	jge	.LBB2_4
# %bb.5:                                # %else_thencas_16
                                        #   in Loop: Header=BB2_2 Depth=1
	movl	4(%rsp), %eax
	movl	pont_multiplier(%rip), %ecx
	imull	%eax, %ecx
	cmpl	%ecx, %eax
	jge	.LBB2_7
# %bb.6:                                # %if_then_cas_32
                                        #   in Loop: Header=BB2_2 Depth=1
	addl	$100, 4(%rsp)
.LBB2_7:                                # %if_fim_cas_32
                                        #   in Loop: Header=BB2_2 Depth=1
	movl	4(%rsp), %eax
	subl	%eax, (%rsp)
	cmpl	$999, (%rsp)            # imm = 0x3E7
	jle	.LBB2_2
.LBB2_8:                                # %while_fim_cas_13
	movl	(%rsp), %eax
	movl	%eax, %ecx
	shrl	$31, %ecx
	addl	%eax, %ecx
	andl	$-2, %ecx
	subl	%ecx, %eax
	cmpl	$1, %eax
	sete	%al
	popq	%rcx
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end2:
	.size	myfunction, .Lfunc_end2-myfunction
	.cfi_endproc
                                        # -- End function
	.globl	returnstring            # -- Begin function returnstring
	.p2align	4, 0x90
	.type	returnstring,@function
returnstring:                           # @returnstring
	.cfi_startproc
# %bb.0:
	movq	%rdi, -8(%rsp)
	movl	$.L.casual_str_cas_48, %eax
	retq
.Lfunc_end3:
	.size	returnstring, .Lfunc_end3-returnstring
	.cfi_endproc
                                        # -- End function
	.globl	main                    # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:
	pushq	%rax
	.cfi_def_cfa_offset 16
	movl	$10, %edi
	callq	myfunction
	andb	$1, %al
	movb	%al, 7(%rsp)
	movl	$.L.casual_str_cas_52, %edi
	callq	returnstring
	xorl	%eax, %eax
	popq	%rcx
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end4:
	.size	main, .Lfunc_end4-main
	.cfi_endproc
                                        # -- End function
	.type	.L.casual_str_cas_52,@object # @.casual_str_cas_52
	.section	.rodata.str1.1,"aMS",@progbits,1
.L.casual_str_cas_52:
	.asciz	"%cas_51"
	.size	.L.casual_str_cas_52, 8

	.type	.L.casual_str_cas_48,@object # @.casual_str_cas_48
.L.casual_str_cas_48:
	.asciz	"%cas_47"
	.size	.L.casual_str_cas_48, 8

	.type	.L.casual_str_cas_1,@object # @.casual_str_cas_1
.L.casual_str_cas_1:
	.asciz	"Hello World"
	.size	.L.casual_str_cas_1, 12

	.type	.L.casual_str_pont_const,@object # @.casual_str_pont_const
.L.casual_str_pont_const:
	.asciz	"Goodbye World"
	.size	.L.casual_str_pont_const, 14

	.type	pont_const,@object      # @pont_const
	.data
	.globl	pont_const
	.p2align	3
pont_const:
	.quad	.L.casual_str_pont_const
	.size	pont_const, 8

	.type	pont_multiplier,@object # @pont_multiplier
	.globl	pont_multiplier
	.p2align	2
pont_multiplier:
	.long	3                       # 0x3
	.size	pont_multiplier, 4

	.type	pont_multiplierdois,@object # @pont_multiplierdois
	.globl	pont_multiplierdois
	.p2align	2
pont_multiplierdois:
	.long	5                       # 0x5
	.size	pont_multiplierdois, 4

	.section	".note.GNU-stack","",@progbits
