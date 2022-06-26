	.text
	.file	"code.ll"
	.section	.rodata.cst4,"aM",@progbits,4
	.p2align	2               # -- Begin function exp
.LCPI0_0:
	.long	1075838976              # float 2.5
	.text
	.globl	exp
	.p2align	4, 0x90
	.type	exp,@function
exp:                                    # @exp
	.cfi_startproc
# %bb.0:
	andb	$1, %dil
	movb	%dil, -9(%rsp)
	movl	%esi, -4(%rsp)
	movss	%xmm0, -8(%rsp)
	movb	%dil, pont_b1(%rip)
	movss	%xmm0, pont_f1(%rip)
	cmpl	pont_n2(%rip), %esi
	setle	%al
	setle	-11(%rsp)
	setl	%cl
	setl	-12(%rsp)
	movss	pont_f2(%rip), %xmm1    # xmm1 = mem[0],zero,zero,zero
	addss	.LCPI0_0(%rip), %xmm1
	ucomiss	%xmm1, %xmm0
	seta	%dl
	orb	%al, %dl
	andb	%cl, %dl
	movb	%dl, -10(%rsp)
	movl	$3, pont_n1(%rip)
	retq
.Lfunc_end0:
	.size	exp, .Lfunc_end0-exp
	.cfi_endproc
                                        # -- End function
	.section	.rodata.cst4,"aM",@progbits,4
	.p2align	2               # -- Begin function main
.LCPI1_0:
	.long	1075838976              # float 2.5
	.text
	.globl	main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:
	pushq	%rax
	.cfi_def_cfa_offset 16
	movss	.LCPI1_0(%rip), %xmm0   # xmm0 = mem[0],zero,zero,zero
	xorl	%edi, %edi
	movl	$2, %esi
	callq	exp
	xorl	%eax, %eax
	popq	%rcx
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end1:
	.size	main, .Lfunc_end1-main
	.cfi_endproc
                                        # -- End function
	.type	pont_b1,@object         # @pont_b1
	.bss
	.globl	pont_b1
	.p2align	2
pont_b1:
	.byte	0                       # 0x0
	.size	pont_b1, 1

	.type	pont_b2,@object         # @pont_b2
	.globl	pont_b2
	.p2align	2
pont_b2:
	.byte	0                       # 0x0
	.size	pont_b2, 1

	.type	pont_n1,@object         # @pont_n1
	.globl	pont_n1
	.p2align	2
pont_n1:
	.long	0                       # 0x0
	.size	pont_n1, 4

	.type	pont_n2,@object         # @pont_n2
	.data
	.globl	pont_n2
	.p2align	2
pont_n2:
	.long	1                       # 0x1
	.size	pont_n2, 4

	.type	pont_f1,@object         # @pont_f1
	.bss
	.globl	pont_f1
	.p2align	2
pont_f1:
	.long	0                       # float 0
	.size	pont_f1, 4

	.type	pont_f2,@object         # @pont_f2
	.data
	.globl	pont_f2
	.p2align	2
pont_f2:
	.long	1069547520              # float 1.5
	.size	pont_f2, 4

	.section	".note.GNU-stack","",@progbits
