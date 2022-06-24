	.text
	.file	"code.ll"
	.globl	teste                   # -- Begin function teste
	.p2align	4, 0x90
	.type	teste,@function
teste:                                  # @teste
	.cfi_startproc
# %bb.0:
	movl	%edi, %eax
	retq
.Lfunc_end0:
	.size	teste, .Lfunc_end0-teste
	.cfi_endproc
                                        # -- End function
	.globl	max                     # -- Begin function max
	.p2align	4, 0x90
	.type	max,@function
max:                                    # @max
	.cfi_startproc
# %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	pushq	%r14
	.cfi_def_cfa_offset 24
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset %rbx, -32
	.cfi_offset %r14, -24
	.cfi_offset %rbp, -16
	movl	%esi, %r14d
	movl	%edi, %ebp
	movb	pont_t(%rip), %bl
	movl	$5, %edi
	callq	teste
	testb	%bl, %bl
	jne	.LBB1_2
# %bb.1:
	cmpl	%eax, %ebp
	jg	.LBB1_2
# %bb.4:                                # %else_thencas_1
	movl	%r14d, %eax
	jmp	.LBB1_3
.LBB1_2:                                # %if_then_cas_1
	movl	$5, %eax
.LBB1_3:                                # %if_then_cas_1
	popq	%rbx
	.cfi_def_cfa_offset 24
	popq	%r14
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	retq
.Lfunc_end1:
	.size	max, .Lfunc_end1-max
	.cfi_endproc
                                        # -- End function
	.globl	main                    # -- Begin function main
	.p2align	4, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# %bb.0:
	xorl	%eax, %eax
	retq
.Lfunc_end2:
	.size	main, .Lfunc_end2-main
	.cfi_endproc
                                        # -- End function
	.type	pont_t,@object          # @pont_t
	.data
	.globl	pont_t
	.p2align	2
pont_t:
	.byte	1                       # 0x1
	.size	pont_t, 1

	.type	pont_f,@object          # @pont_f
	.bss
	.globl	pont_f
	.p2align	2
pont_f:
	.byte	0                       # 0x0
	.size	pont_f, 1

	.section	".note.GNU-stack","",@progbits
